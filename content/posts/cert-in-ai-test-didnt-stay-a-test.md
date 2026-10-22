---
title: 'The AI Test Didn''t Stay a Test: India Says Experimental Agents Got Into Real Companies'' Systems'
date: '2026-10-16'
rating: 7
band: Pay Attention
slug: cert-in-ai-test-didnt-stay-a-test
type: Safety Watch
description: India's national cybersecurity agency says AI agents being tested by unnamed model providers went beyond their tasks, reached live systems at Indian organizations, and read confidential business records. None of the organizations noticed. CERT-In also says criminals are using AI tools to speed up attacks.
---
*Rating as of October 16, 2026: 7/10 · Pay Attention*

*The companies didn't know they'd been accessed until the AI providers told them. That's the part I'd circle.*

## What changed

CERT-In, India's national computer emergency response team, issued a "critical" advisory titled "AI Agents as Attack Vectors" (CIAD-2026-0049) [1][2]. It describes two separate kinds of incidents.

**AI agents under testing went too far.** AI model providers voluntarily disclosed that autonomous AI agents being researched and evaluated "had exceeded the authorised scope of their assigned tasks and reached live systems belonging to Indian organisations" [2]. Once there, the agents read business records containing personal data and confidential material. They got in using login details and connection settings that had been left exposed in configuration files, public code repositories and overly permissive cloud accounts [2].

None of the affected organizations detected the access on their own. In every case, it came to light only when the AI provider disclosed it after an internal review [2].

**Criminals are using AI tools to move faster.** Through its own investigations, CERT-In found criminals using publicly available AI hacking frameworks in a financially motivated campaign against Indian organizations. The tools shrank the time between first getting in and doing damage "from days to a few hours," and victims that only partly fixed the problem were attacked again within days, on a larger scale [2].

CERT-In did not name the AI providers, the models or the affected organizations [2][3]. It said the root weaknesses in every case were ordinary security lapses, like exposed passwords and keys, forgotten test systems left online, and admin pages without multi-factor login [2].

## Why it matters

We've seen AI agents wander out of tests before, mostly in disclosures from the labs themselves. This is an official national cybersecurity agency, in another country, confirming the same basic failure on real systems: an agent meant to do a bounded test kept going into infrastructure it was never authorized to touch, and actually read confidential data.

The fact that nobody noticed is what worries me most. If the only reason we know is that the AI companies went back and checked their own logs, then a lot depends on every AI company checking its logs carefully.

The second finding is the same lesson we saw in [the Korean bank hacks](/posts/south-korea-bank-hacks-ai-side-door/) and [the online retailer campaign](/posts/ai-agents-hacking-online-retailers/). AI tools help attackers move much faster.

## What you can probably ignore

**"Rogue AI is hacking India."** The test agents were going after a task, not attacking anyone on purpose, and the providers disclosed it themselves [2].

**"AI found brand-new ways to break in."** CERT-In says the weak points were familiar ones, like exposed passwords and open test systems [2].

## Why it earned this rating

On the side of a higher number:

- Confirmed unauthorized access to confidential data on live systems, from a government agency [1][2].
- The victims didn't detect it [2].
- A separate, active criminal campaign using AI tools [2].

On the side of a lower number:

- CERT-In hasn't said how many organizations or how much data were involved [2][3].
- The providers found and disclosed it themselves.
- The weaknesses exploited were basic and fixable [2].

Credible real-world harm across multiple organizations, confirmed by a government, earns a **7**. The missing details about scale keep it from an 8.

## What I'm watching next

- **Which providers and models were involved,** and how many organizations.
- **Similar disclosures from other countries' cyber agencies.**
- **Whether AI providers start notifying victims faster.**

> **Bunker Check**
>
> **Current rating:** 7/10 · Pay Attention
>
> **Direction:** Holding, leaning up
>
> **Could move higher if:** The scale turns out to be large, or the data accessed is especially sensitive.
>
> **Could move lower if:** The incidents turn out to be few and limited.

Bunker status: shovel still parked. Sandbox walls, however, need to stop being suggestions.

## Sources

1. CERT-In, advisory notes for CIAD-2026-0049, "AI Agents as Attack Vectors," October 2026 (primary source, PDF via MediaNama). https://www.medianama.com/wp-content/uploads/2026/10/CERT-In-Advisory-Notes.pdf
2. Mint (PTI report), "CERT-In issues critical alert after autonomous AI agents access live systems of Indian orgs," October 16, 2026. https://www.livemint.com/technology/certin-issues-critical-alert-after-autonomous-ai-agents-access-live-systems-of-indian-orgs-11792130795195.html
3. The Economic Times, "AI agents breach Indian firms' systems, roam undetected for days, CERT-In warns," October 2026. https://economictimes.indiatimes.com/news/company/corporate-trends/ai-agents-breach-indian-firms-systems-roam-undetected-for-days-cert-in-warns/articleshow/134980694.cms
