# AGENTS.md

Instructions for AI agents working in the `ihmr` repository.

`CLAUDE.md` carries the same content. If you are a person, `README.md` and `CONTRIBUTING.md`
are friendlier places to start.

## What this repository is

The **canonical public record** of IHMR — the India Health Maintenance Rail. An open research
project asking how India could build infrastructure for continuous health maintenance at
population scale.

If IHMR claims something publicly, it is represented here.

## Tone — this matters

**The writing here is warm and inviting.** This is a deliberate choice, not an accident of
style. The project depends on domain experts — clinicians, civil servants, community health
workers — choosing to engage, and most of them are not going to push through a document that
reads like a compliance manual.

Write as a knowledgeable person genuinely glad the reader turned up:

- Address the reader directly. Prefer "we" and "you" over the passive voice.
- Explain *why* a rule exists rather than just stating it.
- Make invitations feel like invitations.
- Acknowledge the reader's scepticism generously; it is well earned.

Warm is **not** the same as promotional. No hype, no inflated claims, no manufactured
certainty, no marketing register. The tone to aim for is closer to a good research
publication than to either a standards document or a landing page.

British spelling: *organised, fulfilment, programme, prioritise, behaviour, artefact.*

## Hard rules

- **Markdown only.** No PDFs, Word documents, or proprietary formats.
- **Every document needs complete front matter**, validating against
  `schema/document.schema.json`.
- **Never state a hypothesis as a decision.** Most of this project is `hypothesis`. The status
  field is load-bearing.
- **Never imply IHMR is a Government of India programme**, or that any institution has endorsed,
  funded, or partnered with it. This applies to drafts as much as to published text.
- **Never write clinical guidance.** Clinical claims need named clinical review; flag and stop.
- **Never include personal health information**, or identify anyone who has not consented.
- **Never silently rewrite a published claim.** Mark it `superseded`, keep the original, record
  what replaced it and why, and add an entry to `updates/`.
- **AI output is never evidence.** It helps locate sources; it never replaces reading them.
  This applies to your own output.

## AI disclosure

Set `ai_disclosure` on anything you draft or substantially edit, and **leave `signed_off_by`
blank** — only a named human can sign off. If you are between two tiers, declare the higher
one. Never list an AI as an author. Never write that AI verified anything.

See `AI_USE_POLICY.md`.

## Where things go

| Content | Folder |
|---|---|
| Evidence work, with sources | `research/` |
| Arguments and thinking | `essays/` |
| Something we do not know | `questions/` |
| A proposal open for comment | `rfcs/` |
| A position we have adopted | `decisions/` |
| A test and its result | `experiments/` |
| How something might be built | `architecture/` |
| Converted primary material | `sources/` |
| What changed this week | `updates/` |

Read the folder's `README.md` before adding to it.

## IDs and URLs

IDs are **permanent** and paths are **stable**. Published documents get cited, and every comment
on the website is anchored to a document path and commit. Renaming or renumbering breaks
citations, the provenance chain, and existing comments.

Filenames lead with the ID: `IHMR-RSCH-001-abdm-and-the-action-layer.md`.

## Research standard

Primary sources first. Cite material claims. Separate observed fact from inference, policy
design from implementation, and programme intent from measured outcome. Record uncertainty.
Preserve contradictory evidence. Say what would falsify a claim. Be explicit when evidence from
another country may not transfer to India.

## When you are unsure

Say so, and leave the uncertainty visible in the document rather than resolving it quietly.
Recording an open question is a contribution. Guessing and presenting it as settled is exactly
the failure this project is built to avoid.
