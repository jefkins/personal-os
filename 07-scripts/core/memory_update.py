"""
memory_update.py — append a structured entry to a memory file.
Enforces the standard format: ## [YYYY-MM-DD] — Title

Usage:
    python 07-scripts/core/memory_update.py decisions_log "Chose X over Y" "Because..."
    python 07-scripts/core/memory_update.py lessons_learned "API rate limits" "Batch the calls."
"""

import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MEMORY = ROOT / "12-memory"
VALID = {p.stem for p in MEMORY.glob("*.md")}

def main():
    if len(sys.argv) < 4:
        sys.exit(f"Usage: memory_update.py <file> <title> <content>\nFiles: {', '.join(sorted(VALID))}")
    name, title, content = sys.argv[1], sys.argv[2], " ".join(sys.argv[3:])
    if name not in VALID:
        sys.exit(f"Unknown memory file '{name}'. Options: {', '.join(sorted(VALID))}")
    path = MEMORY / f"{name}.md"
    entry = f"\n## [{date.today().isoformat()}] — {title}\n{content}\n"
    with open(path, "a", encoding="utf-8") as f:
        f.write(entry)
    print(f"Appended to {path.relative_to(ROOT)}:")
    print(entry)

if __name__ == "__main__":
    main()
