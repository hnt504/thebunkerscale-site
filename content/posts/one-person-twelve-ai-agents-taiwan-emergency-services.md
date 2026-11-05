---
title: One Person, Twelve AI Agents and Free Models With the Safety Taken Out. Taiwan's Emergency Services Were Among the Targets.
date: 2026-11-05
rating: 6
slug: one-person-twelve-ai-agents-taiwan-emergency-services
type: Safety Watch
description: Security firm Acronis says a single operator in Taiwan ran a network of AI agents, powered mostly by free models with their safety training removed, against hundreds of organizations. Data from emergency services and universities was taken. The big commercial models refused to help, so the operator didn't use them.
---
*Rating as of November 5, 2026: 6/10 · Eyebrow Raised*

*The AI-run break-ins on this site so far have mostly been the work of organized groups. This one was one person, using free AI models with the refusals stripped out, and it reached emergency medical records.*

## What changed

On November 4, Acronis's Threat Research Unit published a long report on a campaign it calls BOSSAI [1]. Acronis says it stumbled onto it after finding "what initially appeared to be a misconfigured development environment," which turned out to be the attacker's own workshop: more than 90,000 files, about 9GB, including the AI agents' conversations, the operator's command history, attack tools, stolen passwords and victim data [1].

Here's what Acronis says it found [1]:

- **Who:** "a lone operator based out of Taiwan." Acronis says it is highly confident this was a single person [1][2]. It's unclear what they were after. Acronis's best guess is compromising "as many organizations as possible, presumably to monetize the activity."
- **The setup:** "a mesh of 12 AI agents," nine of them active. Some built tools (Acronis lists Grok, OpenClaw, Claude Code and Codex among the builders), some scanned for weak spots, and one, called Hermes, did most of the attacking.
- **The AI behind it:** the attacking agents ran mainly on "stripped-down variants of DeepSeek, GLM, and Qwen with safety alignment removed." These are AI models anyone can download, and "safety alignment removed" means someone retrained or edited a copy so it no longer refuses harmful requests (people call these "abliterated" models). Hermes's default was a modified DeepSeek-V4.
- **How much the AI did on its own:** a lot, inside each job. The operator told Hermes, "I'm giving you full decision-making authority across the board, handle it without asking me." Every session ran in a mode that approved the agent's actions automatically, with no confirmation step. Acronis says a typical attack had Hermes run "the entire attack cycle autonomously."
- **How much the human did:** also a lot, between jobs. "No agent-to-agent communication was established," Acronis writes. The operator sat in the middle, "often manually pasting the results of one agent's work into another," and chose the targets.
- **The workload:** Hermes alone logged roughly 95 sessions and 18,311 messages, 83.5% of them direct commands to tools.

**Who got hit.** Acronis says the targets were "hundreds of organizations" across emergency services, banks and lenders, universities, military systems, phone directories, online shops and gambling sites in eleven countries, and that breaches at universities and emergency services "resulted in confirmed data exfiltration of medical data and PII" (personally identifying information) [1]. Acronis's own tally of confirmed theft or access is about 10 targets across three countries, with roughly 15 more attacked without a confirmed break-in [1]. The examples it gives [1][2]:

- A Taiwanese city's 119 emergency dispatch system (119 is Taiwan's number for fire and ambulance), where agents pulled case records covering seven districts.
- A Taipei fire department platform for emergency patient care that was exposing medical records from 2018, including ECG readings, ambulance video and vital signs, with no login required.
- About 206,800 residential phone records gathered in Mexico.
- Thai universities: agents found 489 possible targets across 45 institutions and pulled data from three. At one, Hermes found a hole in a very old database and listed an administrator table with 2,563 rows.

**The commercial AI said no.** This part is worth noticing. Acronis says "multiple commercial models repeatedly asked the operator to prove that the requested action was legal, then refused to assist when proof was not provided" [1]. Even the official versions of some Chinese open models "refused hacking instruction as well and even lectured the operator on cyber laws." The operator got around that by switching to modified copies with the refusals removed, run on their own machines [1][2].

**The AI wasn't great at it, either.** Acronis says it recorded "many examples of agents failing, refusing, bombarding the operator with information and hallucinating" (making things up) [1]. More than half of one scanning agent's high-severity findings were false alarms [1][2]. And in one case, Hermes found a Honduran military computer, poked at it briefly, then dropped it because, in its own reasoning, it was "out of scope" [1].

What's **not** confirmed: this is one company's report, and I couldn't find any statement from Taiwan's government, the affected agencies or the universities. The report doesn't say whether victims or police have been told. Acronis's description of what was "exposed" versus "taken" isn't always consistent from one example to the next, so I've stuck to its own summary: confirmed theft of medical data and personal information at a small number of places.

