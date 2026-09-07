---
id: IHMR-Q-005
type: question
title: How do we know something actually happened?
status: hypothesis
created: 2026-09-03
updated: 2026-09-03
topics: [verification, architecture]
related: [IHMR-Q-006, IHMR-Q-007]
ai_disclosure: ai-assisted-research
signed_off_by:
license: CC-BY-4.0
lang: en
---

# How do we know something actually happened?


We think this may be the hardest problem in the whole design, and we would rather say that
loudly than discover it later.

## Why it matters

It is not enough for the system to record that someone was advised to do something. The question
that matters is whether it happened. Was the test done? Was the medicine obtained and taken? Did
the referral complete? Did the blood pressure actually come down?

**If verification does not work, the whole thing degrades into a reminder system**, which is
precisely what we have said IHMR is not.

## Why it is hard

Evidence has to flow back from thousands of independent people and organisations, most of whom
have no particular reason to report anything.

India's immunisation platform manages this for vaccination, and it is worth understanding why:
vaccination is a discrete event, publicly administered, and already recorded as part of the
work. Almost nothing else in health looks like that. "Did she take her medication this month" and
"did her blood pressure come down" have no equivalent return path.

## What would count as an answer

- A realistic account of which things can be verified, which can be reasonably inferred, and
  which simply cannot be known
- Some sense of what proportion of verification could come from existing systems
- A design that behaves sensibly when verification is absent, rather than treating silence as
  failure
- Honest thinking about whether interpreting messy returned evidence is itself a job for AI

## Where our thinking currently sits

Verification probably does not need to be uniform. Some things are annual and light touch.
Others need close attention. What matters is that once a need is identified, the person is not
lost track of.

We suspect this should be one of the first things we prototype, precisely because it is the step
most likely to show the design does not work.

## Help us with this

If you have built or operated any system that has to confirm something happened in the physical
world, across many independent parties, we would like to hear how it went.
