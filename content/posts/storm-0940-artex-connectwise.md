---
title: The AI Hacking Tool Was Pulled Offline. Microsoft Says a China-Aligned Group Used It Anyway.
date: '2026-10-23'
order: 1
rating: 7
slug: storm-0940-artex-connectwise
type: Safety Watch
description: Microsoft says a China-aligned hacking group used ARTEX, the open-source AI hacking tool from the South Korean bank attacks, to go after hundreds of organizations through a compromised ConnectWise backup service. Most attempts failed, but some reached privileged access in under three hours.
---
*Rating as of October 23, 2026: 7/10 · Pay Attention*

*Two weeks ago the AI hacking tool behind the Korean bank attacks went closed-source. Microsoft now says a state-aligned group was already using it on a much bigger scale.*

## What changed

On October 21, Microsoft's threat intelligence team published a report on a hacking group it calls Storm-0940 [1]. Microsoft describes the group as "China-state aligned," active since 2021, and focused on stealing data [1]. Microsoft "assesses" that Storm-0940 was behind the ConnectWise supply chain compromise that surfaced in mid-October [1]. (A supply chain attack is when attackers break into a company that other businesses rely on, and use that trusted connection to get to its customers.)

Here's the short version of what Microsoft says happened [1]:

- **The tool:** ARTEX, the same open-source AI penetration testing framework that turned up in [the South Korean bank attacks](/posts/artex-ai-hacking-tool-pulled-offline/). Microsoft describes it as able to run "an autonomous penetration test from reconnaissance through data exfiltration with little needed human interaction." It "can use any AI model," and Microsoft doesn't say which ones were used here.
- **The way in:** attackers got hold of credentials for ConnectWise Cloud Backup, a service that IT companies use to back up their clients' Microsoft 365 accounts. Because that app was already trusted, the attackers could sign in to customers' environments without any user logging in [1][3]. Microsoft doesn't say how ConnectWise itself was first breached.
- **The scale:** Microsoft says the group used ARTEX "to attempt to sign-in to more than 2,250 tenants" (a tenant is one organization's Microsoft 365 setup), and targeted hundreds of organizations around the world in government, aerospace and defense, financial services and other sectors [1][2].
- **The speed:** in "multiple instances," the time from first targeting to privileged access "was less than 3 hours" [1]. One chart in the report shows more than 200 sign-ins in under four minutes [1].
- **The results:** Microsoft says "the majority of the targeting wasn't successful," but that the group still "achieved privileged cloud persistence at many organizations in a brief time" [1]. In plain English, at a number of organizations the attackers got high-level access and set things up so they could keep it.

What's **not** confirmed matters just as much. Microsoft doesn't give a count of organizations that were actually compromised, and it says an affected app or a successful sign-in "does not necessarily indicate that customer data was accessed or exfiltrated" [1]. ConnectWise said it had "no indicators to date" that its customers' backup data was compromised [3]. The security firm Huntress said it found at least 162 compromised tenants among the customers it watches, according to BleepingComputer [3]. Microsoft also says this "did not result from a compromise of or a vulnerability in Microsoft corporate systems, products, or services" [1].

China's Foreign Ministry denied any knowledge of the incidents, according to The Record [2]. The Record also reports that the security firm Zscaler published its own research the same day finding ARTEX-linked attacks well beyond South Korea, across dozens of industries in several countries [2]. I haven't been able to open Zscaler's report itself, so treat that part as secondhand.

ConnectWise shut down its Cloud Backup and several related services while it investigated, and Microsoft is telling customers to keep the affected ConnectWise connections disabled until ConnectWise says otherwise [1][3].

## Why it matters

When ARTEX's developer [took the tool closed-source](/posts/artex-ai-hacking-tool-pulled-offline/) on October 8, I wrote that it was the right instinct but that copies already downloaded "don't disappear." This is what that looks like. Microsoft says ARTEX-enabled activity started "as early as September 2026," before the tool was pulled, and that threat actors in multiple regions are using it [1].

It also changes who we're talking about. CrowdStrike assessed the Korean bank attacker as likely financially motivated and didn't tie them to any government or named group [4]. This is, by Microsoft's assessment, a state-aligned group going after governments and defense companies, and it used the AI tool the way a business would use automation: to try many doors at once, around the clock. Microsoft's own words are that agentic AI "allows them to scale their operations exponentially" [1].

For most people, the practical effect is indirect. If your employer or your town's IT provider used ConnectWise Cloud Backup, their security team has some cleanup to do. You don't need to change anything about how you use AI at home.

## What you can probably ignore

**"AI hacked Microsoft."** Microsoft says its own systems weren't compromised and none of its products had a flaw that was used [1]. The attackers came in through a trusted backup app at a different company.

**"AI is now running China's hacking operations on autopilot."** Microsoft says ARTEX can work with "little needed human interaction," but it doesn't say how much the people behind it directed this campaign [1]. Someone still chose the targets and the backup service to go after. The attribution is Microsoft's assessment, and China denies it [1][2].

**"Pulling ARTEX offline was pointless."** It didn't undo copies people already had, which is the problem here. It does stop new public versions, and Microsoft has now published detections and hunting guidance for exactly this kind of activity [1].

## Why it earned this rating

On the side of a higher number:

- A state-aligned group, not one person, using an AI agent tool against government, defense and financial targets [1][2].
- Real scale: more than 2,250 tenants targeted, and privileged access at "many organizations" [1].
- Speed: under three hours from first targeting to privileged access in multiple cases [1].
- It shows that AI hacking tools stay in circulation after their creators try to pull them back.

On the side of a lower number:

- Most of the attempts failed, and no theft of data has been confirmed [1][3].
- People directed the campaign, and the way into ConnectWise in the first place isn't explained.
- Microsoft, ConnectWise and other security firms caught it, shut the access down and published ways to find it [1][3].
- State-backed groups using AI to speed up attacks isn't brand new. What's new is the scale and the off-the-shelf tool.

That puts it level with my other big real-world AI attack ratings, [the Korean bank attacks](/posts/south-korea-bank-hacks-ai-side-door/) and [the ARTEX follow-up](/posts/artex-ai-hacking-tool-pulled-offline/), both at **7**. I kept it below [the online retailer campaign](/posts/ai-agents-hacking-online-retailers/) at 8 because there, the harm was confirmed: more than 600,000 stolen card records [5]. Here, the harm is still mostly unknown. If that changes, so does this number.

## What I'm watching next

- **Whether data was actually stolen,** and from whom. Microsoft notes Storm-0940 has used this kind of access to read email in the past [1].
- **ConnectWise's explanation** of how its backup service was breached in the first place.
- **A government response,** such as a CISA advisory or allied statement naming the group.
- **Other groups using ARTEX,** since Microsoft says actors in multiple regions already are [1].

> **Bunker Check**
>
> **Current rating:** 7/10 · Pay Attention
>
> **Direction:** Holding, leaning up
>
> **Could move higher if:** investigators confirm sensitive data was stolen from government or defense targets, or more state-backed groups are found running AI agent tools at this scale.
>
> **Could move lower if:** the confirmed compromises turn out to be few and quickly contained, with no data taken.

Bunker status: the shovel stays in the garage. Your company's IT team, however, may be having a long week.

## Sources

1. Microsoft Threat Intelligence, "AI-driven, large-scale nation-state campaign using ARTEX enables supply chain compromise," October 21, 2026 (primary source). https://www.microsoft.com/en-us/security/blog/2026/10/21/storm-0940-uses-artex-agentic-ai-connectwise-supply-chain-compromise/
2. The Record, "Microsoft blames ConnectWise attacks on Chinese state hacker using ARTEX AI agents," October 22, 2026 (includes the Chinese Foreign Ministry denial and Zscaler's findings). https://therecord.media/china-cyber-connectwise-ai
3. BleepingComputer, Ionut Ilascu, "Hackers breach Microsoft 365 tenants via ConnectWise supply-chain attack," October 17, 2026 (includes ConnectWise's statements and Huntress's tenant count). https://www.bleepingcomputer.com/news/security/hackers-breach-microsoft-365-tenants-via-connectwise-supply-chain-attack/
4. CrowdStrike, "Unknown Threat Actor Uses AI-Driven ARTEX to Target South Korean Finance," October 7, 2026. https://www.crowdstrike.com/en-us/blog/unknown-threat-actor-uses-artex-to-target-south-korean-finance/
5. Gambit Security, "Autonomous AI Agents are breaking into hundreds of Online Retailers for $25 a target in an ongoing campaign," September 22, 2026. https://gambit.security/blog-posts/autonomous-ai-agents-online-retailers-25-a-company
