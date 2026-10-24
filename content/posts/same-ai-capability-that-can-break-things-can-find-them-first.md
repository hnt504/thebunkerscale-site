---
title: The Same AI Capability That Can Break Things Can Also Find Them First
date: '2026-10-21'
order: 2
rating: 6
rating_history:
  - date: 2026-10-21
    rating: 5
    note: Original rating. AI found critical PHP flaws and the fixes appeared to ship before attackers had them.
  - date: 2026-10-24
    rating: 6
    note: The disclosure leaked. Amazon saw exploit attempts four days before the patches, attempts hit the millions, and governments took sites offline. No confirmed break-ins yet.
band: Eyebrow Raised
slug: same-ai-capability-that-can-break-things-can-find-them-first
type: Briefing
description: AI-assisted researchers found serious security holes in PHP, the software behind about 70% of websites. The fixes shipped, but the secret leaked first, and attackers started trying the flaws days before the patches. No confirmed break-ins so far.
---
*Rating as of October 24, 2026: 6/10 · Eyebrow Raised*

*I first called this mostly good news. Then the secret got out early. Please update your websites, and this time I mean it more.*

## What changed

**Update, October 24, 2026:** The "found it first" part of this story did not hold up as well as it looked on October 21. Amazon says its honeypots (decoy servers set up to attract attackers) logged an attempt to exploit these flaws on October 17, four days before the patches, while the details were still supposed to be secret. Amazon says it is unclear how the attacker got the information [6][7]. The flaws' identifiers started circulating on online forums on October 20, and TechTarget reports that Calif, one of the firms that found the bugs, accidentally published a video of the exploit, which was deleted but copied widely [8]. The PHP project moved its release up from October 22 to October 21, and the PHP Foundation says a security vendor, Chainguard, put out patched builds hours before the agreed time, so "any attacker could now study the fix" while everyone else waited [8].

After that, it got loud. Cloudflare's CEO said exploit attempts went from thousands in the 10 hours before the announcement to millions afterward [6][8]. The UK's National Cyber Security Centre told organizations to update immediately, or consider taking affected systems offline, and several UK council sites and the Metropolitan Police site went down [9]. Government sites in the Netherlands, Germany, Belgium and France were also taken offline as a precaution [8].

The calming part, and it matters: as of October 23, no successful break-in had been confirmed. Several security firms say the exploits being sprayed around mostly don't work on normal settings, an attempt to install botnet malware (software that enlists hacked machines into a network attackers control) was stopped, and one firm that tested about 57 servers found none had been exploited [10]. One security company, VulnCheck, says it has built an exploit that does work in common setups, but it is only sharing it with paying customers [10]. And a lot of servers are still exposed: one count found only about 199,000 PHP instances patched within 12 hours, with roughly 71% of those it sampled on versions old enough to get no official fix [10].

*Original post, October 21:*

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

**Update, October 24:** I'm moving this from a **5** to a **6**. The flaws were found with AI help, as I said, but the safe, orderly handoff I praised didn't happen the way it looked: attackers were trying the bugs before the patches existed, and governments switched sites off to be safe [6][8][9]. I'm stopping at 6 rather than 7 because nobody has confirmed a single successful break-in, and most of the exploits going around reportedly fail [10]. If confirmed compromises start showing up, especially at scale, this goes higher.

*Original reasoning, October 21:*

A **5** because it's genuinely important (huge reach, very severe flaws) but the news is that it went well. It's a sign of how capable these models have become at real security work, which cuts both ways. If you run a PHP site, patch now: fixed versions are 8.2.35, 8.3.36, 8.4.27 and 8.5.12, and PHP 7 or older needs to be upgraded [3][4].

## What I'm watching next

- **How fast people patch,** and whether attackers start using these flaws once the details are out. (Update: they started trying before the details were out [6][7].)
- **Confirmed break-ins.** So far there are attempts, not confirmed compromises [10]. That's the line between a 6 and something higher.
- **A working public exploit.** If a reliable exploit like the one VulnCheck describes gets out, the many unpatched and out-of-date servers become a much bigger problem [10].
- **How the leak happened.** Amazon doesn't know how the first attacker got the details early [6][7]. If AI-found bugs keep leaking before the fixes are ready, "find it first" stops being much of an advantage.
- **Whether "find it first" becomes routine,** with labs and security firms working this way on other widely used software [1].

> **Bunker Check**
>
> **Current rating:** 6/10 · Eyebrow Raised
>
> **Direction:** Rising
>
> **Could move higher if:** confirmed break-ins show up, especially at scale or at government or critical services, or a reliable exploit goes public.
>
> **Could move lower if:** the attempts keep failing, patching catches up, and no confirmed compromises appear.

Bunker status: shovel stays put. Your web host's homework is now overdue.

## Sources

1. OpenAI, "Patch the Planet: global response coordination as agents uncover critical vulnerabilities," October 21, 2026 (primary source). https://openai.com/index/coordinated-disclosure-of-critical-vulnerabilities
2. Wiz Research, "PHP2Shell: AI uncovers critical RCE vulnerabilities affecting 70% of the Internet," October 21, 2026. https://www.wiz.io/blog/php2shell-php-rce
3. PHP security advisory GHSA-6wmf-4rv5-p3rp, "RCE via stale global state," October 2026 (primary source). https://github.com/php/php-src/security/advisories/GHSA-6wmf-4rv5-p3rp
4. BleepingComputer, "PHP ships emergency patches for critical PHP2Shell flaws," October 21, 2026. https://www.bleepingcomputer.com/news/security/php-ships-emergency-patches-for-critical-php2shell-flaws/
5. Cloudflare, "Cloudflare deploys protections against php2shell vulnerability," October 21, 2026. https://blog.cloudflare.com/php-vulnerabilities-waf-protection/
6. SecurityWeek, "PHP2Shell Exploitation Started Days Before Patches," October 22, 2026 (reporting Amazon Threat Intelligence's findings). https://www.securityweek.com/php2shell-exploitation-started-days-before-patches/
7. The Register, "Hackers pile on PHP2Shell as AWS reveals attacks began before disclosure," October 22, 2026. https://www.theregister.com/cyber-crime/2026/10/22/hackers-pile-on-php2shell-as-aws-reveals-attacks-began-before-disclosure/5304749
8. TechTarget, "PHP2Shell disclosure unravels after leaks forced early patch drop," October 22, 2026. https://www.techtarget.com/cybersecurity/news/366652613/PHP2Shell-disclosure-unravels-after-leaks-forced-early-patch-drop
9. Insurance Business, "UK councils and Met Police among sites pulled offline after NCSC alert," October 21, 2026. https://www.insurancebusinessmag.com/uk/news/cyber/uk-councils-and-met-police-among-sites-pulled-offline-after-ncsc-alert-594424.aspx
10. SecurityWeek, "Mirai Botnet Operators Join PHP2Shell Attacks as ASLR Bypass Exploits Emerge," October 23, 2026. https://www.securityweek.com/mirai-botnet-operators-join-php2shell-attacks-as-aslr-bypass-exploits-emerge/
