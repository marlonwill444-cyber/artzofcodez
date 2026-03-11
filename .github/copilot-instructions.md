# GitHub Copilot Instructions

## Project Overview
This repository contains helper scripts for generating images using the Leonardo AI Production API. The project supports the MDigitalArtz VisualForge Bio-Armor series, which follows strict design guidelines for creating cel-shaded, neon-spectral armor character art.

## Repository Structure
- `mdigitalartz_leonardo.py`: Python implementation of Leonardo API wrapper
- `mdigitalartz_leonardo.ts`: TypeScript implementation of Leonardo API wrapper
- `generate_aether_core.py`: Character-specific image generation script
- `PROJECT_VISUALFORGE_GUIDE.md`: Detailed style bible and quality control guidelines for the Bio-Armor series

## Code Style Guidelines

### Python
- Follow PEP 8 style guide
- Use type hints for function parameters and return types
- Include docstrings for all functions using the existing format (`:param` and `:return` style)
- Keep functions modular and focused on single responsibilities

### TypeScript
- Use strict TypeScript mode
- Export functions that may be used by other modules
- Use async/await for API calls
- Follow existing naming conventions (camelCase for functions/variables, UPPER_CASE for constants)

## Security Best Practices

### API Key Management
- **CRITICAL**: Never commit real API keys to the repository
- API keys in the code are placeholders and should be replaced with environment variables in production
- When modifying code, always suggest using `os.environ` (Python) or `process.env` (TypeScript) for sensitive credentials
- Add comments reminding users to keep API keys secret

### Dependencies
- Use `requests` library for Python HTTP calls
- Use `axios` library for TypeScript/Node.js HTTP calls
- No additional dependencies should be added without consideration of security implications

## VisualForge Design Standards
When working with image generation prompts or quality control:
- Reference `PROJECT_VISUALFORGE_GUIDE.md` for complete design requirements
- Follow the Neon Spectral palette locks (Neon Teal, Electric Indigo, Solar Magenta)
- Ensure prompts enforce cel-shading style with hard-edged cuts, no airbrush gradients
- Validate all designs meet the QA checklist with scores ≥4 in all metrics

## Workflow Guidelines

### Before Making Changes
- Understand the purpose of both Python and TypeScript implementations
- Ensure changes are synchronized between both language implementations when applicable
- Consider backward compatibility with existing API calls

### Testing
- These scripts require network access to interact with the Leonardo API
- When testing locally, ensure you have valid API credentials and network connectivity
- In environments without network access, focus on code correctness, type safety, and API structure validation
- Document expected API responses in comments for offline verification

### Documentation
- Update docstrings/JSDoc comments when modifying function signatures
- Keep inline comments concise and focused on non-obvious logic
- Reference external Leonardo API documentation when relevant

## Common Tasks

### Adding New API Endpoints
1. Add the function to both Python and TypeScript implementations
2. Use consistent naming across both languages (snake_case in Python, camelCase in TypeScript)
3. Include proper type hints/TypeScript types
4. Add comprehensive docstrings/JSDoc comments
5. Follow existing patterns for headers, error handling, and response parsing

### Modifying Image Generation Parameters
1. Check both `generate_images_phoenix()` and `generate_images_anime_xl()` functions
2. Update default values consistently
3. Update docstrings with new parameter descriptions
4. Ensure parameters align with Leonardo API documentation

### Working with Style Guide
- The `PROJECT_VISUALFORGE_GUIDE.md` contains critical design constraints
- Do not modify the style guide without explicit instruction
- When generating prompts, incorporate the style requirements (cel-shading, palette locks, anatomy rules)

## Notes
- This repository is designed to be used in environments with network access
- Scripts are intended as helper utilities, not production-ready services
- Keep code simple and maintainable for users who may be learning the Leonardo API
