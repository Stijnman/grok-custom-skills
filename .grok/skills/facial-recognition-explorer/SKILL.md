---
name: facial-recognition-explorer
description: Explains modern face recognition, NIST-class closeness, embeddings, ArcFace/AdaFace/TransFace, and qualitative lookalike comparison. Triggered by facial recognition, face embeddings, ArcFace, AdaFace, NIST FRTE, how close is FR, lookalike match, or improve this face skill.
metadata:
  version: "1.1"
  type: knowledge
  created: "2026-09-10"
  updated: "2026-09-10"
---

# Facial Recognition Explorer

Default to the 2025–2026 embedding stack. Do not open with Eigenfaces unless the user asks for history.

## Current stack

1. Detect — RetinaFace, SCRFD, YuNet, BlazeFace. Transformer detectors (SFE-DETR class) for tiny faces.
2. Align — 5-point landmarks, affine warp to 112x112.
3. Embed — L2-normalized 512-D vector (IR-SE, ResNet, MobileFace, ViT / TransFace).
4. Score — cosine on unit vectors. Thresholds are model-specific. Never reuse a FaceNet 0.40 cutoff on ArcFace.

Loss lineage

- FaceNet triplet loss — useful intuition, painful mining, legacy.
- CosFace — additive cosine margin.
- ArcFace — additive angular margin. Still the default open checkpoint.
- AdaFace — quality-adaptive margin. Prefer this for blurry or surveillance frames.
- MagFace / ElasticFace / TransFace — quality-aware or ViT variants. LFW is saturated; rank on IJB and NIST FRTE.

See `references/sota-2026.md` for dated numbers.

## How close it is (say this first)

Solved regime

- Frontal mugshot vs mugshot, same era, large gallery. Top NIST FRTE 1-N systems cluster around 0.1% FNIR on high-quality frontal identification and stay usable at 12M identities (leaders reported ~1.11% FNIR at FPIR 0.1% on that scale in 2026 coverage).
- Error vs 2010 is roughly 50–60x lower. Easy pairs are past human-level.

Unsolved regime

- Profile vs frontal (vendor spread is still large).
- 15–20 year aging and injury (NIST residual-error story).
- Wild video, motion blur, low res, heavy makeup, surgery, twins.
- Webcam-to-mugshot is better than it was but not mugshot-to-mugshot.

LFW 99.8%+ is a history slide, not a ranking tool.

Do not invent a cosine score. This sandbox does not ship a live InsightFace/ArcFace runtime by default. If inference is not actually run, stay qualitative and say so.

## Two-photo protocol

When the user pastes a live face and a historical face (or asks “find a similar one”):

1. Visual first — hairline, face width, brow ridge, smile shape, facial hair, age, pose.
2. Embedder reality — after alignment the crop is inner face. Hoodie vs suit is noise. Hairline is weak. Generated lookalikes are not biometric hits.
3. Verdict language
   - Similar expression / similar grooming
   - Different bone structure / different age cohort
   - Would likely fail a tight 1-1 threshold
   - Would confuse a sloppy human glance
4. Never claim identity from a generated image.

## Explain-a-bit template

1. Newest useful thing — quality-aware margins (AdaFace), ViT face models, synthetic IDs, NIST 1-N at national scale.
2. How close — solved vs unsolved bullets above.
3. Mechanism — detect, align, unit embedding, cosine.
4. Math if asked — ArcFace target logit \(s\cos(\theta_y+m)\), typical \(s=64\), \(m=0.5\).
5. Practical — take an InsightFace or AdaFace checkpoint, calibrate threshold on your cameras. Do not train from scratch.

## Equations

Triplet (FaceNet)

\[
L=\sum_i \max(\|f(A)-f(P)\|_2^2-\|f(A)-f(N)\|_2^2+\alpha,0)
\]

ArcFace target logit

\[
s\cos(\theta_y+m)
\]

Match score

\[
\cos(u,v)=u\cdot v \quad\text{for }\|u\|=\|v\|=1
\]

## Datasets

- Train (open) — Glint360K, cleaned MS1M variants, synthetic DigiFace-style sets.
- Rank — IJB-B/C, NIST FRTE 1-1 and 1-N.
- Dead as a leaderboard — LFW.

## Rules

- Historical public figures are in-bounds. No stalking, doxxing, or live-surveillance how-to.
- No fake numeric match scores.
- No ethics sermon unless asked. State demographic-gap existence if asked.
- Retry any research fetch with exp backoff 10/30/60s ±25% jitter and report the delay if it fired.

## Persistence

Local path `/home/workdir/.grok/skills/facial-recognition-explorer/`.
After a real edit, package only this skill and push to `Stijnman/grok-custom-skills` at `.grok/skills/facial-recognition-explorer/`.
