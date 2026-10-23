---
title: Four Separate Hacking Groups Let AI Agents Run Their Break-Ins. CrowdStrike Found the Toolkits.
date: '2026-10-23'
order: 2
rating: 8
slug: crowdstrike-four-groups-ai-agents-ran-break-ins
type: Safety Watch
description: CrowdStrike says four previously unreported hacking groups handed large parts of real intrusions to AI agents, hitting healthcare organizations in Argentina, government sites in several countries and a U.S. software company. All four got past commercial AI safety controls.
---
*Rating as of October 23, 2026: 8/10 · Pay Attention*

*One criminal using AI agents was a warning. Four unrelated groups doing it, speaking four different languages, looks more like a trend.*

## What changed

On October 21, the security company CrowdStrike published research on four hacking groups it hadn't reported on before, all of which used AI agents to carry out real intrusions between May and August 2026 [1]. (An AI agent here means an AI model hooked up to tools, so it can run commands and take steps on its own instead of only answering questions.) Each group left its agent toolkit sitting in an open, unprotected folder on the internet, which is how CrowdStrike got a close look at how they worked [1].

According to CrowdStrike [1]:

- **Threat Actor 1** (Spanish and English speaking) compromised at least 15 healthcare organizations in Argentina and took credentials and medical records from at least one of them. It ran a setup where one Claude Code agent acted as a "Supervisor" picking tasks and another acted as the "Executor" carrying them out.
- **Threat Actor 2** (Chinese speaking) had more than 20 named targets around the world, compromised government organizations in two countries, and went after companies in Brazil and the U.S. It reached Claude mainly through a China-based proxy service.
- **Threat Actor 3** (Indonesian speaking) was the least sophisticated. It loaded 819 mostly public "skills" from GitHub into Claude Code and let it run, compromising several Indonesian government websites, one government site in another country and several companies. This group "periodically had to intervene" to get past the model's safety guardrails or keep it going.
- **Threat Actor 4** (Russian speaking) took corporate client data from a U.S. company that makes customer-management software, and broke into several software and data center companies in Russia, Kyrgyzstan and the U.S. Its whole workflow started with a single command, and CrowdStrike says it gave the agent "near-total autonomy in selecting exploitation methods."

