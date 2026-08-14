#!/usr/bin/env python3
"""Read-only comparison of Drive SKILL.md files against a local GitHub skills repository."""

from __future__ import annotations

import argparse
import csv
import json
import re
import subprocess
import sys
from collections import defaultdict
from pathlib import Path
from typing import Any


DEFAULT_QUERY = "name = 'SKILL.md' and trashed = false"


def run(command: list[str], *, check: bool = True) -> subprocess.CompletedProcess[str]:
    result = subprocess.run(command, text=True, capture_output=True, check=False)
    if check and result.returncode:
        message = result.stderr.strip() or result.stdout.strip() or "command failed"
        raise RuntimeError(f"{' '.join(command[:4])}: {message}")
    return result


def normalize(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", value.lower())


def markdown_cell(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", " ").strip() or "—"


def frontmatter(text: str) -> str:
    if not text.startswith("---\n"):
        return ""
    end = text.find("\n---", 4)
    return text[4:end] if end >= 0 else ""


def yaml_field(block: str, key: str) -> str:
    lines = block.splitlines()
    pattern = re.compile(rf"^{re.escape(key)}:\s*(.*)$")
    for index, line in enumerate(lines):
        match = pattern.match(line)
        if not match:
            continue
        value = match.group(1).strip()
        if value in {">", "|", ">-", "|-", ">+", "|+"}:
            collected: list[str] = []
            for candidate in lines[index + 1 :]:
                if candidate and not candidate[0].isspace():
                    break
                if candidate.strip():
                    collected.append(candidate.strip())
            return " ".join(collected)
        return value.strip('"\'')
    return ""


def inline_description(text: str) -> str:
    match = re.search(r"^\*\*Description:\*\*\s*(.+)$", text, flags=re.M)
    return match.group(1).strip() if match else ""


def first_sentence(value: str) -> str:
    value = re.sub(r"\s+", " ", value).strip()
    return re.split(r"(?<=[.!?])\s+", value, maxsplit=1)[0] if value else ""


def parse_skill_file(path: Path) -> tuple[str, str]:
    text = path.read_text(encoding="utf-8", errors="replace")
    block = frontmatter(text)
    name = yaml_field(block, "name")
    if not name:
        heading = re.search(r"^#\s+(.+?)\s*$", text, flags=re.M)
        name = heading.group(1).strip() if heading else ""
    description = yaml_field(block, "description") or inline_description(text)
    return name, first_sentence(description)


def parse_ndjson(output: str) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    for line in output.splitlines():
        line = line.strip()
        if line:
            records.extend(json.loads(line).get("files", []))
    return records


def list_drive_skills(query: str) -> list[dict[str, Any]]:
    params = {
        "q": query,
        "pageSize": 1000,
        "orderBy": "modifiedTime desc",
        "fields": "files(id,name,mimeType,parents,modifiedTime,size,webViewLink),nextPageToken",
    }
    result = run(["gws", "drive", "files", "list", "--params", json.dumps(params), "--page-all", "--format", "json"])
    return parse_ndjson(result.stdout)


def get_drive_folder_name(folder_id: str, cache: dict[str, str]) -> str:
    if not folder_id:
        return ""
    if folder_id in cache:
        return cache[folder_id]
    params = {"fileId": folder_id, "fields": "id,name,mimeType,parents"}
    result = run(["gws", "drive", "files", "get", "--params", json.dumps(params)], check=False)
    if result.returncode:
        cache[folder_id] = ""
        return ""
    try:
        cache[folder_id] = json.loads(result.stdout).get("name", "")
    except json.JSONDecodeError:
        cache[folder_id] = ""
    return cache[folder_id]


def download_drive_file(file_id: str, destination: Path) -> bool:
    params = {"fileId": file_id, "alt": "media"}
    result = run(
        ["gws", "drive", "files", "get", "--params", json.dumps(params), "--output", str(destination)],
        check=False,
    )
    return result.returncode == 0 and destination.exists()


def github_inventory(repo: Path) -> list[dict[str, str]]:
    skills_root = repo / ".grok" / "skills"
    if not skills_root.is_dir():
        raise RuntimeError(f"Expected skills directory not found: {skills_root}")
    inventory = []
    for skill_file in sorted(skills_root.glob("*/SKILL.md")):
        declared_name, _ = parse_skill_file(skill_file)
        inventory.append({"name": declared_name or skill_file.parent.name, "directory": skill_file.parent.name})
    if not inventory:
        raise RuntimeError(f"No SKILL.md files found under {skills_root}")
    return inventory


def verify_repo(repo: Path, repo_slug: str) -> tuple[str, str]:
    local_commit = run(["git", "-C", str(repo), "rev-parse", "HEAD"]).stdout.strip()
    if not repo_slug:
        return local_commit, ""
    remote = run(["gh", "api", f"repos/{repo_slug}/commits/main", "--jq", ".sha"], check=False)
    remote_commit = remote.stdout.strip() if remote.returncode == 0 else "unavailable"
    return local_commit, remote_commit


def make_report(rows: list[dict[str, str]], github_count: int, local_commit: str, remote_commit: str, output: Path) -> None:
    unmatched = [row for row in rows if row["status"] == "Not found on GitHub"]
    unique_keys = {row["candidate_key"] for row in unmatched}
    matched = len(rows) - len(unmatched)
    lines = [
        "# Google Drive vs. GitHub Skills Comparison",
        "",
        "This report was generated through read-only Drive listing and download operations. Downloaded skill definitions were parsed as data and were not executed.",
        "",
        "| Metric | Count / value |",
        "|---|---:|",
        f"| Drive `SKILL.md` files examined | {len(rows)} |",
        f"| GitHub skill definitions examined | {github_count} |",
        f"| Drive files matched to GitHub | {matched} |",
        f"| Drive files not found by name | {len(unmatched)} |",
        f"| Unique unmatched candidate names | {len(unique_keys)} |",
        f"| Local GitHub commit | `{local_commit}` |",
    ]
    if remote_commit:
        lines.append(f"| Remote `main` commit | `{remote_commit}` |")
    lines.extend([
        "",
        "## Unmatched Drive candidates",
        "",
        "| Candidate | Drive folder | Declared name | Brief description | Modified (UTC) | Drive file |",
        "|---|---|---|---|---|---|",
    ])
    if unmatched:
        for row in unmatched:
            link = row["web_view_link"] or f"https://drive.google.com/file/d/{row['drive_file_id']}/view"
            lines.append(
                f"| `{markdown_cell(row['candidate_key'])}` | {markdown_cell(row['folder_name'])} | "
                f"{markdown_cell(row['declared_name'])} | {markdown_cell(row['description'])} | "
                f"{markdown_cell(row['modified_time'])} | [Open]({link}) |"
            )
    else:
        lines.append("| — | — | — | Every examined Drive skill matched a GitHub skill. | — | — |")
    lines.extend([
        "",
        "## All compared files",
        "",
        "| Candidate | GitHub status | GitHub name | Drive folder | Declared name | Modified (UTC) |",
        "|---|---|---|---|---|---|",
    ])
    for row in rows:
        lines.append(
            f"| `{markdown_cell(row['candidate_key'])}` | {row['status']} | {markdown_cell(row['github_name'])} | "
            f"{markdown_cell(row['folder_name'])} | {markdown_cell(row['declared_name'])} | {markdown_cell(row['modified_time'])} |"
        )
    lines.extend([
        "",
        "## Interpretation",
        "",
        "An unmatched result means that neither the Drive skill’s declared name nor its immediate parent-folder name had an exact normalized match among the GitHub skill names and folders. Treat functionally similar names as review candidates, not matches. Search scope is limited to Drive files that satisfy the configured query.",
        "",
    ])
    output.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", required=True, type=Path, help="Local clone of the GitHub skills repository")
    parser.add_argument("--repo-slug", default="", help="Optional owner/repository slug used to verify remote main")
    parser.add_argument("--output-dir", required=True, type=Path, help="Directory for CSV, Markdown, and read-only downloads")
    parser.add_argument("--drive-query", default=DEFAULT_QUERY, help="Drive API query; defaults to all non-trashed SKILL.md files")
    args = parser.parse_args()

    args.output_dir.mkdir(parents=True, exist_ok=True)
    downloads_dir = args.output_dir / "downloads"
    downloads_dir.mkdir(exist_ok=True)
    drive_files = list_drive_skills(args.drive_query)
    github = github_inventory(args.repo)
    by_name = {normalize(item["name"]): item for item in github}
    by_directory = {normalize(item["directory"]): item for item in github}
    folders: dict[str, str] = {}
    rows: list[dict[str, str]] = []

    for item in drive_files:
        file_id = item["id"]
        destination = downloads_dir / f"{file_id}_SKILL.md"
        if not download_drive_file(file_id, destination):
            rows.append({
                "drive_file_id": file_id, "folder_name": "", "declared_name": "", "description": "",
                "modified_time": item.get("modifiedTime", ""), "web_view_link": item.get("webViewLink", ""),
                "candidate_key": file_id, "status": "Download failed", "github_name": "",
            })
            continue
        declared_name, description = parse_skill_file(destination)
        parent_id = (item.get("parents") or [""])[0]
        folder_name = get_drive_folder_name(parent_id, folders)
        match = None
        for candidate in (declared_name, folder_name):
            if normalize(candidate) in by_name:
                match = by_name[normalize(candidate)]
                break
            if normalize(candidate) in by_directory:
                match = by_directory[normalize(candidate)]
                break
        candidate_key = declared_name or folder_name or file_id
        rows.append({
            "drive_file_id": file_id,
            "folder_name": folder_name,
            "declared_name": declared_name,
            "description": description,
            "modified_time": item.get("modifiedTime", ""),
            "web_view_link": item.get("webViewLink", ""),
            "candidate_key": candidate_key,
            "status": "Published" if match else "Not found on GitHub",
            "github_name": match["name"] if match else "",
        })

    rows.sort(key=lambda row: (row["candidate_key"].lower(), row["drive_file_id"]))
    csv_path = args.output_dir / "drive_github_skill_comparison.csv"
    with csv_path.open("w", newline="", encoding="utf-8") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(rows[0]) if rows else ["drive_file_id"])
        writer.writeheader()
        writer.writerows(rows)
    local_commit, remote_commit = verify_repo(args.repo, args.repo_slug)
    report_path = args.output_dir / "drive_github_skill_comparison.md"
    make_report(rows, len(github), local_commit, remote_commit, report_path)
    print(f"drive_files_examined={len(rows)}")
    print(f"github_skill_definitions={len(github)}")
    print(f"not_found={sum(row['status'] == 'Not found on GitHub' for row in rows)}")
    print(f"report={report_path}")
    print(f"csv={csv_path}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except RuntimeError as error:
        print(f"error: {error}", file=sys.stderr)
        raise SystemExit(1)
