# Project: MDigitalArtz VisualForge — Bio-Armor Series

*Citation note: Tags like `[cite: ###]` are stakeholder reference anchors kept for traceability; no external docs are required to use this guide.*

## 1) Style Bible — Do / Don’t

**Linework**
- **Do:** Use firm outer contours (thicker at shadow turns), crisp inner mechanical seams, and knife-edge highlights to separate armor plates.
- **Don’t:** Feathered or sketchy strokes; blurry edges; wobble in ellipses or foreshortened limbs.

**Cel-Shading Logic**
- **Do:** Two-value shading per plane (key + shadow), hard-edged cuts, minimal bounce light; rim-light is a separate band, not a gradient.
- **Don’t:** Airbrush gradients, noise overlays, soft glow mush; avoid uncontrolled ambient fill that muddies forms.

**Neon Spectral Palette Locks** [cite: 175, 239]
- Base armor neutrals: Charcoal #111418, Graphite #1c1f27.
- Primary glow: Neon Teal #00f6ff; Secondary: Electric Indigo #6a4bff; Accent slash: Solar Magenta #ff2cfb.
- Metal hits: Titanium #8b9fb6; Warm brake lights: Ember #ff5c39 (sparingly).
- **Lock rules:** One dominant glow channel per piece; never mix warm and cool glows on the same rim; reserve magenta for focal glyphs only.

**Do / Don’t Quicklist**
- **Do:** Adult heroic proportions; angular silhouettes; negative-space vents; asym pose for dynamism; material separation via value, not texture.
- **Don’t:** Rounded “bubble” armor; toddler/dwarf proportions; rainbow gradients; lens flares; text/logos; soft plush folds.

**Hard Reject Failure Modes** [cite: 287, 296]
- Muddy midtones or gray fog that collapses contrast.
- Rounded anatomy or “chibi/dwarf” body scale.
- Pillow shading or airbrushed gradients.
- Over-noise, JPG artifacts, or smear/glow halos.
- Off-model palette (pink/rainbow, mixed warm-cool rims).
- Missing silhouette read at thumbnail (head/shoulder/weapons merging).

