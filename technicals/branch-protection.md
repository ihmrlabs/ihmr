# Branch protection

Both public repositories use **rulesets** rather than classic branch protection.

## Why rulesets

Three reasons, and the second one is the one that mattered.

**They match names, not branches.** Classic protection can only be attached to a branch that
already exists, which left a real hole: until somebody created `submit-papers`, there was nothing
to protect, so anyone with write access could create it and push. A ruleset matches the name, so
the branch is protected before it exists.

**They can be paused and resumed without being destroyed.** Lifting protection for an initial
import is `enforcement: disabled` and then `active` again. With classic protection you delete the
configuration and rebuild it from memory, which is exactly when a rule quietly goes missing.

**They are auditable in one place.** `gh api repos/ihmrlabs/<repo>/rulesets` lists everything.

## What is protected

| Repository | Ruleset | State |
|:--|:--|:--|
| `ihmr` | `main` | active |
| `ihmr` | `submit-papers` | active |
| `ihmr-engine` | `main` | **disabled** until the first push creates the branch |

Private repositories are not protected. Branch protection there needs a paid plan, and it is not
worth it for the website or the internal notes.

## The rules

| Rule | Why |
|:--|:--|
| Pull request required | Nothing lands unreviewed, including publications |
| Status checks: `Front matter and manifests`, `Internal links`, `House style` | A malformed document breaks website ingestion silently |
| Strict checks | Two merges out of order would produce a manifest that disagrees with itself |
| No force pushes | Rewriting history breaks every existing citation |
| No deletions | Self-explanatory |
| Linear history | A published path should have one traceable line to it |
| No bypass actors | The person most likely to push to main at midnight is the maintainer |

## Why `submit-papers` is protected at all

Merging into it mints permanent DOIs. That is a sharper reason than `main` has.

Note though that the protection is not what makes publishing safe. **The idempotency is.** What
publishes is decided by the state of the papers, not by the push: a paper is eligible only when it
is signed off and has no DOI yet. Once it has one it is never eligible again, so a stray push
mints nothing. See [publishing.md](publishing.md).

The ruleset is the second lock, not the first.

## Turning enforcement off and on

For an initial import, when there is nothing published to protect:

```bash
# pause
gh api -X PUT repos/ihmrlabs/ihmr/rulesets/22258221 -f enforcement=disabled

# push

# resume, immediately
gh api -X PUT repos/ihmrlabs/ihmr/rulesets/22258221 -f enforcement=active
```

Do it in one sitting. A ruleset left disabled is worse than one that was never created, because
it looks protected in a list.

## Activating the engine ruleset

After `ihmr-engine` has its first push and a `main` branch exists:

```bash
gh api -X PUT repos/ihmrlabs/ihmr-engine/rulesets/22258070 -f enforcement=active
```
