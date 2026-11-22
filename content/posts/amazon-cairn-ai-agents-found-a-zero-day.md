---
title: Attackers Told Their AI Agents to "Obtain Shell Access." The Agents Found a Brand-New Flaw to Do It.
date: 2026-11-22
rating: 7
slug: amazon-cairn-ai-agents-found-a-zero-day
type: Safety Watch
description: Amazon says a likely China-linked attacker pointed the Cairn AI hacking tool at universities in East Asia, and its agents found a flaw nobody knew about in a medical imaging program, then used it to take full control of a server. A fix exists in the code, but no fixed version has been released yet.
---
*Rating as of November 22, 2026: 7/10 · Pay Attention*

*Until now, the AI-run break-ins I've written about went through doors that were already known to be broken. In this one, the agents found a new door on their own.*

## What changed

On November 20, Amazon published a report on its security blog titled "Chinese-nexus actor's Cairn AI agents found a zero-day on their own," by CJ Moses, the chief information security officer of Amazon Integrated Security [1]. A "zero-day" is a software flaw that nobody, including the people who make the software, knew about yet, so there is no fix waiting to be installed.

Here's what Amazon says happened [1]:

- **How Amazon saw it:** on September 10, Amazon found a copy of Cairn, an open-source AI hacking tool that coordinates several AI agents, running on the open internet with no password. Its history was visible, including the attacker's instructions and what the AI did in response.
- **Who and where:** Amazon assesses "with moderate confidence" that the attacker is linked to China, based on Simplified Chinese instructions, China Standard Time timestamps and the choice of targets: universities in East Asia outside mainland China.
- **How much the person did:** the attacker gave the agents a list of internet addresses and a goal, which Amazon quotes as "obtain shell access" (control of the machine from a command line). The agents then "planned, executed, and adjusted their approach as they learned, without the operator choosing each next step," over a campaign of about 48 hours starting September 8.
- **What didn't work:** against one university's database server, the agents spent about 16 hours and 148 steps trying known tricks and got nowhere. Against another university's computing server, they built about 80 likely usernames from public university pages and tried more than 30,000 password combinations. None worked.
- **What did work:** a target running MONAI Label, an open-source program researchers use to label medical images with AI's help [1][3]. Amazon says the agents worked out what the program was, mapped its features, found a file upload function and tested whether it could be tricked into saving files in the wrong place. It could. "In about 11 minutes, the agents went from mapping the application's API to arbitrarily writing files on the server," Amazon writes. In a later session they used that to plant code that gave them control of the server with full administrator ("root") rights.
- **Was it really new?** Amazon says it assesses "with high confidence" that this was a zero-day, because there was no fix, bug report, advisory or earlier mention of it anywhere [1].
- **What came next:** the attacker then handed the agents a way into a second university's network that ran the same program. Amazon says "we infer" the attacker used the new flaw to get in there, then told the agents to go after other machines on that network [1].

The flaw itself is now public. The MONAI Label project published a security advisory on November 18, rated "Critical," saying the program's upload feature can be tricked into writing files anywhere on the server, which "can lead to remote code execution" [2]. Login protection is "disabled by default," so in the standard setup "any network client that can reach the server can exploit this" [2]. Amazon reported it to the project [1][2]. The advisory lists every version up to 0.8.5 as affected and the patched version as "None": the fix "will be included in the next MONAI Label release" [2]. Until then, the project says to turn on login protection, keep the server off untrusted networks and run it with limited permissions [2].

What's **not** confirmed: Amazon doesn't name the victims or which AI models powered the agents, doesn't say how many organizations were targeted, and doesn't say whether any data was taken [1]. The victims weren't Amazon customers, and Amazon says it worked with "a government partner" to notify them [1]. I couldn't find any statement from the victims. The China link is a moderate-confidence assessment, and the second break-in is Amazon's inference, not something it watched directly.

## Why it matters

Every AI-run break-in I've rated so far had the same reassuring footnote. In [the Unit 42 Cairn campaign](/posts/unit-42-cairn-ai-agents-semiconductor-defense-civil-society/), the agents used weak passwords and old, already-fixed flaws. The same was true, broadly, of [VAPOR PANDA](/posts/vapor-panda-ai-agents-government-ministries/) and [the four groups CrowdStrike found](/posts/crowdstrike-four-groups-ai-agents-ran-break-ins/). The advice was boring and it worked: patch your software, fix your passwords.

