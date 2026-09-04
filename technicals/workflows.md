# Workflows

Every automation, what triggers it, and on which branch.

## The rule

**Everything that writes to R2 or mints a DOI runs on `main`, or on a branch by explicit human
choice. Nothing publishes from a push.**

| Workflow | Repository | Triggered by | Writes |
|:--|:--|:--|:--|
| `validate.yml` | `ihmr` | pull request, push to `main` | nothing |
| `sync-r2.yml` | `ihmr` | push to `main`, manual | R2 |
| `publish.yml` | `ihmr` | push to `submit-paper/**` (dry run), **manual** (real) | R2, Zenodo, a pull request |
| `sync-datasets.yml` | `ihmr-engine` | push to `main` touching `datasets/`, manual | R2 |
| `ci.yml` | `ihmr-engine`, `ihmr-web` | pull request, push to `main` | nothing |

## validate.yml

Three jobs, all of which fail the build rather than warn.

**Front matter and manifests.** Every document is checked against `schema/document.schema.json`,
and every manifest against `schema/manifest.schema.json` plus a check that the files it names
actually exist. A malformed document would otherwise break website ingestion silently, or render
as a broken page.

**Internal links.** Every relative link must resolve. Published paths get cited, and a dead link
inside the corpus is a small version of the same problem.

**House style.** No em dashes. The project uses hyphens, and a style rule that is not enforced is
a style rule that decays.

Runs on pull requests too, so nothing malformed can merge.

## sync-r2.yml

Mirrors the corpus into the bucket on every merge to `main`, then calls the site's ingestion
endpoint with the exact commit.

It uses `copy`, never `sync`. **A pipeline can never delete a published path**, because deleting
one would break citations, DOI landing pages, and every comment anchored to it. Withdrawing
something is a deliberate act, recorded, never a side effect of a pipeline run.

It also writes an immutable snapshot at `revisions/<commit>/`, which is what makes a citation to
a revision keep resolving.

## publish.yml

See [`publishing.md`](publishing.md). The short version: pushing to `submit-paper/**` runs a dry
run that mints nothing; minting requires a manual run with `dry_run` unticked.

## sync-datasets.yml

Mirrors `datasets/` and `visualizations/` from the engine into the bucket, and writes
`datasets/index.json` so the site can list them in one read rather than one per dataset.

**Fails** if any dataset has no `SOURCE.md`, because a dataset without provenance is not
evidence. **Warns** if a dataset has no named verifier, because the site already labels those and
blocking the sync would not make anyone read them sooner.

## What is not automated, on purpose

**Deployment.** The site is deployed by hand for now. Automatic deploys on merge are fine for
most projects; here, a merge can change what a published research article says, and that deserves
a person watching.

**Withdrawal.** Nothing removes a published path. If something genuinely must come down, it is
done deliberately and recorded, because a claim that quietly disappears is worse for a research
project than one that is openly retracted.

**Nothing runs on a schedule.** Which means if a sync fails, the bucket silently lags. A daily
reconciliation comparing `last-sync.json` against `main` would catch it, and does not exist yet.
