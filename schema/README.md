# Schema

Every document in this repository starts with a small block of information about itself, and
[`document.schema.json`](document.schema.json) is the machine-readable definition of it.

Our checks validate every document against this on each pull request, so a document that would
break the website cannot quietly get merged. If something is missing or malformed, the error
will tell you plainly what and where.

**If wrestling with this is putting you off contributing, please do not let it.** Send us the
text and we will handle the metadata.

## What the fields do

| Field | Why it exists |
|---|---|
| `id` | Permanent identifier. Survives renames, moves, and supersession - it is what people cite |
| `type` | Which kind of document this is |
| `status` | How sure we are. See the table in the main README |
| `created` / `updated` | Health policy moves; dates matter |
| `authors` | People. Never AI tools |
| `topics` / `related` | How the corpus connects to itself |
| `supersedes` / `superseded_by` | The trail when we change our minds |
| `ai_disclosure` | How AI was used. Required - see [AI_USE_POLICY.md](https://projectihmr.org/about/how-we-use-ai) |
| `signed_off_by` | The person who checked the claims and takes responsibility |
| `clinical_review_by` | Required for clinical claims |
| `sources` | Paths into `sources/`, so a claim resolves to the thing it came from |
| `doi` | Minted for research and essays once they reach `evidence` or `decision`. See below |
| `lang` | Currently always `en` |

## Two kinds of document

**Research documents** - research, essays, questions, RFCs, decisions, experiments, architecture
- carry an epistemic `status`: how much weight we put behind the claim.

**Pages** - governance, privacy, the glossary, and so on - carry `status: current` or
`superseded` instead. A privacy policy has versions, but it does not have epistemic weight, and
labelling one a `hypothesis` would be nonsense.

## DOIs

Research articles and essays get a DOI once they reach `evidence` or `decision`, so they can be
cited formally. The schema requires it at those statuses.

Questions, RFCs, decisions and pages do not. They are living documents, and minting a permanent
identifier for something designed to keep changing would mislead whoever cited it.

## Two rules worth knowing

**Validation runs in CI.** `schema/validate.py` checks every document on each pull request, so
a malformed one cannot merge and break the website quietly.

**IDs are permanent.** Once a document is published, its ID is cited and its path is linked.
Renaming or renumbering breaks citations, breaks the provenance chain, and breaks every comment
anchored to it.

**`status` here is not a workflow state.** It says how much epistemic weight the project puts
behind a claim - not how far along it is. A document can be finished and still be a
`hypothesis`.
