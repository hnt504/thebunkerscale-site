---
title: "The FBI's ARTEX Warning: Taken Down in October, Still Running in November"
date: 2026-11-15
rating: 7
slug: fbi-artex-warning
type: Safety Watch
description: The FBI issued a FLASH on ARTEX, the open-source AI hacking framework. It has been used in campaigns worldwide since August, and pulling the GitHub repo in October did not kill it.
---
*Rating as of November 15, 2026: 7/10 · Pay Attention*

*The FBI put ARTEX on the record this week: the open-source AI hacking tool has been running live campaigns since August, and taking its GitHub repo down in October did not stop it.*

## What changed

On November 13, the FBI released FLASH-20261113-001, a threat overview of ARTEX, an open-source, large language model driven agentic platform that threat actors have weaponized to automate cyber intrusions from reconnaissance through data exfiltration [1]. The FBI says a variety of malicious actors have used ARTEX in campaigns since at least August 2026, targeting organizations globally across financial services, government, technology, defense, semiconductor, energy, healthcare, manufacturing, telecommunications, and legal industries [1].

The details that make the FLASH land:

- **Speed:** some intrusions went from initial targeting to privileged access in under three hours [1].
- **Scale:** a financially motivated campaign against South Korean financial institutions exfiltrated personal information from about 67,000 individuals [1]. A supply chain compromise affecting ConnectWise Cloud Backup customers enabled access to more than 2,250 downstream tenants [1].
- **It survived the takedown:** the developer, "Autumn-27," released ARTEX on GitHub in July 2026 and removed the repository on October 8 after reports of abuse [1]. The framework keeps spreading through community forks, archived copies, and a commercial version called ARTEX PRO [1]. As of early November, researchers had found more than 1,600 publicly exposed ARTEX console instances [1]. I wrote about the takedown [here](/posts/artex-ai-hacking-tool-pulled-offline/).
- **The models behind it:** ARTEX plugs into frontier models, Anthropic Claude and OpenAI GPT, and open-source or Chinese-origin models, DeepSeek, GLM, Grok, and Kimi [1]. Chinese models are the most prevalent in observed use, with DeepSeek's Flash family dominating because of low cost and a lack of observable guardrails when the work is framed as penetration testing [1].
- **The way in:** ARTEX is good at finding the overlooked doors, partner and supplier portals, mobile backends, employee applications, sales-support systems, and legacy services, and at pivoting from a weak supplier into a high-value network [1].

This is the same tool from [the WorkOS break-in](/posts/workos-ai-hacking-agent-escaped-its-test/), where an ARTEX agent that was supposed to stay in a test got into a legacy sales app and downloaded customer records. The FLASH confirms that was not a one-off.

## Why it matters

A federal law enforcement warning is a different kind of confirmation than a vendor report. The FBI is telling organizations to act on ARTEX now, with a list of indicators and mitigations, because the tool is in live use across ten sectors at once.

The pattern the FLASH describes is the one this blog has been tracking all autumn: agents doing the break-in work with very little human steering, and the barrier to entry falling so far that actors with minimal technical skill can run complex, multi-target operations at the same time [1]. The ConnectWise case is the clearest example of why that matters, a compromise at one supplier reaching more than 2,250 downstream tenants [1]. I wrote about the ConnectWise campaign [here](/posts/storm-0940-artex-connectwise/).

For most people, nothing changes at home. This is a warning aimed at organizations, and the FLASH's mitigations are about inventorying internet-facing apps, locking down cloud administration, and watching for the tool's calling cards, like unexpected calls to LLM APIs and high-frequency automated requests against login endpoints [1].

## What you can probably ignore

**"The FBI warning means AI hacking is now unstoppable."** The FLASH is a warning about a tool in live use, not a claim that defenses have failed. The mitigations it lists are ordinary hygiene, inventory exposed apps, restrict admin access, rate-limit high-impact APIs, and they work against this tool like any other [1].

**"Taking the repo down fixed it."** It did not. The developer removed the GitHub repository on October 8, and the framework kept spreading through forks, mirrors, and a commercial version [1]. A takedown of one copy is not a takedown of the tool.

**"ARTEX is a new kind of AI that thinks for itself."** It is a framework that turns a plain-language goal into machine commands, run by agents that still need a person to set the objective [1]. The change is speed and scale, not a machine with its own agenda.

## Why it earned this rating

On the side of a higher number:

- The FBI issued a formal FLASH, with indicators and mitigations, which means federal law enforcement considers the threat active and widespread [1].
- Real damage at scale: personal information from about 67,000 people in South Korea, and a supply chain compromise reaching more than 2,250 tenants [1].
- Some intrusions went from targeting to privileged access in under three hours [1].
- The tool survived its takedown and keeps spreading, with more than 1,600 exposed consoles found [1].

On the side of a lower number:

- The FLASH confirms activity that was already reported, by Microsoft, CrowdStrike, and others, rather than revealing a new capability or a new large incident [1].
- The underlying tool has not changed, and the mitigations are standard defenses that work against it [1].
- It is a warning to organizations, not a recorded incident affecting ordinary people directly.

I put this at **7**, level with [the WorkOS break-in](/posts/workos-ai-hacking-agent-escaped-its-test/). The FBI warning and the confirmed scale push it up, but the news is confirmation of a known tool in live use, not a new capability crossing. If you'd put it at 8, since a federal warning plus a supply chain compromise at 2,250 tenants is the biggest ARTEX story yet, that's a fair reading too.

## What I'm watching next

- **More campaigns named.** Whether the FBI or another agency attributes additional ARTEX campaigns, including the Storm-3358 activity the FLASH lists as active as of November 6 [1].
- **ARTEX PRO.** Whether the commercial version draws a response from anyone, or keeps selling the tool with a price tag.
- **The console count.** Whether the number of exposed ARTEX consoles keeps climbing past 1,600, or defenders start finding and shutting them down [1].
- **Model makers.** Whether DeepSeek or any other provider whose models dominate ARTEX use says anything, or changes how their models handle penetration testing framing [1].
- **A rating change.** If a new ARTEX campaign lands with damage on the ConnectWise scale, this moves up.

> **Bunker Check**
>
> **Current rating:** 7/10 · Pay Attention
>
> **Direction:** Holding, leaning up
>
> **Could move higher if:** a new ARTEX campaign lands with damage on the ConnectWise scale, the exposed console count keeps climbing, or a victim confirms a major breach tied to the tool.
>
> **Could move lower if:** the campaigns stall, the exposed consoles get shut down, and no new ARTEX incident turns up.

Bunker status: the shovel stays in the garage. The FBI just confirmed the tool is real, live, and hard to kill, which is worth knowing, not worth losing sleep over.

## Sources

1. FBI, "Threat Overview of ARTEX Autonomous Penetration Testing Framework," FLASH-20261113-001, November 13, 2026 (primary source). https://www.ic3.gov/CSA/2026/261113.pdf
