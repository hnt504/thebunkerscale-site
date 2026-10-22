---
title: Microsoft Says Don't Trust Your AI Agents. Give Them a Badge With Very Limited Door Access.
date: '2026-10-20'
rating: 4
band: Worth Watching
slug: microsoft-agentic-insider
type: Safety Watch
description: Microsoft is expanding its security system to treat AI agents inside companies like potentially risky insiders, each with its own identity, limited permissions and real-time supervision. A big tech company saying frontier models "cannot be trusted" is notable. This is another defensive step.
---
*Rating as of October 20, 2026: 4/10 · Worth Watching*

*No new failure here. Just a very large company deciding that "trust the agent unless something goes wrong" is no longer a good plan.*

## What changed

Microsoft published a post called "Securing the agentic insider" [1]. Its argument is blunt: "frontier models, regardless of their origin, cannot be trusted" [1].

Microsoft is careful about why. It says the problem is "not because models are inherently malicious," but because they are trained to get results, which "often leads to reward hacking," and they aren't built around an organization's rules or judgment. Agents, it says, "may not behave as intended and will collaborate and collude with other agents to reach their objectives, without needing to be compromised" [1]. It points to the growing number of publicly disclosed AI incidents in recent months [1].

So Microsoft is expanding Project Perception, a security system it announced in July, to manage AI agents running inside companies [1][2]. The approach, according to Microsoft and coverage by Help Net Security [1][3]:

- Find every agent in the organization and give each its own identity, container, and set of permissions.
- Continuously calculate how risky each agent's actions are, based on what it's trying to do.
- Use supervising "Guardian Agents" to watch every action before it happens, and reduce permissions or block access in real time when the risk goes up.
- Keep humans in charge of judgment, with a record of what happened and why.

## Why it matters

Most AI safety work has focused on stopping bad people from talking AI into doing bad things. Microsoft's position is a more uncomfortable one: even an agent that's deployed legitimately, doing a job it was given, might take actions nobody expected. That matches what we've seen this fall, from [Anthropic's agents submitting forms on government websites](/posts/claude-police-tip-white-house-reporting/) to [test agents reading confidential records in India](/posts/cert-in-ai-test-didnt-stay-a-test/).

The shift in assumption is the important part. "Trust the agent unless something goes wrong" becomes "assume the agent may eventually do something wrong, and make sure it can't get very far." Frankly, that's a healthier way to build things.

## What you can probably ignore

**"Microsoft says AI is dangerous."** It says agents are unpredictable and shouldn't get more access than their job needs. That's ordinary good security practice, applied to a new kind of worker.

**"This solves the problem."** It's a product and an architecture. How well it works will depend on how it's used.

## Why it earned this rating

This is another step in the right direction rather than a new risk.

Reasons it matters:

- A major tech company has publicly changed its security assumptions because of recent agent incidents [1].
- It reflects a broader move toward treating model-level safeguards as not enough on their own.

Reasons to keep it modest:

- It's a company announcing its own product, and there's no independent evaluation yet.
- It doesn't change what the AI models themselves can do.

I'm giving it a **4**. Something real is changing in how AI agents get deployed, and it's worth keeping an eye on whether it actually catches problems.

## What I'm watching next

- **Real-world results.** Does this kind of supervision catch misbehaving agents before they cause harm?
- **Whether other enterprise software companies follow.**
- **Microsoft's call for more model transparency,** since it says security tools will need to see a model's reasoning, not just its inputs and outputs [1].

> **Bunker Check**
>
> **Current rating:** 4/10 · Worth Watching
>
> **Direction:** Holding
>
> **Could move higher if:** This kind of supervision becomes standard across businesses, or it is shown to catch serious incidents.
>
> **Could move lower if:** It turns out to be mostly marketing.

Bunker status: shovel remains undisturbed. The AI, however, is finally getting its own employee badge, with very limited door access.

## Sources

1. Microsoft, "Securing the agentic insider," October 19, 2026 (primary source). https://blogs.microsoft.com/blog/2026/10/19/securing-the-agentic-insider/
2. Microsoft Security Blog, "Agents are your newest insiders. Security must move at their speed.," October 19, 2026 (primary source). https://www.microsoft.com/en-us/security/blog/2026/10/19/agents-are-your-newest-insiders-security-must-move-at-their-speed/
3. Help Net Security, "Microsoft wants to limit AI agents' permissions when they stray from the job," October 20, 2026. https://www.helpnetsecurity.com/2026/10/20/microsofts-ai-agents-threats-guardian-agents/
