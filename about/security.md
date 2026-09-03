---
id: IHMR-PAGE-007
type: page
title: Security
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

# Security

**Last updated: 3 September 2026**

This page is about how we protect what we hold. If you have **found** a vulnerability, please
see [how to report it](../.github/SECURITY.md) - and thank you.

---

## The short version

The most effective thing we do for your security is **hold almost nothing**.

This project is about health data. It does not contain health data about anybody. The only
personal information here is a name, a verified email address, and sometimes a phone number,
given voluntarily by people who left a comment.

Everything else on this site is public research that we actively want you to copy.

## What we hold, and what we deliberately do not

| We hold | We do not hold |
|:--|:--|
| Your name, if you gave one | Any health information about you |
| Your verified email address | Passwords - there are no accounts |
| Your phone number, if you offered it | Payment details - there is nothing to buy |
| Your published comment | Your location beyond a truncated IP in short-lived logs |
| Whether you chose to be anonymous | Anything from other websites you visit |

No passwords means no password breach. No payment details means no card data. Quite a lot of
security comes from having declined to collect things in the first place.

## The guarantee we care most about

**Your email address is never shown publicly**, and we have tried to make that structurally true
rather than merely a policy someone has to remember.

Your contact details live in a separate database table from your comment. The database role used
to serve public pages, the API, the MCP server and every feed **has no permission to read that
table at all**. Row-level security enforces it inside Postgres.

So it is not that our code is careful to avoid selecting your email. It is that if the code
tried, the database would refuse.

We think this matters. Policies get forgotten during a refactor eighteen months later, by
someone who was not part of this conversation. Permissions do not.

## Where things live

| What | Where |
|:--|:--|
| Your email and phone, encrypted | Postgres in **Mumbai, India** |
| Your published comment | Postgres in **Mumbai, India** |
| Encryption keys | Held separately from the database, never in it |
| Public site content | Cloudflare's global network |
| Analytics, only with consent | PostHog, European Union |

The site sits behind Cloudflare, which handles denial-of-service protection and rate limiting
before traffic reaches us.

## Who can see your details

Only the maintainer, and only where there is a reason - answering you about a comment,
principally.

The moderation tools sit behind an authenticated gate that unauthenticated requests never get
past. Every moderation action is logged with who did it and when.

There is currently one person with access. When that changes, this page will say so.

## What we ask of you

Please **do not put identifiable health information in a comment**, whether it is yours or
somebody else's. Not because we would misuse it, but because a public research site is not the
place for it and we would have to decline to publish it. See [moderation](moderation.md).

If you want to tell us something that requires personal detail, email us instead.

## If something goes wrong

We will:

1. Fix it
2. Tell the people affected directly, without waiting for anyone to ask
3. Notify India's Data Protection Board within the required timeframe
4. **Publish what happened, what we got wrong, and what changed**

Point four is not required of us. We are committing to it because a project asking people to
trust its reasoning about health infrastructure should be willing to show its own failures.

## Honest limitations

- This is one person's project, not an organisation with a security team. There is no
  twenty-four-hour response, and we should not pretend otherwise
- We depend on Cloudflare, Supabase, PostHog and Resend. Their security is our security, and we
  have chosen them partly on that basis but we do not control them
- Nothing here has been through a formal security audit. If you have the skills and would like
  to look, we would genuinely welcome it

Saying this plainly seems better than implying a maturity that does not exist yet.

## If the project ends

If IHMR Labs stops, personal data will be deleted rather than transferred, and we will say so
publicly before it happens. The public research is CC BY licensed and can outlive the project.
Your email address should not.

---

Report a vulnerability: [how to do that](../.github/SECURITY.md)
Anything else: **hello@projectihmr.com**