This report wears that footnote thin. The agents weren't handed a known weakness. They looked at an unfamiliar program, found one nobody had found before, and used it, in about the time it takes to make a sandwich. We've seen AI do this in the lab: [Anthropic's unreleased model](/posts/anthropic-unreleased-claude-built-working-exploit-chains/) and [a free model attacking Firefox](/posts/free-ai-model-built-working-firefox-attack/) both built working attacks under controlled conditions. This is attackers doing it to real organizations.

Patching still matters. It just can't protect you from a flaw that doesn't have a patch yet, and right now this one doesn't.

For most people, nothing changes at home. If you work at a hospital, university or research lab that runs MONAI Label, it's worth making sure whoever looks after it has read the advisory.

## What you can probably ignore

**"AI is now discovering brand-new ways to hack anything."** It found one flaw, of a well-understood kind (a file upload that doesn't check where files go), in a program that by default doesn't ask for a password [2]. Against two other targets, the same agents spent hours and got nowhere [1].

**"Hackers broke into hospitals and stole patient records."** Amazon describes the targets as universities and a server running a medical imaging research tool. It reports no patient data, and no data taken at all [1].

**"The AI hacked on its own, with nobody behind it."** A person chose the targets, set the goal and handed over the way into the second network [1]. The agents chose how to get there.

## Why it earned this rating

On the side of a higher number:

- AI agents found a previously unknown flaw and used it against real organizations, not in a test [1].
- They went from first look to writing files on the server in about 11 minutes, then got full control [1].
- The person behind it mostly set a goal and a list of targets [1].
- There is still no released fix, and the vulnerable setup is the default one [2].

On the side of a lower number:

- It's one flaw of a simple, well-known type, in a program that's open by default [2].
- The agents spent hours on two other targets and failed [1].
- No data theft is reported, the victims and models aren't named, and the scale is unknown [1].
- It's one company's report, with moderate confidence on who was behind it, though the project's own advisory confirms the flaw [1][2].

I put this at **7**, level with [the Unit 42 Cairn campaign](/posts/unit-42-cairn-ai-agents-semiconductor-defense-civil-society/). It moves past that one in one important way, finding a new flaw instead of using known ones, but Unit 42 documented ten breached organizations and more than a million stolen records, and this has far less confirmed damage. It isn't 8 like [the CrowdStrike groups](/posts/crowdstrike-four-groups-ai-agents-ran-break-ins/) because the harm here is unclear and the flaw was an easy one to find for anyone looking. If you'd put it at 8 because "AI finds new flaws in the wild" is a line that matters more than the size of any one campaign, I think that's a reasonable call, and it's the direction I'd expect this to go.

## What I'm watching next

- **The fixed release.** Whether MONAI Label ships a patched version soon, and whether anyone reports attacks on unpatched servers now that the flaw is public.
- **The victims.** Whether any university confirms what was reached, and whether data was taken.
- **More AI-found zero-days.** A second confirmed case, especially in widely used software or with real damage, would move this to an 8.
- **Which models.** Whether Amazon or others say what AI powered the agents, and whether it was a commercial model that should have refused.
- **Cairn itself.** It keeps turning up in break-ins. Whether its developers add limits, and whether governments say anything about it.

> **Bunker Check**
>
> **Current rating:** 7/10 · Pay Attention
>
> **Direction:** Rising
>
> **Could move higher if:** more AI-found zero-days turn up in real attacks, especially in widely used software, or victims confirm data was taken.
>
> **Could move lower if:** this stays a one-off, the fix ships quickly with no further attacks, and the second break-in turns out not to have used the new flaw.

Bunker status: the shovel stays in the garage. "Install your updates" is still good advice. It's just no longer the whole plan, so the canned goods can stay where they are while the people who run servers have a slightly worse week.

## Sources

1. CJ Moses, Amazon Security Blog, "Chinese-nexus actor's Cairn AI agents found a zero-day on their own," November 20, 2026 (primary source). https://aws.amazon.com/blogs/security/chinese-nexus-actors-cairn-ai-agents-found-a-zero-day-on-their-own/
2. Project MONAI, "Path traversal in datastore upload endpoints allows arbitrary file write," GitHub security advisory GHSA-qc22-rmgc-vg94, November 18, 2026. https://github.com/Project-MONAI/MONAILabel/security/advisories/GHSA-qc22-rmgc-vg94
3. Eduard Kovacs, SecurityWeek, "Amazon: China-Linked Hackers' AI Agents Exploited Medical Software Zero-Day," November 21, 2026. https://www.securityweek.com/amazon-china-linked-hackers-ai-agents-exploited-medical-software-zero-day/
4. BleepingComputer, "Hackers use autonomous AI tool Cairn to find zero-day, take over server," November 20, 2026. https://www.bleepingcomputer.com/news/security/hackers-use-autonomous-ai-tool-cairn-to-find-zero-day-take-over-server/
