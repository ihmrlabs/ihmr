---
id: IHMR-Q-010
type: question
title: Can the system coordinate care without exposing the diagnosis?
status: hypothesis
created: 2026-09-03
updated: 2026-09-03
topics: [privacy, consent, architecture]
related: [IHMR-Q-003, IHMR-Q-007]
ai_disclosure: ai-assisted-research
signed_off_by:
license: CC-BY-4.0
lang: en
---

# Can the system coordinate care without exposing the diagnosis?


To arrange a test, someone has to know a test is needed. Do they also have to know why?

## Why it matters

Coordination means telling third parties something. A laboratory, a pharmacy, a community
health worker, an insurer. Each of them needs enough to act and, we suspect, considerably less
than the full picture.

Getting this wrong makes the system a disclosure engine, which would be both a privacy failure
and, given what a diagnosis can mean socially in practice, a real harm to people.

## The questions inside the question

- What is the least a fulfiller needs to act correctly and safely?
- Can something be actioned without revealing the condition that prompted it?
- Where does minimising information become clinically unsafe? There will be cases
- Who is allowed to query someone's health state, for what purpose, and with what record?
- How is consent expressed so it is meaningful rather than a checkbox?
- How does someone see who has looked at what?

## Where our thinking currently sits

Identity existing should not make health information broadly accessible. Access should be
purpose limited and visible to the person. These feel like the right instincts and are not yet
a design.

## What would count as an answer

A concrete account of what each type of participant sees, with the clinical safety exceptions
named explicitly rather than discovered later.

## Help us with this

Privacy engineers and researchers, particularly anyone who has implemented purpose limitation
in a system that actually had to work.
