# Branch protection

To be applied after the first push. `main` does not exist on the remote until then, and
protection cannot be set on a branch that is not there.

## Why this matters more here than in most repositories

Published paths get cited. A DOI landing page, a citation in someone else's paper, and every
comment on the website all point at a path in `main`. **Force-pushing or rewriting `main` breaks
things that are not ours to break.**

## Rules for `main`

```bash
gh api -X PUT repos/ihmrlabs/ihmr/branches/main/protection \
  --input .github/branch-protection.json
```

| Rule | Why |
|:--|:--|
| Require a pull request | Nothing lands unreviewed, including publications |
| Require status checks: `documents`, `links`, `prose` | A malformed document breaks website ingestion silently |
| Require branches to be up to date | Two publications merging out of order would produce a manifest that disagrees with itself |
| **Block force pushes** | Rewriting history breaks every existing citation |
| **Block deletions** | Self-explanatory |
| Apply to administrators | The person most likely to push to main at midnight is the maintainer |

## Rules for `submit-papers`

**Protected exactly like `main`**, and for a sharper reason: merging into it mints permanent
DOIs.

```bash
gh api -X PUT repos/ihmrlabs/ihmr/branches/submit-papers/protection \
  --input technicals/branch-protection.json
```

Same rules, same reasoning. Requiring a pull request means somebody reviews what is about to
become permanently citable, and blocking force pushes means the branch cannot be rewritten
underneath a run.

## What actually keeps this safe

Not the branch protection, useful though it is. **The idempotency.**

What publishes is decided by the state of the papers, not by the push that triggered the run. A
paper is eligible when it is signed off, has no DOI, and carries a publishable status. Once it
has a DOI it is never eligible again.

So re-running a failed job publishes nothing. Merging a stale branch publishes nothing. Pushing
twice publishes nothing. The only way to mint is to make a paper eligible, which means signing
it off, which is a deliberate act by a named person.

## The flow

```text
finish a paper, set signed_off_by
        ↓
open a pull request into submit-papers
        → dry run: lists exactly what merging would publish. Mints nothing.
        ↓
merge it
        → mints a DOI for every eligible paper
        → builds each PDF, with its DOI inside it
        → deposits to Zenodo, into the ihmr community
        → opens a pull request into main
        ↓
merge that
        → syncs to R2, re-ingests, goes live
```
