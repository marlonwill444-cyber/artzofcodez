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
  1. Sentence 1: Origin hint + role (“Forged in orbital drydocks, designed as vanguard tank.”).
  2. Sentence 2: Capability hook + palette callout (“Neon teal conduits channel shock-lances; magenta sigils appear only at full charge.”).
  3. Sentence 3 (optional): Limiter/quirk for personality without trademarked IP (“Cannot deploy in vacuum longer than 11 minutes without coolant purge.”).
- **Consistency tactics:** Shared skeletal rig and camera distance; lock seed for pose family; reuse silhouette anchors (pauldrons/helm crest) per slot; change only one hero motif per variant (weapon or crest), not both.

## 3) Quality Control — Hard QA Checklist + Scoring (0–5)
Score each dimension 0–5 (0 = fail/absent, 3 = shippable, 5 = exemplary). Pass requires **≥4** in every metric and **total ≥18**. [cite: 348]

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
- Anatomy adult-scale; no dwarfing; joints/foreshortening plausible.
- No text, logos, watermarks, or copyrighted motifs.
- No noise, smear, or compression artifacts on glow edges.

## Expert Notes (Advanced Execution)
- Block silhouettes first in pure black at 64px, then light-map with two-value cel; only after that apply palette locks to prevent midtone drift.
- Use dual-pass prompting: pass 1 for pose + silhouette seed; pass 2 for material separation with control over rim channels; keep seed fixed for character slots.
- Deploy rim light on the shadow side only; constrain to 10–15% width of limb/plate to avoid glow bloat.
- For variations, change one design axis at a time (crest, weapon, or visor pattern) while freezing camera FOV and limb spread to keep set cohesion.

## Self-Rating (included per deep-analysis requirement)
- **Score:** 9.5 / 10 for accuracy, completeness, and utility.
- **Rationale:** Provides actionable Do/Don’t rules, palette locks, batch naming, lore template, and QA rubric with pass thresholds. Would reach 10/10 with live exemplars and visual swatches, which are out of scope here.
