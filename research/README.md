# Research

Work we have actually done, with our sources shown so you can check it.

Each note answers one question, so it can be corrected on its own without disturbing anything
else. We prefer primary sources, cite anything that matters, say what we are unsure about, and
keep the evidence that disagrees with us.

Every note tries to answer:

1. What question are we answering?
2. Why does it matter to IHMR?
3. What evidence did we look at?
4. What did we learn?
5. What are we still unsure about?
6. What does this change about the project?
7. What should someone look at next?

Research that changes nothing about the project should say so. That is a real finding, not a
failure.

Usually `evidence`.

---

## How research is stored

Each piece of research is a **folder**, and each published version is a folder inside it:

```text
research/
└── IHMR-RSCH-001-state-of-indias-healthcare/
    ├── README.md                                    what this is, and its versions
    ├── v1/
    │   ├── IHMR-RSCH-001-state-of-indias-healthcare-v1.md
    │   └── IHMR-RSCH-001-state-of-indias-healthcare-v1.pdf
    └── v2/
        ├── IHMR-RSCH-001-state-of-indias-healthcare-v2.md
        └── IHMR-RSCH-001-state-of-indias-healthcare-v2.pdf
```

### Why versions are folders and not just git history

Git already records every change, so this might look redundant. It is not, and the reason is
citation.

Once someone cites version 1, **version 1 has to stay exactly as it was, at a path that does not
move.** Git can give you that if you know the commit hash, but a reader who has a citation in
front of them should not need to understand git to check it. A version folder is the same
guarantee in a form anyone can use.

So: **published versions are never edited.** If something changes materially, it becomes a new
version. Earlier versions stay where they are, unchanged, forever.

Small corrections - a typo, a broken link - are made in place and noted in the document's
history. A changed number, a changed conclusion, or new evidence means a new version.

### The PDF is generated, never written

**Markdown is the source of truth. The PDF is built from it.**

Nobody edits the PDF, and no PDF is ever the only copy of anything. It is generated on
publication so that the work can be read offline, printed, filed by someone who works in
documents rather than repositories, and attached to an email by a civil servant. Those are real
readers and they matter.

If the Markdown and the PDF ever disagree, the Markdown is right and the PDF needs rebuilding.

### Filenames carry the ID and version

A downloaded PDF loses its folder, so the filename has to say what it is on its own. Anyone who
finds `IHMR-RSCH-001-state-of-indias-healthcare-v1.pdf` in a downloads folder eighteen months
later can still identify it.

### The PDF is what the DOI points at

When a version is published, its **PDF is the artefact deposited with Zenodo**, and that is what
someone downloads when they resolve the DOI. The Markdown source is deposited alongside it, so
the source is preserved too.

This sets the order of operations, and the order is not arbitrary:

```text
1  version reaches evidence or decision
2  create the Zenodo deposition
3  reserve the DOI            ← before anything is built
4  write the DOI into the Markdown front matter
5  generate the PDF from that Markdown
6  upload the PDF and the Markdown
7  publish
```

**Step 3 has to come before step 5.** If the DOI were issued at publication, the PDF would be
built before its own identifier existed, and every downloaded copy would be missing the one
thing that lets someone cite it. Reserving first is what makes a self-identifying PDF possible.

Each version gets its own DOI. A shared concept DOI covers all versions and always resolves to
the newest, so a citation can be either exact or general.

Because a PDF travels away from this site, it carries everything needed to stand alone: the
citation block, the AI disclosure, the provenance line, the licence, and its own DOI.

### The folder README

Each research folder has a `README.md` giving the title, a one-line summary, the current version,
and a list of every version with its date, its DOI, and what changed.

That page is what someone lands on when they follow a link to the research rather than to a
specific version.

### Versions and supersession are different things

A **new version** is a revised edition of the same work.

**Superseded** means a different document has replaced this one entirely. That is recorded in
front matter with `superseded_by`, and the original stays published.

Essays follow exactly the same structure.
