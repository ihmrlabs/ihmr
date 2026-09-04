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

## Publication branches

`submit-paper/**` is deliberately **not** protected. It is a working branch: push to it as often
as you like, and every push runs a dry run that mints nothing.

The protection that matters is not on that branch. It is that **minting requires a manual run
with `dry_run` unticked**, so no push, rebase or rerun can ever create a permanent DOI by
accident.

## The flow

```text
git checkout -b submit-paper/IHMR-RSCH-001-state-of-indias-healthcare-v1
git push                          → dry run, mints nothing, tells you what would happen
                                  → repeat until clean
Actions → Publish → dry_run off   → mints the DOI, builds the PDF, opens a PR
merge the PR                      → lands on main, having been reviewed
```

Nothing is minted at merge, because it already happened on the branch. Merging is just merging.
