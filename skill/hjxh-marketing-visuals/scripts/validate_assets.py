from __future__ import annotations

import json
import sys
from collections import Counter
from pathlib import Path


EXPECTED_COUNTS = {"logo": 6, "ip": 6, "product": 4, "font": 10}
ALLOWED_EXTENSIONS = {
    "logo": {".png"},
    "ip": {".png"},
    "product": {".png", ".jpg", ".jpeg"},
    "font": {".ttf", ".otf"},
}


def fail(message: str) -> None:
    raise ValueError(message)


def main() -> int:
    skill_dir = Path(__file__).resolve().parents[1]
    manifest_path = skill_dir / "assets" / "manifest.json"
    if not manifest_path.is_file():
        fail(f"Missing manifest: {manifest_path}")

    entries = json.loads(manifest_path.read_text(encoding="utf-8"))
    if not isinstance(entries, list):
        fail("Manifest root must be a list.")

    aliases: set[str] = set()
    counts: Counter[str] = Counter()
    for entry in entries:
        alias = entry.get("alias")
        category = entry.get("category")
        relative_path = entry.get("path")
        if not alias or alias in aliases:
            fail(f"Missing or duplicate alias: {alias!r}")
        aliases.add(alias)
        if category not in EXPECTED_COUNTS:
            fail(f"Invalid category for {alias}: {category!r}")
        if not relative_path or Path(relative_path).is_absolute():
            fail(f"Packaged path must be relative for {alias}: {relative_path!r}")
        asset_path = skill_dir / relative_path
        if not asset_path.is_file():
            fail(f"Missing asset for {alias}: {asset_path}")
        if asset_path.suffix.lower() not in ALLOWED_EXTENSIONS[category]:
            fail(f"Invalid extension for {alias}: {asset_path.suffix}")
        counts[category] += 1

    if dict(counts) != EXPECTED_COUNTS:
        fail(f"Category counts differ: expected {EXPECTED_COUNTS}, got {dict(counts)}")

    print(f"Validated {len(entries)} HJXH assets.")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"Asset validation failed: {exc}", file=sys.stderr)
        raise SystemExit(1)

