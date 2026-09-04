# Publishing a research version

How a finished piece of research becomes a citable artefact with a DOI.

The whole design turns on one asymmetry: **a DOI is permanent and cannot be deleted.** Every
other action in this repository is repeatable. A bad merge can be reverted, a broken render can
be re-run, a wrong figure can be corrected in a new version. A minted DOI is forever.

So publishing is deliberately the hardest thing to do here, and everything below follows from
that.

---

## The flow

```text
git checkout -b submit-paper/IHMR-RSCH-001-state-of-indias-healthcare-v1
git push
        ↓
   DRY RUN, on every push
   validates the corpus, checks the signature, confirms no DOI exists yet,
   builds the PDF, reports what would happen
   MINTS NOTHING
        ↓
   repeat until clean. push as often as you like.
        ↓
Actions → Publish a research version → run from this branch, dry_run UNTICKED
        ↓
   reserve the DOI
   write it into the article and the manifest
   rebuild the PDF, so it carries its own identifier
   deposit both to Zenodo, into the ihmr community
   open a pull request into main
        ↓
   merge the pull request
   nothing is minted at merge. it already happened.
```

## Why a push cannot publish

The obvious design is that pushing to a publication branch publishes. It is wrong here, and the
reason is worth stating because it is not obvious.

**A push is the easiest thing in git to do by accident.** An amend and force push, a stale branch
someone pushes to, a re-run of a failed job, a rebase onto a moved main. With push-to-publish,
`git push --force` becomes an irreversible act, which is a terrible property for a command people
use casually.

So the branch is still the unit of work and the record of intent. Only the irreversible step
needs a person to choose it, on a branch that has already proved it would work.

## Branch naming

```text
submit-paper/<work-folder>-v<version>
submit-paper/IHMR-RSCH-001-state-of-indias-healthcare-v1
```

The workflow parses the work and the version out of the branch name, so nobody types them twice
and the two cannot disagree.

## What stops a publication

Three guards, all of which fail the run rather than warn:

**No signature, no DOI.** If `signed_off_by` is empty in the version's front matter, the run
stops. Attaching a permanent identifier to research nobody has verified would make an unchecked
claim permanently citable, which is precisely the failure this project exists to avoid.

**No minting twice.** If the manifest already records a DOI for that version, the run stops. Two
permanent identifiers for one piece of work is worse than none. If it genuinely needs a new
identifier, that is a new version.

**The corpus must validate.** Front matter, manifests, links and prose are all checked before
anything is deposited, and again afterwards once the DOI and PDF have been written in.

## Why the DOI is reserved before the PDF is built

The PDF is what Zenodo holds and what someone gets when they resolve the DOI. It travels away
from the site entirely: emailed, printed, filed, opened eighteen months later by somebody who has
never seen projectihmr.org.

**So it has to carry its own identifier**, which means the identifier must exist before it is
built. If the DOI were issued at publication in the ordinary way, every downloaded copy would be
missing the one thing needed to cite it.

Zenodo's `prereserve_doi` is what makes this possible. It is not a convenience; it is what makes
the artefact work.

## The sandbox

`sandbox.zenodo.org` is a practice copy of Zenodo. Same interface, same behaviour, but the DOIs
it issues are fake and do not resolve.

`sandbox: true` is the default on the workflow. Leave it on for a rehearsal, untick it when you
mean it.

Two things about the sandbox catch people out:

- **It is a separate system with its own account and its own token.** A zenodo.org login does not
  work there.
- **Communities do not carry across.** The `ihmr` community exists on zenodo.org and not on
  sandbox, so sandbox runs deposit without one.

## Publishing manually instead

Entirely reasonable, especially for the first one. Zenodo has an ordinary web upload form, and
doing it by hand means you see exactly what the record looks like before anything is permanent.

The only thing to get right is the ordering. The upload form has a **Reserve DOI** button: press
it *before* uploading, put the DOI into the article, build the PDF, then upload that PDF and
publish. Same sequence as the workflow, done by hand.

The workflow earns its place when there are twenty outputs and doing it carefully by hand
twenty times is where the mistakes come from.

## Secrets

| Secret | Where | What for |
|:--|:--|:--|
| `ZENODO_API_TOKEN` | `ihmrlabs/ihmr` | Reserving and publishing depositions |

That is the whole list. The workflow writes to this repository, so it uses the built-in
`GITHUB_TOKEN`, and it reads the publish scripts from `ihmr-engine`, which is public and needs no
credential.

An earlier design put the workflow in `ihmr-engine`, which meant it needed a long-lived personal
access token to write here. Moving one file removed a permanent credential.

## After publishing

The pull request contains the DOI, the PDF, and the manifest change. **Check the DOI resolves and
the Zenodo record looks right before merging.** The record's metadata stays editable afterwards
(you can add authors, fix a title, correct an affiliation) but the DOI itself does not change.

Merging triggers the ordinary corpus sync: mirror to R2, snapshot the commit, re-ingest, and the
site picks up the new version.

## Related

- [`branch-protection.md`](branch-protection.md) - the rules on `main`, and why force pushes are blocked
- [`r2-layout.md`](r2-layout.md) - where everything lands in the bucket
- [`workflows.md`](workflows.md) - every workflow, what triggers it, and on which branch
