#!/usr/bin/env python3
"""Validate every SKILL.md so a malformed file never ships.

Catches the class of bug that hides skills from `npx skills` and plugin
loaders — most importantly frontmatter that a strict YAML parser rejects
(e.g. an unquoted colon-space in a description). Run locally with:

    python3 scripts/validate-skills.py

Exits non-zero (and lists every problem) if anything fails.
"""

from __future__ import annotations

import glob
import re
import sys

try:
    import yaml
except ImportError:
    sys.exit("PyYAML is required: pip install pyyaml")

REQUIRED_TOP = ("name", "description", "license")
NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
# {discipline}/{category}/{skill-name}/SKILL.md
PATH_RE = re.compile(r"^(ux|pm)/[a-z0-9-]+/[a-z0-9-]+/SKILL\.md$")


def split_frontmatter(text: str):
    """Return the YAML frontmatter block, or None if absent/unterminated."""
    if not text.startswith("---"):
        return None
    parts = text.split("---", 2)
    if len(parts) < 3:
        return None
    return parts[1]


def validate(path: str) -> list[str]:
    errors: list[str] = []
    with open(path, encoding="utf-8") as fh:
        text = fh.read()

    if not PATH_RE.match(path):
        errors.append("path is not {discipline}/{category}/{skill-name}/SKILL.md")

    fm = split_frontmatter(text)
    if fm is None:
        errors.append("missing or unterminated YAML frontmatter (--- ... ---)")
        return errors

    try:
        data = yaml.safe_load(fm)
    except yaml.YAMLError as exc:
        # This is what a strict loader (and npx skills) trips on.
        detail = str(exc).replace("\n", " ")
        errors.append(f"frontmatter is not valid YAML — {detail}")
        return errors

    if not isinstance(data, dict):
        errors.append("frontmatter did not parse to a mapping")
        return errors

    for key in REQUIRED_TOP:
        if not data.get(key):
            errors.append(f"missing required field: {key}")

    name = data.get("name")
    if isinstance(name, str) and not NAME_RE.match(name):
        errors.append(f"name '{name}' is not kebab-case")

    desc = data.get("description")
    if isinstance(desc, str) and len(desc.strip()) < 20:
        errors.append("description is suspiciously short (<20 chars)")

    meta = data.get("metadata")
    if not isinstance(meta, dict):
        errors.append("missing metadata block")
    else:
        if not meta.get("author"):
            errors.append("missing metadata.author")
        if not meta.get("version"):
            errors.append("missing metadata.version")

    return errors


def main() -> int:
    files = sorted(glob.glob("ux/**/SKILL.md", recursive=True) +
                   glob.glob("pm/**/SKILL.md", recursive=True))
    if not files:
        print("No SKILL.md files found — run from the repo root.", file=sys.stderr)
        return 1

    names: dict[str, str] = {}
    total_errors = 0
    for path in files:
        errs = validate(path)
        # Cross-file: duplicate names break discovery (one shadows the other).
        try:
            fm = split_frontmatter(open(path, encoding="utf-8").read())
            data = yaml.safe_load(fm) if fm else None
            if isinstance(data, dict) and isinstance(data.get("name"), str):
                nm = data["name"]
                if nm in names:
                    errs.append(f"duplicate name '{nm}' (also in {names[nm]})")
                else:
                    names[nm] = path
        except yaml.YAMLError:
            pass

        if errs:
            total_errors += len(errs)
            print(f"\n✗ {path}")
            for e in errs:
                print(f"    - {e}")

    print()
    if total_errors:
        print(f"FAILED: {total_errors} problem(s) across {len(files)} skills.")
        return 1
    print(f"OK: {len(files)} skills validated, all frontmatter clean.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
