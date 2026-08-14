---
name: contact-vcard-export
description: "Create a validated vCard contact-export file from contact details that the user has explicitly selected and confirmed. Use for: create VCF, export contacts, vCard file, contact import file."
license: MIT
metadata:
  version: 1.0.0
  author: Stijnman
  grok:
    tags: [create VCF, export contacts, vCard file, contact import file]
---

# Contact vCard Export

## Purpose

Create a portable `.vcf` file for contacts the user explicitly identifies, validates, and approves for export.

## Workflow

1. Ask the user to confirm the selected contacts and the fields to include.
2. Normalize phone numbers only when the country context is known; otherwise preserve the supplied value and flag it for review.
3. Include only verified fields such as name, phone, email, organization, address, or note.
4. Generate vCard 3.0 or 4.0 entries with escaped text and a descriptive filename.
5. Validate that each card contains a display name and that no phone number, email, or note was unintentionally added.
6. Present the file as an export; never claim it was imported into a device address book.

## Privacy boundaries

Do not automatically mine contacts from screenshots, prior conversation, or third-party sources. Treat contact details as sensitive personal data. Do not create or send the file until the user has confirmed the selected records.

## Error handling

| Situation | Response |
|---|---|
| Name or number is ambiguous | Ask for the missing or corrected value. |
| Country code is unknown | Preserve the provided format and request confirmation. |
| Duplicate contact appears | Show the duplication and ask whether to merge or retain separate entries. |
| Invalid field characters occur | Escape them according to vCard rules and report any transformation. |
