# Copilot Instructions for ArtzOfCodez

## Repository Overview

This repository generates Bio-Armor artwork using Leonardo AI. It contains Python and TypeScript scripts for API integration and a comprehensive style guide.

**Key docs:**
- `PROJECT_VISUALFORGE_GUIDE.md` — Complete style bible, QA checklist, and production guidelines
- `SECURITY.md` — Security policy and vulnerability reporting

## Security Rules (CRITICAL)

### Never Commit Secrets
- **NEVER** hardcode API keys, tokens, or credentials in code
- **ALWAYS** use environment variables for secrets (e.g., `LEONARDO_API_KEY`)
- **EXISTING ISSUE**: Current scripts contain hardcoded API keys — these MUST be rotated and removed in any PR that touches them

### If You Find Secrets
If secrets appear in diffs, history, or code you're modifying:
1. **Stop** — do not commit
2. **Rotate** the compromised key immediately via Leonardo dashboard
3. Refactor to use environment variables: `os.environ.get("LEONARDO_API_KEY")`
4. Document the rotation in your PR

### Environment Variable Pattern
```python
# Python
import os
API_KEY = os.environ.get("LEONARDO_API_KEY")
if not API_KEY:
    raise ValueError("LEONARDO_API_KEY environment variable not set")
```

```typescript
// TypeScript
const API_KEY = process.env.LEONARDO_API_KEY;
if (!API_KEY) {
  throw new Error("LEONARDO_API_KEY environment variable not set");
}
```

## Running Existing Scripts

### Python Scripts
The repository has Python scripts using `requests` library:

```bash
# Install dependencies (if needed)
pip install requests

# Run Leonardo API helper
python mdigitalartz_leonardo.py

# Run Aether Core generator
python generate_aether_core.py
```

**Note:** These scripts require internet access and a valid `LEONARDO_API_KEY` environment variable.

### TypeScript Scripts
TypeScript files are present but toolchain may not be configured:

```bash
# ASSUMPTION: If Node.js/npm are set up, you would run:
npm install axios  # Install dependencies
npx ts-node mdigitalartz_leonardo.ts  # Execute TypeScript

# Or compile first:
npx tsc mdigitalartz_leonardo.ts
node mdigitalartz_leonardo.js
```

**If no `package.json` exists**, these commands are assumptions. Do not invent build tooling without confirming project needs.

## Code Quality Standards

### Follow the Style Guide
- Review `PROJECT_VISUALFORGE_GUIDE.md` before making art-generation changes
- Maintain consistency with existing palette locks and QA metrics
- Adhere to "Do/Don't" sections for linework and shading

### PR Discipline
- **Keep PRs small**: One logical change per PR
- **No drive-by formatting**: Don't reformat unrelated code
- **No refactors in feature PRs**: Separate structural changes from features
- **Descriptive commits**: Explain what and why, not just what

## Definition of Done

Before marking any work complete, verify:

- [ ] **Functionality**: Changes work as intended; tested locally
- [ ] **Security**: No secrets committed; env vars used for API keys
- [ ] **Tests**: If test infrastructure exists, relevant tests pass
- [ ] **Documentation**: Updated if behavior/API changes
- [ ] **Style**: Follows existing code conventions
- [ ] **Review**: Code review comments addressed
- [ ] **Clean**: No debugging code, commented-out code, or temp files
- [ ] **Minimal**: Smallest possible change to achieve the goal

## Style Guide Reference

For art generation work, consult `PROJECT_VISUALFORGE_GUIDE.md` for:
- Neon Spectral palette locks (Charcoal, Graphite, Neon Teal, Electric Indigo, Solar Magenta)
- Cel-shading rules (two-value shading, hard-edged cuts)
- QA scoring thresholds (≥4 in every metric, total ≥16)
- Hard reject failure modes (muddy midtones, rounded anatomy, pillow shading)

## Contributing Workflow

1. **Read** relevant docs (this file, PROJECT_VISUALFORGE_GUIDE.md, SECURITY.md)
2. **Plan** your change — understand existing code first
3. **Implement** minimal, surgical changes
4. **Test** locally with actual API calls (if applicable)
5. **Review** your own diff — does it add unintended changes?
6. **Submit PR** using template (see `.github/pull_request_template.md`)
7. **Address feedback** promptly and completely

## Questions?

- Art style questions → `PROJECT_VISUALFORGE_GUIDE.md`
- Security questions → `SECURITY.md`
- API integration → Comments in `mdigitalartz_leonardo.py` or `.ts`
