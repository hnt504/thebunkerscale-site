---
title: 'The AI Is Getting Too Good at Finding Security Holes. So Anthropic Built a Guest List.'
date: 2026-10-07
rating: 5
band: Eyebrow Raised
slug: anthropic-cyber-verification-guest-list
type: Safety Watch
description: 'Anthropic expanded a vetted program that gives security teams its strongest models with fewer cyber restrictions, in three tiers. Its partners found at least 129,000 verified software vulnerabilities in four months. Access to full AI cyber ability is starting to look like credentialed entry.'
---

*Rating as of October 7, 2026: 5/10 · Eyebrow Raised*

*The interesting part isn't that AI can find bugs. It's that getting its full ability now looks less like downloading software and more like getting a security clearance.*

## What changed

Anthropic expanded its Cyber Verification Program, which gives vetted security professionals access to its most capable models with fewer cyber restrictions [1]. Reuters reported the change [2].

The reasoning, in Anthropic's words: cybersecurity is "inherently dual use," because the same ability that helps a security team find and fix a weakness can help an attacker exploit it [1]. So Anthropic's regular models block most cyber work, and the program is the way for defenders to get past those blocks.

There are now three tiers [1]:

- **Defense Access**, for defensive work like responding to incidents and analyzing malware. Anthropic expects many organizations to qualify, from company security teams to regional hospitals and small utilities.
- **Red Team Access**, which adds authorized penetration testing. Even here, actions that could cause physical harm or mass disruption, like deploying ransomware, are still blocked in real time.
- **Specialized Access**, with the fewest blocks, for a small set of organizations authorized to test systems like flight operating systems, power grids, telecom networks and bank transfer infrastructure. Anthropic says it reviews each of these "in depth in collaboration with the US government."

The capability numbers behind this are big. Anthropic says partners in its earlier program found at least 129,000 verified software vulnerabilities between April and July 2026, and its own scanning of open-source software found another 5,500 [1]. Over 33,000 were rated critical or high severity [2].

## Why it matters

"AI might someday be good at hacking" is no longer the question. Finding tens of thousands of serious software flaws in a few months is industrial-scale work, and it is happening now.

That creates a real dilemma. If the public versions are locked down, defenders fall behind attackers who use other tools. If they're wide open, attackers get the same help. Anthropic's answer is a tiered guest list: the more dangerous the ability, the more vetting you need. Google is doing something similar with [Gemini 4 Argon](/posts/google-gemini-4-argon-restricted-launch/). It looks like this is becoming the standard way to release powerful cyber capability.

## What you can probably ignore

**"Anthropic is handing hacking AI to anyone who asks."** Every tier requires verification, and the highest tier is reviewed with the US government [1].

**"129,000 vulnerabilities means software is hopelessly broken."** These were found so they could be fixed. That's the point of the program.

## Why it earned this rating

On the side of a higher number:

- The capability evidence is substantial [1][2].
- Reduced-safeguard access is expanding to more organizations [1].

On the side of a lower number:

- No new attack, breach or misbehavior is involved.
- This is mainly a defensive program with layered vetting [1].

A meaningful change in how powerful capability is handed out, with safeguards and no harm, is a **5**.

## What I'm watching next

- **Leaks or misuse** of reduced-safeguard access.
- **How strict the vetting really is** as the program grows.
- **Whether the vulnerabilities actually get fixed,** and how fast.

> **Bunker Check**
>
> **Current rating:** 5/10 · Eyebrow Raised
>
> **Direction:** Holding
>
> **Could move higher if:** Reduced-safeguard access is abused, or the vetting turns out to be weak.
>
> **Could move lower if:** The program keeps running cleanly and measurably improves defense.

No shovel. The velvet rope now comes with a security clearance, apparently.

## Sources

1. Anthropic, "Expanding the Cyber Verification Program," October 2026 (primary source). https://www.anthropic.com/news/cyber-verification-program
2. Reuters (via Yahoo Tech), "Anthropic opens its most powerful AI models to more security teams," October 6, 2026. https://tech.yahoo.com/ai/claude/articles/anthropic-opens-most-powerful-ai-190324449.html