## 2) Batch Production — Collection Drop (8 Designs)
- **Naming convention:** `SERIES01_CHAR01_VARIANT01` … `SERIES01_CHAR08_VARIANT01` (series ↔ character slot ↔ variant). For alternate colorways, increment VARIANT.
- **Product title template:** `Bio-Armor [Series Code] — [Callsign] // [Signature Mechanism]` (e.g., “Bio-Armor S01 — Asterion // Photon Rampart”).
- **Lore blurb structure (short, copyright-safe)** [cite: 352]:
  1. Sentence 1: Origin hint + role (“Forged in orbital dry docks, designed as vanguard tank.”).
  2. Sentence 2: Capability hook + palette callout (“Neon teal conduits channel shock-lances; magenta sigils appear only at full charge.”).
  3. Sentence 3 (optional): Limiter/quirk for personality without trademarked IP (“Cannot deploy in vacuum longer than 11 minutes without coolant purge.”).
- **Consistency tactics:** Shared skeletal rig and camera distance; lock seed for pose family; reuse silhouette anchors (pauldrons/helm crest) per slot; change only one hero motif per variant (weapon or crest), not both.

## 3) Quality Control — Hard QA Checklist + Scoring (0–5)
Score each dimension 0–5 (0 = fail/absent, 3 = shippable, 5 = exemplary). Pass requires **≥4** in every metric and **total ≥16** (gold standard: 18–20). [cite: 348]

| Metric | 0–1 | 2 | 3 (baseline) | 4 | 5 |
| --- | --- | --- | --- | --- | --- |
| Silhouette Readability | Merged forms; head/weapon lost at 64px | Major tangents | Clear head/torso/weapon split | Strong negative space; weapon readable | Iconic, instantly legible at 32px |
| Anatomical Correctness (adult/hourglass) | Chibi/dwarf, bent proportions | Limb length off >15% | Adult scale; joints aligned | Heroic taper; foreshortening clean | Dynamic heroic stance with convincing weight |
| Style Consistency | Mixed render styles | Minor mixed edges | Uniform cel cuts; consistent line weight | Palette + line + materials locked | Feels from one hand; perfect rhythm of edges |
| Cleanliness | Smears/halos/noise | Minor artifacting | Edges closed; no pillow shading | Micro-clean plates; no stray pixels | Surgical lines; print-ready on flat color |

**Hard QA Checklist (fail any = reject)**
- Palette adheres to Neon Spectral lock (no unauthorized hues).
- Line weight hierarchy present (outer > inner) and edges closed.
- Two-value cel shading; rim light band separated, no soft airbrush.
- Silhouette readable at 64px; head/torso/weapon separation visible.
- Anatomy adult-scale; no disproportionate scaling (dwarfism/chibi); joints/foreshortening plausible.
- No text, logos, watermarks, or copyrighted motifs.
- No noise, smear, or compression artifacts on glow edges.

## Expert Notes (Advanced Execution)
- Block silhouettes first in pure black at 64px, then light-map with two-value cel; only after that apply palette locks to prevent midtone drift.
- Use dual-pass prompting: pass 1 for pose + silhouette seed; pass 2 for material separation with control over rim channels; keep seed fixed for character slots.
- Deploy rim light on the shadow side only; constrain to 10–15% width of limb/plate to avoid glow bloat.
- For variations, change one design axis at a time (crest, weapon, or visor pattern) while freezing camera FOV and limb spread to keep set cohesion.

## Enhanced AI Instructions (1%-Expert Specialist Workflow)
- Hold response mode: if the user says they are sending multiple voice notes, only return: **"Acknowledged. I will wait for 'Proceed' before giving the full response."**
- On **Proceed**, remove redundant content and correct grammar in the user's provided notes, then provide **3 improved prompt versions** with **negative prompts**.
- Use this structure in every full response:
  1. What information is missing + ask 2–3 direct clarifying questions.
  2. Main answer scoped to the project only, citing this file section used.
  3. Reasoning + evidence per main point, with explicit assumptions.
  4. Missing angles + opposite-view considerations + expert questions.
  5. AI self-rating with individual 1–10 scores for accuracy, completeness, relevance, clarity, and usefulness; for any item below 8, explain the gap and provide a revised answer section that fixes it.
  6. Quality check: format match, supported claims, concrete action steps.
- Always end with a **1%-Expert Specialist follow-up prompt** and include a **negative prompt** to reduce drift/noise.

**Copy/paste template prompts (with negatives):**
1. **Voice-note gated expert mode**
   - Prompt: "I am going to send multiple voice notes. Do not provide a full answer until I say 'Proceed'. When I say 'Proceed', first clean fluff and fix grammar, then give 3 upgraded prompt options with project-scoped expert analysis, explicit assumptions, missing-angle review, and self-rating."
   - Negative: "Do not answer early, do not invent facts, do not go out of project scope, do not omit citations to file sections used."
2. **Project-file-first specialist mode**
   - Prompt: "Respond as a top 1% [role] for [project goal]. Use project files as source of truth first; cite file name + section used. Ask up to 3 clarifying questions if key info is missing. Provide concise, actionable output for [audience] in [format]."
   - Negative: "No generic advice without evidence, no unsupported claims, no irrelevant background, no missing assumptions list."
3. **100x deeper analysis mode**
   - Prompt: "Run 100x deeper analysis: reasoning and evidence for each conclusion, what I left out, opposite-view critique, advanced expert strategies, and a quality-scored revision loop for any score under 8."
   - Negative: "No shallow summaries, no skipped trade-offs, no unclear next steps, no format drift."

## Appendix — Stakeholder Directives & Compliance
- **Citation map:**  
  - [cite: 175, 239] Neon Spectral palette lock requirement.  
  - [cite: 287, 296] Hard reject failure modes.  
  - [cite: 352] Lore blurb structure constraint.  
  - [cite: 348] QA scoring metrics and thresholds.
