# Technicals

How this repository actually operates: what runs, what it writes, and why each rule exists.

Most of it follows from one asymmetry. **Published paths get cited.** A DOI landing page,
somebody else's bibliography, and every comment on the website all point at a path in `main`. So
the machinery is built around not breaking those, which makes it more careful than a repository
of this size would otherwise need.

| Document | What it covers |
|:--|:--|
| [publishing.md](publishing.md) | How a research version gets a DOI, and why a push cannot publish |
| [workflows.md](workflows.md) | Every workflow, its trigger, and what it writes |
| [branch-protection.md](branch-protection.md) | The rules on `main`, and why force pushes are blocked |
| [r2-layout.md](r2-layout.md) | Where everything lands in the bucket, and why there are three copies |

## The four rules everything else follows from

**A DOI cannot be deleted.** So publishing is the hardest thing to do here: it needs a signature,
a dry run, and a deliberate manual step.

**A published version is never edited.** A material change becomes a new version. Earlier
versions stay exactly as they were, because someone may have cited them.

**A pipeline never deletes.** Both sync workflows use `copy`. Removing something published is a
human decision, recorded.

**Markdown is the source of truth.** PDFs are generated, never authored, and never the only copy
of anything. If the two disagree, the Markdown is right.
