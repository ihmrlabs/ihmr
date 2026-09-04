#!/usr/bin/env python3
"""
Which papers are ready to publish.

Eligibility is a property of the papers, not of the push that triggered the run.
That is what makes the whole thing safe to re-run: a paper that already has a
DOI is never eligible again, so pushing twice, re-running a failed job, or
merging a stale branch publishes nothing.

A paper is eligible when all three hold:

  1. It is signed off.      signed_off_by is set in the version front matter.
  2. It has no DOI.         the manifest records none for that version.
  3. It is publishable.     status is evidence or decision, not hypothesis.

Rule 1 is the one that matters most. A DOI is permanent, and attaching one to
research nobody has verified would make an unchecked claim permanently citable.

    python3 schema/eligible_for_publication.py .            # human readable
    python3 schema/eligible_for_publication.py . --json     # for a workflow matrix
"""
import json
import pathlib
import re
import sys

PUBLISHABLE_STATUSES = {"evidence", "decision"}


def front_matter(text: str) -> dict:
    if not text.startswith("---"):
        return {}
    try:
        end = text.index("\n---", 3)
    except ValueError:
        return {}
    out = {}
    for line in text[4:end].split("\n"):
        if ":" in line and not line.startswith((" ", "-", "\t")):
            k, _, v = line.partition(":")
            out[k.strip()] = v.strip()
    return out


def scan(root: pathlib.Path):
    eligible, skipped = [], []

    for folder, kind in (("research", "research"), ("essays", "essay")):
        base = root / folder
        if not base.exists():
            continue

        for work in sorted(p for p in base.iterdir() if p.is_dir()):
            mf = work / "manifest.json"
            if not mf.exists():
                continue
            try:
                manifest = json.loads(mf.read_text())
            except json.JSONDecodeError:
                skipped.append((work.name, None, "manifest is not valid JSON"))
                continue

            for entry in manifest.get("versions", []):
                version = entry["version"]
                label = f"{work.name} v{version}"
                vdir = work / f"v{version}"

                doc = vdir / entry.get("document", "")
                if not doc.exists():
                    skipped.append((work.name, version, "document not found"))
                    continue

                if entry.get("doi"):
                    skipped.append((work.name, version, f"already published, {entry['doi']}"))
                    continue

                status = entry.get("status", "")
                if status not in PUBLISHABLE_STATUSES:
                    skipped.append((work.name, version, f"status is {status or 'unset'}, not publishable"))
                    continue

                fm = front_matter(doc.read_text())
                signer = (fm.get("signed_off_by") or "").strip()
                if not signer:
                    skipped.append((work.name, version, "not signed off"))
                    continue

                eligible.append({
                    "work": work.name,
                    "version": version,
                    "kind": kind,
                    "folder": folder,
                    "title": manifest.get("title", work.name),
                    "signedOffBy": signer,
                    "status": status,
                })

    return eligible, skipped


def main() -> int:
    root = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else ".")
    as_json = "--json" in sys.argv

    eligible, skipped = scan(root)

    if as_json:
        print(json.dumps({"count": len(eligible), "papers": eligible}))
        return 0

    if eligible:
        print(f"{len(eligible)} ready to publish:\n")
        for p in eligible:
            print(f"  {p['work']} v{p['version']}")
            print(f"    {p['title']}")
            print(f"    signed off by {p['signedOffBy']}, status {p['status']}\n")
    else:
        print("Nothing is ready to publish.\n")

    if skipped:
        print(f"Not eligible ({len(skipped)}):\n")
        for work, version, why in skipped:
            v = f" v{version}" if version is not None else ""
            print(f"  {work}{v}: {why}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
