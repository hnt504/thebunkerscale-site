---
title: A Second China-Linked Group Ran AI Agents Against 200 Organizations. Nine Were Breached, Including Government Ministries.
date: 2026-10-31
rating: 7
slug: vapor-panda-ai-agents-government-ministries
type: Safety Watch
description: CrowdStrike says a China-nexus hacking group it calls VAPOR PANDA used the ARTEX AI agent tool, mostly powered by DeepSeek, against more than 200 organizations in 11 days. It confirmed break-ins at nine, including a Middle East interior ministry and telecom companies. A person steered the agents at key moments.
---
*Rating as of October 31, 2026: 7/10 · Pay Attention*

*Last week Microsoft said one China-aligned group was using an AI hacking tool at scale. CrowdStrike now says a different one was too, and this time it can name the kinds of places that got breached.*

## What changed

On October 29, CrowdStrike's Counter Adversary Operations team published a report on a hacking group it calls VAPOR PANDA [1]. CrowdStrike counts it among the "China-nexus" groups (its term for hackers tied to China) and says that since 2021 it has mainly gone after government, think tank, energy and natural-resource organizations in Europe, North America, Oceania and the UK [1].

Here's what CrowdStrike says happened [1]:

- **The tool:** ARTEX, the AI agent framework that has now turned up in [the South Korean bank attacks](/posts/artex-ai-hacking-tool-pulled-offline/) and [Microsoft's Storm-0940 report](/posts/storm-0940-artex-connectwise/). CrowdStrike describes it as a main agent that coordinates "planner and worker agents" over a shared map of what they've found. CrowdStrike says this campaign "is separate from" the Storm-0940 activity.
- **The AI behind it:** the group ran ARTEX "primarily with the Chinese-origin DeepSeek" model, plus a second, subscription-based commercial model that CrowdStrike "could not confirm." Neither CrowdStrike nor the press coverage names that second model, and neither says anything about getting past a company's safety controls.
- **The scale:** starting October 17, the group used ARTEX against "more than 200 distinct organizations worldwide" in at least 14 countries over 11 days.
- **The results:** CrowdStrike "confirmed post-exploitation activity at nine organizations," meaning the attackers got in and did things once inside, including installing a backdoor. It saw password-guessing attacks against at least 12 more.
- **Who got hit:** the confirmed cases include an interior ministry in the Middle East, telecom companies in the U.S., Belgium and the Philippines, and a Greek government organization where the attackers got mail and VPN access. CrowdStrike also describes "extensive intrusions" at the foreign ministries of two Latin American countries, and says the group "likely compromised a third" ministry. The target lists also included foreign ministries in Latin America, Europe, Asia and the Middle East and 19 U.S. organizations in pharmaceuticals, semiconductors, defense, nuclear and finance.
- **How deep they got:** in some cases the attackers got an enterprise administrator account (about the highest level of control over an organization's network), full control of production servers, stored administrator passwords, and a forged admin key that let them read mailboxes.

The part that matters most for the "is AI doing this on its own?" question: CrowdStrike says the framework "kept a human in the loop." It recovered transcripts showing an operator typing instructions in Chinese, marked "human instruction," and stepping in "only to steer the agents at decision points." One instruction asked the agents to find Windows machines without CrowdStrike's own security software installed [1].

Some of the most striking numbers come from CrowdStrike's interviews with CyberScoop, not the report itself [2]. CyberScoop reports that 140 of the targets were sensitive, and quotes CrowdStrike saying about 70% of the group's targets were "confirmed compromised or had evidence indicating moderate confidence" of it. It also reports that CrowdStrike saw roughly 45 attacks using AI agents in September, across all the attackers it tracks, and 126 so far in October. And it quotes CrowdStrike's Adam Meyers saying ARTEX could "exceed 1,500 commands an hour," where a person at a keyboard has typically managed up to 40 [2]. Those figures aren't in the published report, so treat them as CrowdStrike's say-so for now.

What's **not** confirmed: CrowdStrike doesn't say what data, if any, was taken. Reading mailboxes is close, but the report doesn't describe files leaving the building [1]. No government has commented that I could find, and neither DeepSeek nor ARTEX's developer is quoted anywhere.

## Why it matters

Earlier this month, the AI-run break-in stories on this site were about criminals [stealing card numbers](/posts/ai-agents-hacking-online-retailers/) and [an unknown attacker hitting Korean banks](/posts/artex-ai-hacking-tool-pulled-offline/). Now there are two separate China-linked groups, named by two different security companies, using the same AI agent tool against governments. That's the "more groups, bigger scale" pattern I said I'd be watching for.

It also shows what AI agents change in practice. VAPOR PANDA isn't new and its targets aren't new. What's new is that a small team can run engagements against a couple of hundred organizations at once, because the agents do the tedious middle part (scanning, trying passwords, writing small tools, mapping networks) while a person decides where to push. CrowdStrike says the planning agents in a single intrusion read through on the order of 1.4 billion words-and-pieces of text (tokens) [1]. No human team reads that much.

And it's worth noticing which AI did most of the work: a Chinese model anyone can download or pay for, not one of the big American lab models with tightening cyber restrictions. [Locking down the strongest models](/posts/anthropic-cyber-verification-guest-list/) helps, but it doesn't stop an attacker from using a different one.

For ordinary people, the effect is indirect. Your phone company or a government office may be cleaning up after this. Nothing here suggests anything about how you use AI at home needs to change.

## What you can probably ignore

**"China's AI is hacking governments on its own now."** CrowdStrike's own transcripts show a person giving the orders and stepping in at the key decisions [1]. The AI made the people faster. It didn't replace them.

**"140 governments were hacked."** That number comes from an interview, it covers "sensitive targets," and CrowdStrike's report confirms nine organizations with hands-on activity inside, not 140 [1][2].

**"DeepSeek is a hacking tool."** It's a general AI model that a hacking framework was plugged into. This group also used a second, unnamed commercial model alongside it [1].

## Why it earned this rating

On the side of a higher number:

- Government ministries and telecom companies were actually breached, with top-level network access and mailboxes read [1].
- It's the second China-linked group in two weeks found using the same AI agent tool against governments (after [Storm-0940](/posts/storm-0940-artex-connectwise/)), and CrowdStrike says the agent-run attacks it sees nearly tripled from September to October [1][2].
- One small team ran attacks against more than 200 organizations at once [1].

On the side of a lower number:

- A person steered the agents at the important moments [1].
- Confirmed break-ins are nine, not hundreds, and data theft isn't confirmed [1].
- CrowdStrike caught it and published ways for other companies to find it [1].
- State-linked spying on foreign ministries isn't new. The speed and scale are.

I put this level with [Microsoft's Storm-0940 report](/posts/storm-0940-artex-connectwise/) at **7**. The confirmed victims here are more specific and more sensitive, which pushes it up. But it's still human-directed, it's the same tool doing the same kind of thing, and nobody has confirmed what was taken. I kept it below [CrowdStrike's four-groups report](/posts/crowdstrike-four-groups-ai-agents-ran-break-ins/) and [the online retailer campaign](/posts/ai-agents-hacking-online-retailers/) at 8: the first showed agents running large parts of break-ins across several unrelated groups and getting past commercial safety controls, and the second had confirmed harm to hundreds of thousands of people. If this one turns into confirmed theft of government secrets, it would join them. You could reasonably argue it already should, and I wouldn't fight you very hard.

## What I'm watching next

- **Whether data was taken** from the ministries and telecom companies, and what kind.
- **A government response:** a CISA advisory, an allied statement naming the group, or a response from China.
- **The unnamed commercial model.** If it turns out to be a major Western lab's model, the question becomes how its safeguards missed this.
- **CrowdStrike's monthly count** of AI agent attacks. If it keeps nearly tripling, that matters more than any single campaign.

> **Bunker Check**
>
> **Current rating:** 7/10 · Pay Attention
>
> **Direction:** Holding, leaning up
>
> **Could move higher if:** data theft from government targets is confirmed, a major lab's model turns out to have done much of the work, or agent-run attacks keep growing at this pace.
>
> **Could move lower if:** the confirmed break-ins stay at a handful, are quickly cleaned up, and no data turns out to have been taken.

Bunker status: the shovel stays in the garage. The canned goods can stay on the shelf too. Somebody at a few foreign ministries is having a much worse weekend than you are.

## Sources

1. CrowdStrike Counter Adversary Operations, "VAPOR PANDA Uses AI-Driven ARTEX to Grow Global Espionage Campaign," October 29, 2026 (primary source). https://www.crowdstrike.com/en-us/blog/vapor-panda-uses-artex-to-scale-global-campaign/
2. CyberScoop, Matt Kapko, "China-backed threat group used agentic AI pentesting tool to compromise 140 sensitive targets in 11 days," October 30, 2026 (includes CrowdStrike's interview figures). https://cyberscoop.com/china-vapor-panda-agentic-ai-artex-campaign-crowdstrike/