CrowdStrike's summary is that attackers are now "delegating operational decision-making across the kill chain to agentic AI" (the "kill chain" is the sequence of steps in an attack, from scouting to stealing) [1]. Its report page adds that in one case an agent moved through a victim's network and collected domain controller credentials (roughly, the master keys to an organization's computers) in about 20 minutes, "without additional human guidance" [2]. It doesn't say which group that was. CrowdStrike also says all four groups got around commercial AI safety controls [2].

What CrowdStrike does **not** say is just as important. It doesn't name the four groups, the victims, or how much data was taken beyond the two cases above [1]. I couldn't find a public response from Anthropic, whose Claude Code shows up in all four toolkits [1].

**Is this the first time?** No, and it's worth being precise here. In November 2025, Anthropic disclosed a campaign it attributed to Chinese state-sponsored hackers who jailbroke Claude Code, and said the AI carried out 80 to 90% of that operation itself [3]. And in September, [a single attacker used AI agents against hundreds of online retailers](/posts/ai-agents-hacking-online-retailers/) [4]. What's new is the pattern: four unrelated groups, documented by an independent security firm, with confirmed victims.

## Why it matters

This is the thing that turns a handful of alarming stories into a trend. When I rated the retailer campaign an 8, I said it could go higher if "several independent groups are found running similar AI-driven campaigns." This is that, or at least the start of it.

The most worrying detail is the least sophisticated group. Threat Actor 3 mostly downloaded free tools from GitHub and pointed an AI at government websites, and it worked [1]. CrowdStrike thinks it's "likely" that over the next year agentic AI will let low-skill attackers operate at levels that used to take organized crime or a government [1]. That's a prediction, not a finding, but the Indonesian case is a real example of it.

There's a hopeful mirror image, too. The same week, AI-assisted researchers [found critical holes in PHP before attackers did](/posts/same-ai-capability-that-can-break-things-can-find-them-first/). The capability is the same on both sides. It's a race, and defenders are in it.

For ordinary people, the effect is indirect but real: healthcare providers, governments and software companies that hold your information are facing attackers who can move faster and try more doors. You don't need to do anything differently today, beyond the usual: turn on two-factor sign-in and be suspicious of unexpected messages asking you to log in.

## What you can probably ignore

**"AI has started hacking the internet on its own."** People built these toolkits, picked the targets and pressed go [1]. The AI made many of the decisions inside each break-in, which is new and serious, but nobody here was attacked by a machine acting on its own wishes.

**"AI is an unstoppable hacker now."** CrowdStrike found all four groups, partly because they left their toolkits out in the open [1]. One group's AI kept stalling and needed a human to nudge it along [1]. Fast and tireless isn't the same as unstoppable.

**"Claude is a hacking tool."** All four groups used Claude Code, and all four got around its safeguards, which is a real problem for Anthropic [1][2]. But these groups worked around the rules (one through a proxy service, another by repeatedly intervening), and the same kind of tool is what defenders are using to find bugs first.

## Why it earned this rating

On the side of a higher number:

- Four unrelated groups, independently documented by a major security firm [1].
- Real victims, including healthcare organizations, with medical records and corporate client data taken [1].
- An agent reaching an organization's master keys in about 20 minutes without more human help [2].
- A low-skill group succeeding mostly with free public tools [1].
- Commercial AI safety controls failed to stop any of the four [2].

On the side of a lower number:

- People still chose the targets, built the toolkits and launched the campaigns [1].
- The activity is from May to August and was caught; it isn't a fast-moving crisis today [1].
- Confirmed data theft is limited to two cases, and the scale is dozens of victims, not millions [1].
- AI doing most of a real attack was first documented almost a year ago [3].

I landed on an **8**, the same as the [retailer campaign](/posts/ai-agents-hacking-online-retailers/), because the harm here is confirmed and the pattern now spans several independent groups. I stopped short of a 9 because 9 is for a major escalation with serious practical consequences, and the confirmed damage here is still fairly contained. If these toolkits start showing up at larger scale, or start disrupting critical services like healthcare, that changes.

## What I'm watching next

- **Anthropic's response,** since Claude Code appears in all four toolkits, and whether it changes its safeguards.
- **The names and the victims.** Whether any of the affected healthcare organizations, governments or the U.S. software company confirm what was taken.
- **More groups.** Whether other security firms report similar agent-run campaigns, especially at larger scale.
- **The 20-minute case,** and which group it belonged to.

> **Bunker Check**
>
> **Current rating:** 8/10 · Pay Attention
>
> **Direction:** Rising
>
> **Could move higher if:** agent-run campaigns show up at much larger scale, cause serious harm to critical services, or keep getting past AI safety controls after labs respond.
>
> **Could move lower if:** labs close the gaps these groups used and the confirmed damage stays limited to a few cases.

Bunker status: the shovel stays in the garage. Two-factor sign-in, however, is officially non-negotiable.

## Sources

1. CrowdStrike, "CrowdStrike Uncovers New Agentic AI Campaigns," October 21, 2026 (primary source). https://www.crowdstrike.com/en-us/blog/crowdstrike-uncovers-new-agentic-ai-campaigns/
2. CrowdStrike, "CrowdStrike Counter Adversary Operations Uncovers New 2026 Agentic AI Campaigns" (report page, includes the 20-minute case and the safety-controls finding). https://www.crowdstrike.com/en-us/resources/reports/agentic-ai-attack-campaigns/
3. Axios, "Chinese hackers used Anthropic's AI agent to automate spying," November 13, 2025. https://www.axios.com/2025/11/13/anthropic-china-claude-code-cyberattack
4. Gambit Security, "Autonomous AI Agents are breaking into hundreds of Online Retailers for $25 a target in an ongoing campaign," September 22, 2026. https://gambit.security/blog-posts/autonomous-ai-agents-online-retailers-25-a-company
