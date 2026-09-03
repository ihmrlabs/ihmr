# Privacy

**Last updated: 3 September 2026**

A project that spends its time thinking about health data privacy should be exemplary about its
own. So this page tries to be genuinely readable rather than legally defensive, and to tell you
things you would want to know even where we are not obliged to.

If anything here is unclear, or if you think we have got something wrong, please write to
hello@projectihmr.com. We would rather hear it.

---

## Who is responsible for your data

**Tejas Parthasarathi Sudarshan**, personally.

IHMR Labs is not a registered company, trust, or society. It is an open research project
maintained by one person, and that person is the data fiduciary under India's Digital Personal
Data Protection Act 2023, and the data controller for the purposes of the GDPR if you are in the
UK or EU.

We mention this because it matters practically: there is no company to hide behind, and there is
no support department. If you write to us about your data, a person reads it.

Contact: **hello@projectihmr.com**

## What we collect, and why

### If you only read the site

Nothing that identifies you personally.

Our servers keep short-lived technical logs, which is unavoidable for any website. These include
a truncated IP address, the page requested, and basic browser information. We use them to keep
the site running and to spot abuse. They are not linked to you, and they are not used to build
any profile.

If you consent to analytics, see the section below.

### If you leave a comment

To publish a comment we ask for:

| What | Required | Why |
|:--|:--|:--|
| Your name | Yes | So we know who we are talking to. You choose whether it appears publicly |
| Email address | Yes | To verify you are a real person, and to tell you whether your comment was published |
| Phone number | No | Only if you would like us to be able to reach you another way |
| Display preference | Yes | Whether to show your name publicly, or publish anonymously |
| The comment | Yes | That is the point |

**Your email address and phone number are never shown publicly.** Not on the site, not in our
API, not through our MCP server, not in any feed, and not to anybody who is not us.

This is not only a promise. Our database is built so that the code serving public pages has no
route to reach the table containing your contact details. See [security](security.md).

If you comment anonymously, your comment shows no name. We still know internally which verified
email it came from, so that we can tell you whether it was published and contact you if there is
a genuine reason to.

### If you email us

We keep the correspondence, because that is what email is. We do not add you to anything.

## Analytics

We use **PostHog** to understand how the site is used: which documents get read, where people
give up, whether the open questions are actually being found.

**Analytics only runs if you agree to it.** If you decline, or ignore the banner, it does not
load at all. See [cookies](cookies.md).

Things we have deliberately turned off:

- **Session recording is disabled.** People write comments about health on this site, sometimes
  their own. Recording what someone types before they decide whether to post it would be
  indefensible, so we do not do it at all
- **IP addresses are anonymised** before they reach PostHog
- **No cross-site tracking**, no advertising networks, no data brokers, no third-party
  advertising or marketing pixels of any kind

We do not sell data. There is nothing to sell and no business model that would want it.

## Where your data lives

| What | Where | Who runs it |
|:--|:--|:--|
| Your email and phone | **India** (Mumbai) | Supabase, on Postgres |
| Your published comment | **India** (Mumbai) | Supabase |
| Site content and files | Global edge network | Cloudflare |
| Email delivery | United States, in transit | Resend |
| Analytics, if you consent | European Union | PostHog |

**Your identifying contact details are stored in India.** That is deliberate.

Two honest qualifications. Sending you an email necessarily routes your address through a mail
provider, which is true of any service. And analytics data, if you consent to it, is processed
in the EU because PostHog does not offer an Indian region. We think that is a reasonable trade
for anonymised usage statistics, but you should know it, and it is one of the reasons analytics
is opt-in.

## How long we keep things

| What | How long |
|:--|:--|
| A published comment | While it is published. It is part of a public record |
| Your email and phone | While your comment is published, so that we can contact you about it |
| A rejected comment and its email | Two years, so we can review our own moderation decisions |
| Verification codes | Ten minutes |
| Your session cookie | 180 days, unless you clear it |
| Technical server logs | 30 days |
| Analytics, if you consent | 12 months |

Ask us to delete your data and we will, including your comment if you want it removed.

## What you can ask us to do

Under India's DPDP Act, and under the GDPR if it applies to you, you can ask us to:

- **Tell you what we hold** about you
- **Correct** anything wrong
- **Delete** your data, including any published comment
- **Withdraw consent** for analytics at any time
- **Give you a copy** of what you gave us
- **Nominate someone** to exercise these rights if you die or become incapacitated, which the
  DPDP Act specifically provides for

Email **hello@projectihmr.com**. We aim to respond within seven days and will not make you jump
through hoops to prove who you are beyond confirming the email address involved.

If you are unhappy with how we have handled it, you can complain to India's Data Protection
Board, or to your national supervisory authority if you are in the UK or EU.

## Children

This site is for people working on or interested in health policy and research. It is not aimed
at children, and we do not knowingly collect data from anyone under 18. Under the DPDP Act,
processing children's data requires verifiable parental consent, which we are not set up to
obtain, so please do not comment if you are under 18.

## What we do not do

- Sell or rent your data to anyone
- Share it with advertisers, data brokers, or partners
- Track you across other websites
- Build a profile of you
- Use your data to train any AI model
- Publish your contact details, ever
- Collect health information about you. **We do not want it, and if you include identifiable
  health information in a comment we will not publish it** - see [moderation](moderation.md)

That last one is worth saying twice. This project is *about* health data. It does not *hold*
health data about anybody.

## If something goes wrong

If personal data is exposed, we will tell the people affected and the Data Protection Board
without waiting to be asked, and we will publish what happened and what we changed. See
[security](security.md).

## Changes to this policy

We will update this page as the project changes, and the date at the top will tell you when.
If a change materially affects what we do with data you have already given us, we will email
you rather than quietly editing the page.

Previous versions are in the repository history, because that is how everything here works.

---

Questions, or something we have got wrong: **hello@projectihmr.com**
