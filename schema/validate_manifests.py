"""Validate every manifest.json in research/ and essays/, and check that the files
it points at actually exist. A manifest that references a missing document would
render as a broken page rather than failing loudly, so it fails here."""
import json, pathlib, sys

root = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else ".")
schema_path = root / "schema/manifest.schema.json"
schema = json.loads(schema_path.read_text())
required = set(schema["required"])

problems, checked = [], 0

for folder in ["research", "essays"]:
    base = root / folder
    if not base.exists():
        continue
    for work in sorted(p for p in base.iterdir() if p.is_dir()):
        mf = work / "manifest.json"
        if not mf.exists():
            problems.append(f"{work.relative_to(root)}: no manifest.json")
            continue
        checked += 1
        try:
            m = json.loads(mf.read_text())
        except json.JSONDecodeError as e:
            problems.append(f"{mf.relative_to(root)}: invalid JSON, {e}")
            continue

        missing = required - set(m)
        if missing:
            problems.append(f"{mf.relative_to(root)}: missing {sorted(missing)}")
            continue

        # The folder name should carry the id and slug, so URLs stay predictable.
        expected = f"{m['id']}-{m['slug']}"
        if work.name != expected:
            problems.append(f"{work.relative_to(root)}: folder should be named {expected}")

        seen = set()
        for v in m["versions"]:
            n = v["version"]
            if n in seen:
                problems.append(f"{mf.relative_to(root)}: version {n} listed twice")
            seen.add(n)
            vdir = work / f"v{n}"
            if not vdir.exists():
                problems.append(f"{mf.relative_to(root)}: v{n} declared but folder missing")
                continue
            for key in ("document", "pdf", "visualisations", "dashboard"):
                rel = v.get(key) or (m.get("render", {}) or {}).get(key)
                if key in ("document", "pdf") and v.get(key) and not (vdir / v[key]).exists():
                    problems.append(f"{mf.relative_to(root)}: v{n} {key} not found: {v[key]}")

        if m["currentVersion"] not in seen:
            problems.append(f"{mf.relative_to(root)}: currentVersion {m['currentVersion']} is not a listed version")

        # Published versions must never be edited, so every version below the
        # current one needs a note saying what changed.
        for v in m["versions"]:
            if v["version"] > 1 and not v.get("changed"):
                problems.append(f"{mf.relative_to(root)}: v{v['version']} does not say what changed")

print(f"checked {checked} manifests")
for p in problems:
    print(f"  {p}")
if not problems:
    print("all valid")
sys.exit(1 if problems else 0)
