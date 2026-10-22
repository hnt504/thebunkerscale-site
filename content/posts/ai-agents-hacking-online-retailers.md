---
title: 'One Capable Criminal, Scaled Up: AI Agents Are Breaking Into Online Stores for About $25 a Target'
date: 2026-09-26
rating: 8
band: Pay Attention
slug: ai-agents-hacking-online-retailers
type: Safety Watch
description: 'Security researchers say one financially motivated attacker used open-source AI agents to attack hundreds of online retailers, stealing more than 600,000 valid card records and planting card skimmers on store websites. The AI didn''t go rogue. It made one person far more productive.'
---

*Rating as of September 26, 2026: 8/10 · Pay Attention*

*The scary part isn't that AI decided to become a criminal. It's that it made one criminal much more scalable.*

## What changed

Gambit Security, a cybersecurity company, published an interim report on an ongoing campaign against online retailers [1]. Its researchers say they recovered the attacker's own staging server and reconstructed the campaign from it [1].

According to Gambit [1]:

- A financially motivated attacker is running three open-source AI agent tools against hundreds of online stores, "almost entirely unattended."
- One tool scans for weaknesses, one tries to break in, and one runs the overall operation and makes tactical decisions.
- Between September 10 and 15 alone, 105 attacks were launched and at least 27 companies were compromised to varying degrees. The activity goes back to July and is still running.
- At least 600,000 unexpired credit card records were taken from two companies, and card-stealing code was planted on the checkout pages of five others.
- Where it got in, it usually took less than a day, often just a few hours.
- In some cases, the agent's own "cleanup" routine deleted the victim's data.

BleepingComputer and SecurityWeek both reported the findings [2][3]. BleepingComputer says the human operator gave the agents brief instructions about the goals and then let them handle the rest [2]. The reported cost works out to roughly $25 per scanned company, which is a cost per attempt, not a price for a guaranteed hack [1][4].

## Why it matters

So far on this site, most of the cyber stories have been about AI agents getting out of a test and wandering where they shouldn't. This is different. A person deliberately pointed AI agents at real businesses, and it worked, at meaningful scale, against real customers' payment cards.

The important word here is leverage. Breaking into one online store takes skill and time. Breaking into dozens a day used to take a team. If AI tools let one person run that many attacks in parallel, for the cost of a nice lunch per target, then the number of people capable of doing this goes up, and so does the pace.

## What you can probably ignore

**"Autonomous AI hackers are on the loose."** A human chose to run this campaign and set its goals [2]. The AI did the legwork.

**"Your card was definitely stolen."** The victims mostly haven't been named. If you're worried, the usual advice applies: watch your statements and use your card issuer's alerts.

## Why it earned this rating

On the side of a higher number:

- Real harm to real people: hundreds of thousands of payment card records [1].
- Most of the attack chain was run by AI with little human involvement [1][2].
- Skimmers planted on live websites are something outside researchers can check, and Gambit says it verified many of them [1].

On the side of a lower number:

- Most of the detailed numbers come from one security company, and its report is interim. Gambit itself says a few errors are possible [1].
- A human started and directed it. This is not AI acting on its own.
- The attack methods are familiar ones, just faster and cheaper.

Meaningful real-world harm with AI doing most of the work puts this at an **8**. Not a 9, because it's one attacker, mostly one source, and nothing about it suggests the AI is out of anyone's control.

## What I'm watching next

- **Independent confirmation** from other security firms or from the victims themselves.
- **Copycats.** If several unrelated criminal groups start using the same approach, this becomes a different and bigger story.
- **What the makers of these open-source tools do** in response.

> **Bunker Check**
>
> **Current rating:** 8/10 · Pay Attention
>
> **Direction:** Holding
>
> **Could move higher if:** Several independent groups are found running similar AI-driven campaigns, or the agents start finding brand-new vulnerabilities on their own.
>
> **Could move lower if:** Further investigation shows the AI played a smaller role than reported.

The shovel stays in the garage. Your card issuer's fraud alerts, however, are worth turning on.

## Sources

1. Gambit Security, "Autonomous AI Agents are breaking into hundreds of Online Retailers for $25 a target in an ongoing campaign," September 22, 2026 (primary source, interim report). https://gambit.security/blog-posts/autonomous-ai-agents-online-retailers-25-a-company
2. BleepingComputer, "Malicious AI agents steal 600K credit cards, infect 100+ sites with skimmers," September 23, 2026. https://www.bleepingcomputer.com/news/security/malicious-ai-agents-steal-600k-credit-cards-infect-100-plus-sites-with-skimmers/
3. SecurityWeek, "AI-Powered Campaign Targets Hundreds of Online Retailers," September 2026. https://www.securityweek.com/ai-powered-campaign-targets-hundreds-of-online-retailers/
4. CSO Online, "AI tools help hacker break in for $25 per target," September 2026. https://www.csoonline.com/article/4226861/ai-tools-help-hacker-break-in-for-25-per-target.html
