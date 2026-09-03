---
id: IHMR-PAGE-005
type: page
title: Roadmap
status: current
created: 2026-09-03
updated: 2026-09-03
ai_disclosure: substantially-ai-assisted
ai_tools:
  - claude-opus-5
signed_off_by:
signed_off_date:
license: CC-BY-4.0
lang: en
---

# Roadmap

Where this is going, and roughly in what order. It is honest about how early we are.

We are deliberately **not** doing website → MVP → pilot → scale. Building software before we
understand the problem would produce something confident and wrong.

## Where we are

**Stage 1 of 8.** Framing the problem and establishing the evidence base. Nothing here has been
tested against reality yet.

## The sequence

### 0. Frame the problem
What is IHMR actually trying to achieve, and what would count as success?

### 1. Establish the evidence base ← *we are here*
Understand India's health system properly - its burden of disease, delivery, workforce,
financing, and digital infrastructure - before proposing anything. Then look carefully at what
other countries have tried.

### 2. Define the primitives
Health, health state, obligation, intervention, fulfilment, outcome, consent, financing. Get
the vocabulary right, because everything downstream inherits it.

### 3. Design the rail
Identity, information, action, routing, financing, trust, intelligence, delivery.

### 4. Simulate it
Synthetic people, cohorts, districts, pathways, and constraints - in
[`ihmr-engine`](https://github.com/ihmrlabs/ihmr-engine).

### 5. Stress-test it
Clinical, ethical, privacy, economic, institutional, operational, rural, urban. Deliberately
including how it fails.

### 6. Prototype components
Parsers, obligation engines, health-state services, routing, tooling.

### 7. Test in the real world
Only after the research holds up and with proper institutional collaboration. Not before.

### 8. Work out the institutional vehicle
What would actually need to exist for something like this to operate in India?

## What we are working on now

Live status is on [projectihmr.com](https://projectihmr.com), derived from this repository, so
it cannot drift out of date. [`updates/`](../updates/) has the log.

## Where we would most like help

Right now, at stage 1: **anything that makes our picture of India's health system more accurate.**
Corrections, missing sources, things we have characterised badly, and field knowledge that never
made it into the literature.

See [`questions/`](../questions/) and [CONTRIBUTING.md](../.github/CONTRIBUTING.md).

## A caveat

This roadmap is a plan, not a promise. It will change as we learn things - and when it does, we
will say what changed and why.