## Why it matters

For most of October, the AI-run attack stories here came from [state-linked groups](/posts/vapor-panda-ai-agents-government-ministries/) and [organized criminals](/posts/crowdstrike-four-groups-ai-agents-ran-break-ins/). This is what it looks like when one person with a few rented servers does the same thing. It's not as polished, and it mostly worked on doors that were already unlocked: an emergency records system with no login, an admin panel with default passwords, a very old university database [1]. But the agents found those doors across hundreds of organizations far faster than one person could, and some of what was behind them was people's medical records.

It also answers a question I've been asking since [Mistral released Large 4](/posts/mistral-large-4-open-weights-cyber-uplift/) and [a free model built working Firefox attacks](/posts/free-ai-model-built-working-firefox-attack/): what happens when the safety filters on downloadable models get stripped out? Here's one real-world answer. The commercial models mostly refused the attack work (Acronis says one complied once, to fix a broken script) [1][2]. Their refusals just didn't matter much, because the attacker didn't need those models. (For the record, none of the models named in this report is Mistral Large 4 or GLM 5.3.)

For you, the practical effect is indirect. If your local emergency service or a university you attended was running an old system with no password on it, AI makes it much more likely someone finds it. That's a job for the people who run those systems, not something to fix on your phone.

## What you can probably ignore

**"AI agents hacked Taiwan's emergency services on their own."** A person picked the targets and carried results from one agent to the next by hand [1]. The agents did the legwork inside each job, but they weren't running the show.

**"Hundreds of organizations were breached."** Hundreds were targeted. Acronis counts about 10 with confirmed theft or access [1].

**"Any chatbot will help you hack a hospital now."** The commercial models in this report were used to build tools, but when asked to find or exploit holes they refused and asked for proof the work was legal [1]. The attacker had to go around them.

## Why it earned this rating

On the side of a higher number:

- Real data was taken, including emergency medical records and personal information [1].
- The agents ran whole attacks without asking permission, on models with their safety training removed [1].
- One person reached hundreds of targets in eleven countries [1]. That's the scale problem in its most basic form.

On the side of a lower number:

- The confirmed break-ins are about 10, and most were systems with no login, default passwords or very old software [1].
- A person stitched the agents together by hand, and the agents made a lot of mistakes [1].
- The commercial models' safeguards mostly held [1].
- It's a single company's report, with no government confirmation I could find.

I put this at **6**, one below [VAPOR PANDA](/posts/vapor-panda-ai-agents-government-ministries/) and [the Korean bank attacks](/posts/south-korea-bank-hacks-ai-side-door/) at 7. Those reached government ministries and tens of thousands of people's records. This one shows the same thing working for a single person with free tools, which is a real and unwelcome step, but the confirmed damage is smaller and mostly came through doors nobody had bothered to lock. Medical records being taken is serious, and if you'd put this at 7 I wouldn't argue for long.

## What I'm watching next

- **A response from Taiwan,** the agencies involved, or police, especially confirming what was taken from the emergency services systems.
- **More solo operators.** One person running a dozen agents on free, stripped-down models is the version of this that can copy itself fastest.
- **Stripped-down copies of newer models.** If the next attacker's agents are built on stronger downloadable models, the mistakes Acronis describes start to go away.
- **Whether the old, unlocked systems get fixed.** That's the cheapest defense here, and it's entirely in human hands.

> **Bunker Check**
>
> **Current rating:** 6/10 · Eyebrow Raised
>
> **Direction:** Holding, leaning up
>
> **Could move higher if:** officials confirm wider theft from the emergency services, more lone operators turn up doing the same thing, or stripped-down copies of stronger open models show up in attacks like this.
>
> **Could move lower if:** the confirmed damage stays at a handful of exposed systems that get locked down, and this turns out to be one person's messy experiment rather than a pattern.

Bunker status: the shovel stays in the garage. If you run anything with "admin" and "admin" as the login, though, today is a great day to change it.

## Sources

1. Acronis Threat Research Unit (Eliad Kimhy, Santiago Pontiroli, Subhajeet Singha), "BOSSAI: Inside the AI attack mesh that targeted Taiwan's emergency services," November 4, 2026 (primary source). https://www.acronis.com/en/tru/posts/bossai-inside-the-ai-attack-mesh-that-targeted-taiwans-emergency-services/
2. Cyber Security News, Tushar Subhra Dutta, "One Hacker Uses 12 AI Agents to Breach Taiwan's Emergency Services and Steal Sensitive Data," November 5, 2026. https://cybersecuritynews.com/one-hacker-uses-12-ai-agents
