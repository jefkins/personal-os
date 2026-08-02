# Workflow: weekly update manager

**Objective:** Report available OS/package updates across the machines this OS
spans — report-only, the human runs the commands.

**Required inputs:** none. The gather script `07-scripts/core/update-check.py`
(the T in WAT) outputs JSON with update counts per host, per package manager.

**Runtime:** cron `Update Manager Weekly` (0 9 * * 0).

## Steps

1. Read the JSON. Group by host, then package manager.
2. Produce a concise report:

   ```
   🔄 Weekly Update Report — {date}

   **{host1}:** {summary or "all current ✅"}
   **{host2}:** {summary or "all current ✅"}

   ## Top Packages to Update
   | Package | Current → Latest |

   ## Suggested Commands
   - {host1}: `{command}` (or "none")
   - {host2}: `ssh {host2} '{command}'` (or "none")
   ```

3. Show the **top ~10** most important packages (security, major bumps, key
   tools) — not all 97.

## Update commands reference

- rpm-ostree: `rpm-ostree update`
- flatpak: `flatpak update`
- pip (shared venv): `uv pip install --python <shared-venv>/bin/python --upgrade <pkg>`
- npm: `npm --prefix ~/.npm update -g`

## Rules

1. DO NOT auto-update — report only, suggest commands, let the human run them.
2. Host offline → note it, skip.
3. Everything current → "All packages current across both machines ✅".
4. pip "not found" on a host → fine, skip pip for that host.
