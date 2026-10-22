---
title: The Same AI Capability That Can Break Things Can Also Find Them First
date: '2026-10-21'
order: 2
rating: 5
band: Eyebrow Raised
slug: same-ai-capability-that-can-break-things-can-find-them-first
type: Briefing
description: AI-assisted researchers found serious security holes in PHP, the software behind about 70% of websites, and the fixes shipped before the details went public. This is the good side of the cyber story.
---
*Rating as of October 21, 2026: 5/10 · Eyebrow Raised*

*A short one, and for once, mostly good news. Please update your websites, though.*

## What changed

PHP, the programming language running roughly 70% of websites, shipped emergency patches on October 21 for two critical flaws that could let an attacker run code on a server without logging in [2][3][4]. Every PHP version released in the last decade is affected by at least one of them, going back to 5.4, and the worst is rated 9.2 out of 10 for severity [2].

The interesting part is who found them. Two teams got there independently:

- **Calif**, a security firm, found a critical flaw using OpenAI's GPT-5.6 Sol, as part of OpenAI's "Patch the Planet" effort [1].
- **Wiz Research** found and reported both flaws, using its own tools plus Gemini 4 Argon and GPT-5.6 Sol. Wiz says Gemini 4 Argon "made an invaluable contribution" to the find [2].

PHP's maintainers led the fixes, with Wiz, Cloudflare and others helping coordinate and test them before anything was made public [1][2][5]. OpenAI's summary: "To our knowledge, frontier AI found these vulnerabilities before attackers did" [1].

## Why it matters

We've spent a lot of this fall on AI finding holes the wrong way, like [the retailer hacks](/posts/ai-agents-hacking-online-retailers/) and [Gemini's test that hit three real companies](/posts/gemini-hacked-three-companies-during-a-test/). This is the same capability pointed in the right direction. The flaw was found, reported privately, fixed, and announced in the right order. The disclosure process worked.

## What you can probably ignore

**"AI just saved the internet."** People did plenty here too: the PHP maintainers, Wiz, Calif, Cloudflare. AI made the finding faster, and the old-fashioned coordination did the rest.

**"So AI cyber risk is solved."** Nope. Anything defenders can find this way, attackers can eventually find too. That's the whole race.

## Why it earned this rating

A **5** because it's genuinely important (huge reach, very severe flaws) but the news is that it went well. It's a sign of how capable these models have become at real security work, which cuts both ways. If you run a PHP site, patch now: fixed versions are 8.2.35, 8.3.36, 8.4.27 and 8.5.12, and PHP 7 or older needs to be upgraded [3][4].

## What I'm watching next

- **How fast people patch,** and whether attackers start using these flaws once the details are out.
- **Whether "find it first" becomes routine,** with labs and security firms working this way on other widely used software [1].

Bunker status: shovel stays put. Your web host, however, has homework.

## Sources

1. OpenAI, "Patch the Planet: global response coordination as agents uncover critical vulnerabilities," October 21, 2026 (primary source). https://openai.com/index/coordinated-disclosure-of-critical-vulnerabilities
2. Wiz Research, "PHP2Shell: AI uncovers critical RCE vulnerabilities affecting 70% of the Internet," October 21, 2026. https://www.wiz.io/blog/php2shell-php-rce
3. PHP security advisory GHSA-6wmf-4rv5-p3rp, "RCE via stale global state," October 2026 (primary source). https://github.com/php/php-src/security/advisories/GHSA-6wmf-4rv5-p3rp
4. BleepingComputer, "PHP ships emergency patches for critical PHP2Shell flaws," October 21, 2026. https://www.bleepingcomputer.com/news/security/php-ships-emergency-patches-for-critical-php2shell-flaws/
5. Cloudflare, "Cloudflare deploys protections against php2shell vulnerability," October 21, 2026. https://blog.cloudflare.com/php-vulnerabilities-waf-protection/
