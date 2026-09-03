# IHMR

**India Health Maintenance Rail**

Hello, and thank you for coming to look.

This is an open research project asking a question we think deserves a serious attempt:

> **How could India build infrastructure that continuously helps maintain and improve the
> health of every person, instead of waiting for illness and reacting to it?**

We are early. We are working in the open. And honestly, we would rather be corrected than
agreed with. If you know something we do not, and if you work anywhere near health in India you
almost certainly do, we would love to hear from you.

---

## The question, put plainly

Most healthcare is organised around episodes:

```text
person becomes sick → seeks care → system reacts → person disappears until next time
```

India has already built a remarkable amount of what a population-scale health system needs.
Digital identity. Health records. Registries and consent. Public insurance. One of the world's
largest immunisation programmes. An extensive public primary-care network. And a community
health workforce of roughly a million people, which very few countries can match.

What does not exist yet is a layer that answers, continuously and for each person:

> **What should happen next, who is going to make it happen, and how?**

That is what we are trying to understand. Not to replace what India has built, but to ask what
would connect it into something that maintains health rather than only recording it.

## We always tell you how sure we are

A project like this earns trust by being honest about what it knows. So every document says, at
the top, how much weight we put behind it.

| Status | What it means |
|:--|:--|
| `hypothesis` | We currently think this might be true |
| `evidence` | This is what the available research supports |
| `proposal` | This is how IHMR could work |
| `specification` | Mature enough to define formally |
| `experiment` | We are testing whether it works |
| `decision` | We have adopted this position, for now |
| `superseded` | Something newer has replaced this |

**Most of this project is `hypothesis` today.** We would much rather say so than dress
speculation up as certainty. And when we change our minds, we say that too, keeping the old
reasoning where you can still find it.

## Finding your way around

| Folder | What is inside |
|:--|:--|
| [`questions/`](questions/) | What we do not know. A good place to start |
| [`research/`](research/) | Work we have done, with our sources shown |
| [`essays/`](essays/) | Our thinking and arguments |
| [`rfcs/`](rfcs/) | Proposals open for comment |
| [`decisions/`](decisions/) | What we have adopted, and what it replaced |
| [`experiments/`](experiments/) | Things we tested, and what happened |
| [`architecture/`](architecture/) | How the system might be built |
| [`sources/`](sources/) | Primary material, converted so you can check our work |
| [`updates/`](updates/) | What changed, and what we learned |
| [`about/`](about/) | How we work: governance, glossary, roadmap, policies |

Everything is Markdown. Every document has a permanent ID and a visible history, so any claim
can be traced back to where it came from.

## Some things we are careful to say

We would rather be clear about this upfront than let anyone assume it. IHMR is **not**:

- an AI doctor, a chatbot, or a wellness app
- a hospital chain or an insurance product
- a replacement for doctors, or for India's existing public health infrastructure
- a monolithic health database, or any kind of surveillance system
- a finished proposal for a national health system
- a claim that preventive health is a new idea
- a claim that medical decisions can be automated
- a promise to make every Indian healthy

**IHMR is not a Government of India programme.** It is not endorsed by, funded by, or
affiliated with any government body or institution. If that ever changes, we will say so
clearly and immediately.

Nothing here is clinical guidance.

## Please come and argue with us

This is the part that matters most.

We need correction far more than we need agreement. The people best placed to give it are
clinicians, public health researchers, epidemiologists, health economists, civil servants,
insurers, community health workers, privacy researchers, lawyers, and anyone who has spent real
time inside India's health system.

**You do not need to be an engineer.** You do not need a GitHub account. And you do not need to
propose a fix: telling us what is wrong is a complete contribution on its own.

Have a look at [`questions/`](questions/), read
[how to contribute](.github/CONTRIBUTING.md), or just write to us. We read everything.

## How we use AI

We use AI across this project, in research, engineering and drafting, and we think being open
about that is part of using it responsibly. Every document says how AI was involved. **Every
document is signed off by a named person who has checked its claims.**

See [how we use AI](about/how-we-use-ai.md).

## Licence

- Research and documentation: **CC BY 4.0**, see [LICENSE](LICENSE)
- Software: **Apache 2.0**, see [LICENSE-CODE](LICENSE-CODE)
- Third-party material in `sources/` keeps its original licence, recorded per file

Please reuse this. Adapt it, fork it, build on it, cite it, take it somewhere we never would.
Government use, commercial use and academic use are all explicitly welcome. Attribution is all
we ask.

## Related work

| Repository | What it is for |
|:--|:--|
| **`ihmr`** | This one. Our research, proposals and decisions |
| [`ihmr-engine`](https://github.com/ihmrlabs/ihmr-engine) | Where we test ideas: simulations, models, rules, tooling |

---

[projectihmr.com](https://projectihmr.com) · hello@projectihmr.com

Maintained by [Tejas Parthasarathi Sudarshan](https://tejassuds.com)
