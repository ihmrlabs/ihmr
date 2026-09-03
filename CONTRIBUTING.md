# Contributing

We are genuinely glad you are here.

**You do not need to be an engineer to contribute**, and you do not need to know anything about
Git. If our tooling gets in the way of you telling us something useful, that is our problem to
fix — please just email hello@projectihmr.com and we will sort it out.

The single most valuable thing you can do is **tell us where we are wrong**.

---

## What we most need from you

| If you are… | What would help us enormously |
|---|---|
| A clinician | Tell us where a clinical assumption is wrong, or unsafe |
| A public-health researcher | Tell us if this has been tried before, and what happened |
| An epidemiologist | Challenge how we describe burden, risk, or population data |
| A health economist | Take apart the financing argument — who really pays for prevention? |
| A civil servant or state health official | Tell us what is institutionally impossible, and why |
| An insurer | Tell us whether prevention financing is realistic or wishful thinking |
| A community health worker, ASHA, or ANM | Tell us what the last mile actually looks like |
| A privacy or legal researcher | Find the dangerous assumption before anyone builds it |
| An engineer or data scientist | Break our models, simulations, and architecture |
| Someone who has navigated the health system | Tell us what it actually feels like from the inside |

If you do not see yourself on this list, that does not mean you are not welcome. It probably
means we have not thought of you yet, and we would like to.

## Four ways in, easiest first

### 1. Leave a comment on the website

At [projectihmr.com](https://projectihmr.com). No account needed — you verify your email once,
and you can comment under your name or anonymously.

**A real person reads every comment before it is published**, and if we do not publish yours,
we will write back and tell you why. That is not there to filter out disagreement — disagreement
is exactly what we are hoping for. It is there to keep the discussion useful and to make sure
nobody accidentally shares personal health information in public.

### 2. Start a Discussion

[GitHub Discussions](https://github.com/ihmrlabs/ihmr/discussions) is for open conversation —
questions, challenges, and ideas that do not attach neatly to one document.

### 3. Open an Issue

Good for a specific correction, a factual error, a missing source, or work you think should
exist. Opening an issue does not commit us to anything, and it does not commit you to doing it.

### 4. Open a Pull Request

If you are comfortable with it, propose the change directly. **Prose is as welcome as code** —
most of this repository is writing.

## How to tell us we are wrong

This is the contribution we value most, so here is what makes it easiest for us to act on. None
of it is required — a rough note is much better than no note.

- **Point at the claim.** Quote it, or give us the document ID and section.
- **Say what is wrong** — the fact, the reasoning, the framing, or the conclusion.
- **Share a source if you have one.** If you know it from practice rather than from the
  literature, please say so — field knowledge is real evidence, and we would much rather have it
  labelled honestly than dressed up as a citation.
- **Tell us what would change our mind**, if you can see it.

You do not need to propose a fix. Spotting the problem is the hard part.

## If you are writing a document

Everything here is **Markdown** — plain text with light formatting. If you can write in a word
processor, you can write Markdown.

Every document starts with a small block of information about itself:

```yaml
---
id: IHMR-RSCH-001
type: research
title: ABDM and the Missing Action Layer
status: evidence
authors:
  - Your Name
created: 2026-09-04
updated: 2026-09-04
topics: [abdm, health-information]
related: [IHMR-Q-003]
ai_disclosure: none
signed_off_by: Your Name
signed_off_date: 2026-09-04
license: CC-BY-4.0
lang: en
---
```

Our checks will validate this automatically and tell you plainly if something is missing. If
you would rather not deal with it at all, send us the text and we will handle the rest.

Just below the title, every document carries a short line saying how AI was used in writing it.
See [AI_USE_POLICY.md](AI_USE_POLICY.md).

### The standard we hold ourselves to

This project touches health, public policy, and national infrastructure. Careless research here
does not just produce a weak document — it produces a plausible, well-argued proposal about how
a country should look after the health of more than a billion people. So we try to be careful:

- **Prefer primary sources**, and cite anything that matters.
- **Separate what you observed from what you inferred**, out loud.
- **Distinguish policy design, implementation, and measured outcome.** They are three different
  questions and conflating them is the most common error in this field.
- **Say what you are unsure about.** Uncertainty is information.
- **Keep the evidence that disagrees with you.** Please do not quietly drop the inconvenient
  study.
- **Say what would prove you wrong.**
- **Be explicit** when evidence from another country may not transfer to India.
- **AI summaries are not evidence.** They are useful for finding sources; they never replace
  reading them.

### Clinical claims

Anything clinical needs review by someone clinically qualified. If that is not you, flag it and
stop — we will find a reviewer. We would much rather hold a claim than publish it unreviewed.

**We do not issue clinical guidance**, and nothing here should read as though we do.

## Things we will not publish

- Personal health information, yours or anyone else's
- Material identifying someone who has not agreed to it
- Anything implying IHMR is a government programme, or endorsed by an institution that has not
  endorsed it
- Clinical advice
- Promotional content

## Credit

We credit contributors by name, and we would like to credit you. **AI tools are never listed as
authors** — a tool we used is not a person to thank.

If you would rather contribute without public attribution, just say so. That is completely fine
and we will respect it.

## Being decent to each other

See [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md). The short version: argue with the work as hard as
you like — please do — but be kind to the person.

---

Not sure where to start? [`questions/`](questions/) is a good place. Or just email
hello@projectihmr.com and tell us what you are thinking. We read everything.
