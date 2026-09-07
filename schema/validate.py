import json, pathlib, re, sys

root = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else ".")
schema = json.loads((root / "schema/document.schema.json").read_text())
props    = schema["properties"]
required = set(schema["required"])
enums    = {k: set(v["enum"]) for k, v in props.items() if "enum" in v}

def parse_fm(text):
    if not text.startswith("---"):
        return None
    try:
        end = text.index("\n---", 3)
    except ValueError:
        return None
    out, key = {}, None
    for line in text[4:end].split("\n"):
        if not line.strip():
            continue
        if line.startswith(("  - ", "- ")) and key is not None:
            out.setdefault(key, [])
            if isinstance(out[key], list):
                out[key].append(line.split("- ", 1)[1].strip())
            continue
        m = re.match(r"^([a-z_]+):\s*(.*)$", line)
        if m:
            key, val = m.group(1), m.group(2).strip()
            if val.startswith("[") and val.endswith("]"):
                out[key] = [x.strip() for x in val[1:-1].split(",") if x.strip()]
            elif val == "":
                out[key] = None
            else:
                out[key] = val
    return out

SKIP_NAMES = {"README.md", "AGENTS.md", "CLAUDE.md"}

# Not corpus documents. technicals/ explains how this repository is operated -
# how publishing works, what the branch rules are, where things land in R2 -
# which is the same kind of thing as README or CONTRIBUTING, not a research
# claim. Front matter carries a status and a publication state, and neither
# means anything for a document that is simply true of how the repo runs.
# engine/ is where the publish workflow checks out ihmr-engine, inside this
# working tree because Actions paths are relative to the workspace. It is a
# sibling repository, not part of the corpus, and its dataset files carry
# provenance headers rather than document front matter.
SKIP_DIRS = (".github/", "technicals/", "engine/")

problems, checked = [], 0

for f in sorted(root.rglob("*.md")):
    rel = f.relative_to(root).as_posix()
    if ".git/" in rel or rel.startswith(SKIP_DIRS) or f.name in SKIP_NAMES:
        continue
    # Build scratch. The PDF build writes _build.md and _charts/ into a version
    # folder and clears them afterwards; a failed or interrupted build leaves
    # them, and a leftover should not fail validation.
    if any(part.startswith("_") for part in rel.split("/")):
        continue
    fm = parse_fm(f.read_text())
    if fm is None:
        problems.append((rel, "no front matter")); continue
    checked += 1
    missing = required - set(fm)
    if missing:
        problems.append((rel, f"missing {sorted(missing)}"))
    for k, allowed in enums.items():
        val = fm.get(k)
        if val is not None and not isinstance(val, list) and val not in allowed:
            problems.append((rel, f"{k}={val!r} not permitted"))
    if fm.get("id") and not re.match(props["id"]["pattern"], str(fm["id"])):
        problems.append((rel, f"id {fm['id']} fails pattern"))
    if fm.get("type") == "page" and fm.get("status") not in ("current", "superseded"):
        problems.append((rel, f"page status {fm.get('status')!r} invalid"))

print(f"checked {checked} documents")
for rel, p in problems:
    print(f"  {rel}\n      {p}")
if not problems:
    print("all valid")
sys.exit(1 if problems else 0)
