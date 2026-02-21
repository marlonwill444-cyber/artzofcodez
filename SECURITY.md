# Security Policy

## Credential Hygiene — Never Commit Secrets

API keys, tokens, and passwords **must never be committed to source code**.
All scripts in this repository load credentials exclusively from environment
variables:

| Variable | Used by |
| -------- | ------- |
| `LEONARDO_API_KEY` | `mdigitalartz_leonardo.py`, `mdigitalartz_leonardo.ts`, `generate_aether_core.py` |

Set the variable in your shell (or a local `.env` file that is listed in
`.gitignore`) before running any script:

```bash
export LEONARDO_API_KEY="<your-key>"
python mdigitalartz_leonardo.py
```

If you accidentally commit a key, **revoke it immediately** in the Leonardo
dashboard and generate a new one.

## Reporting a Vulnerability

Please open a **private** GitHub Security Advisory (use the
"Report a vulnerability" button on the Security tab) rather than filing a
public issue. You can expect an acknowledgement within 72 hours and a status
update within 7 days. If a vulnerability is confirmed, a fix will be issued as
soon as possible; if declined, a clear explanation will be provided.
