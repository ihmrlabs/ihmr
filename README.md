# IHMR

**India Health Maintenance Rail.**

Welcome. This is an open research and engineering project asking a question we think is worth
a serious try:

> **How could India build infrastructure that continuously helps maintain and improve the
> health of every person — rather than waiting for illness and reacting to it?**

We are early, we are working in the open, and we would genuinely rather be corrected than
agreed with. If you know something we do not — and if you work anywhere near health in India,
you almost certainly do — we would love to hear from you.

---

## The question, put plainly

Healthcare is mostly organised around episodes:

```text
person becomes sick → seeks care → system reacts → person disappears until the next episode
```

India has already built a remarkable amount of the machinery for a population-scale health
system: digital identity, health records, registries, consent infrastructure, insurance,
immunisation systems, an extensive public primary-care network, and one of the largest
community health workforces anywhere in the world.

What does not yet exist is a layer that answers, continuously and for each person:

> **What should happen next — and who is going to make it happen, and how?**

That is what we are trying to understand. Not to replace what India has built, but to ask what
would connect it into something that maintains health rather than only recording it.

## Everything here tells you how sure we are

We think a project like this earns trust by being honest about what it knows. So every document
carries its epistemic state, right at the top:

| Status | What it means |
|---|---|
| `hypothesis` | We currently think this might be true |
| `evidence` | This is what the available research supports |
| `proposal` | This is how IHMR could work |
| `specification` | Mature enough to define formally |
| `experiment` | We are testing whether it works |
| `decision` | We have adopted this position, for now |
| `superseded` | Something newer has replaced this |

**Most of this project is currently `hypothesis`** — and we would rather say so than dress
speculation up as certainty. When we change our mind, we say that too, and we keep the old
reasoning where you can find it.

## Finding your way around

| Folder | What is in it |
|---|---|
| [`research/`](research/) | Work we have done, with sources |
| [`essays/`](essays/) | Our thinking and arguments |
| [`questions/`](questions/) | What we do not know — a good place to start |
| [`rfcs/`](rfcs/) | Proposals open for comment |
| [`decisions/`](decisions/) | What we have adopted, and what it replaced |
| [`experiments/`](experiments/) | Things we tested, and what happened |
| [`architecture/`](architecture/) | How the system might be built |
| [`sources/`](sources/) | Primary material, converted so you can check our work |
| [`updates/`](updates/) | What changed, and what we learned |

Everything is Markdown. Every document has a permanent ID and a visible history, so you can
always trace a claim back to where it came from.

## Some things we are careful to say

We would rather be clear about this upfront than let anyone infer it. IHMR is **not**:

- an AI doctor, a chatbot, or a wellness app
- a hospital chain or an insurance product
- a replacement for doctors, or for India's existing public-health infrastructure
- a monolithic health database, or any kind of surveillance system
- a finished proposal for a national health system
- a claim that preventive health is a new idea, or that medical decisions can be automated
- a promise to make every Indian healthy

**IHMR is not a Government of India programme.** It is not endorsed by, funded by, or
affiliated with any government body or institution. If that ever changes, we will say so
clearly.

Nothing here is clinical guidance.

## Come and argue with us

Honestly, this is the part that matters most.

We need correction far more than we need agreement, and the people best placed to give it are
clinicians, public-health researchers, epidemiologists, health economists, civil servants,
insurers, community health workers, privacy researchers, lawyers, and anyone who has spent time
inside India's health system.

**You do not need to be an engineer**, and you do not need to propose a fix. Telling us what is
wrong is a complete contribution on its own.

Start with [CONTRIBUTING.md](CONTRIBUTING.md), or just email us. We read everything.

## How we use AI

We use AI across this project — in research, engineering, and drafting — and we think being
open about that is part of doing it responsibly. Every document says how AI was used, and
**every document is signed off by a named human who has checked its claims.**

See [AI_USE_POLICY.md](AI_USE_POLICY.md).

## Licence

- Research, documentation, and specifications: **CC BY 4.0** — [LICENSE](LICENSE)
- Software: **Apache 2.0** — [LICENSE-CODE](LICENSE-CODE)
- Third-party material in `sources/` keeps its original licence, recorded per file.

Please reuse this. Adapt it, fork it, build on it, cite it, take it somewhere we never would.
Government use, commercial use, and academic use are all explicitly welcome — attribution is
all we ask.

## Related repositories

| Repository | What it is for |
|---|---|
| **`ihmr`** | This one — our public research, proposals, and decisions |
| [`ihmr-engine`](https://github.com/ihmrlabs/ihmr-engine) | Where we test ideas: simulations, models, rules, tooling |

---

Project: [projectihmr.com](https://projectihmr.com) · Say hello: hello@projectihmr.com

Maintained by [Tejas Parthasarathi Sudarshan](https://tejassuds.com).
