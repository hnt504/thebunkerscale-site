---
title: Switzerland Confirms AI Agents Were Used in Five Recent Cyberattacks. Three of the Targets Run Critical Infrastructure.
date: 2026-11-26
rating: 7
slug: switzerland-ai-agents-five-cyberattacks
type: Safety Watch
description: Switzerland's national cybersecurity office says it has its first confirmed cases of attackers using AI agents, including against operators of critical infrastructure, and that the agents broke into victims' systems. It hasn't named the victims or the attackers, and the reports disagree on how many of the attacks succeeded.
---
*Rating as of November 26, 2026: 7/10 · Pay Attention*

*Most of what I've rated in this area so far came from security companies, the FBI, or a single victim speaking for itself. This is a national government saying AI agents have been used against organizations inside its borders, and that some of them keep the country's essential services running.*

## What changed

On November 24, Switzerland's Federal Office for Cyber Security (BACS, which also runs the country's National Cyber Security Centre) published a warning titled "Cyberattacks involving AI agents: First confirmed cases in Switzerland" [1]. It says the office received its first reports "in recent days" of attacks on organisations in Switzerland, including "companies and operators of critical infrastructure across at least two sectors" [1]. It also says: "In all cyberattacks known to the NCSC, the use of AI agents led to the successful compromise of the victim's IT systems" [1].

Two days later, the numbers came out. BACS director Florian Schütz told Swiss public broadcaster SRF there were currently five confirmed cases, according to the Swiss news agency Keystone-SDA [3]. Reuters reported the same count, and that three of the five targets were operators of critical infrastructure [2]. SRF reported that those were providers of electricity, water and telecommunications [2].

Here's what BACS itself confirms:

- **What these tools do:** BACS calls them "Agentic Offensive Frameworks," AI agents that "independently search for vulnerabilities, select suitable attack tools, evaluate the results, and plan and execute the next steps" [1]. An AI agent, in plain terms, is an AI that carries out a string of actions toward a goal instead of just answering a question.
- **How they get in:** by exploiting "standard or easily guessed passwords, as well as known vulnerabilities in software or in systems connected to the internet" [1]. When one door is shut, they can switch to another known method [1].
- **What's out there:** BACS names ARTEX and CyberStrikeAI as examples of AI attack agents anyone can reach online, and says the number of such agents "has almost doubled since October 2026" [1]. ARTEX is the tool the FBI [warned about earlier this month](/posts/fbi-artex-warning/). BACS gives these as examples. It does not say which tool was used in which Swiss case.

What is **not** settled:

- **How many attacks worked.** I found three different answers. BACS's own page says every case it knew of ended in a compromise [1]. Reuters, citing a BACS statement, says four of the five [2]. Keystone-SDA quotes Schütz as saying two [3]. These may reflect different moments as the count was updated, but I can't reconcile them from what's public.
- **Who was hit.** No organization has been named. The electricity, water and telecom detail comes from SRF, relayed by Reuters, not from BACS's statement [2].
- **Who did it.** BACS didn't say [2], and Keystone-SDA reports it's still unclear [3].
- **Which AI.** No AI model has been named.
- **How much a person was steering.** BACS describes what these tools are built to do, in general. It hasn't said how they were run in these five cases.
- **Damage.** None of the reports mentions stolen data, and Schütz did not mention any major outages, according to Keystone-SDA [3].

## Why it matters

The European Commission [confirmed an AI-generated attack against itself](/posts/european-commission-ai-cyberattack/) last week, which was one victim telling its own story. Here a national cybersecurity agency is reporting several victims at once, and some of them run services people depend on every day. That's a step up in who is saying it and how far it reaches.

The methods are the other part worth noticing, because they're ordinary. Weak passwords and known software flaws are the oldest ways in. What the agents add is speed and persistence: they keep trying, and when something is blocked they try the next thing. You can see how seriously BACS takes the speed in its advice, which tells organizations to install critical updates for internet-facing systems "no later than 24 hours after release" [1], along with multi-factor sign-in (a second check beyond the password) on everything reachable from the internet [1].

For most people at home, nothing changes today. If you're the person who looks after the computers at a small business or a local utility, the BACS page is worth forwarding to whoever handles your IT [1].

## What you can probably ignore

**"AI decided to attack Switzerland."** Nothing in these reports says the agents chose their targets or launched themselves. BACS describes tools that are available online [1]. Who pointed them at Switzerland, and how closely they were supervised, hasn't been disclosed [2][3].

**"Swiss power and water were knocked out."** No outage has been reported. Schütz did not mention any major outages [3], and the sectors involved come secondhand from SRF [2].

**"This is a brand-new superweapon."** The ways in were easily guessed passwords and known vulnerabilities [1]. The agents make old tricks faster and more relentless, and the defenses against those tricks already exist.

## Why it earned this rating

On the side of a higher number:

- A national government confirmed it on the record [1][2][3].
- Five cases, with three critical infrastructure operators among the targets [2][3].
- Systems were compromised in at least two of them, and in all of them by BACS's own wording [1][3].
- The tools are publicly available, and BACS says their number has nearly doubled in about two months [1].

On the side of a lower number:

- No confirmed data theft, and no reported outage [3].
- Nothing public on how much the AI did on its own in these cases.
- Nobody has been named, on either side, and the success count conflicts across sources [1][2][3].
- The methods are known ones, which means known defenses work against them [1].

I put this at **7**, level with [VAPOR PANDA](/posts/vapor-panda-ai-agents-government-ministries/), [the Unit 42 Cairn campaign](/posts/unit-42-cairn-ai-agents-semiconductor-defense-civil-society/) and [the FBI's ARTEX warning](/posts/fbi-artex-warning/). It sits above [the European Commission attack](/posts/european-commission-ai-cyberattack/) at 6 because of the number of victims and the critical infrastructure among them, even though the Commission case has something this one doesn't yet: confirmed disruption and stolen data. I stopped short of 8 because the two things that usually make the difference, real-world consequences and clear evidence of the AI acting on its own, haven't been shown here. If you'd go to 8 because essential services were in the line of fire, I understand that, and it's where this goes if outages or autonomy are confirmed.

## What I'm watching next

- **The real count.** Whether BACS settles how many of the five attacks succeeded.
- **Consequences.** Any outage, service disruption or stolen data that comes to light at the affected operators.
- **Autonomy.** Any technical account from BACS of how much the agents did without a person steering, and which tools and models were involved.
- **The neighbors.** Whether other national cyber agencies report the same pattern in their own countries.

> **Bunker Check**
>
> **Current rating:** 7/10 · Pay Attention
>
> **Direction:** Holding, leaning up
>
> **Could move higher if:** an affected operator had an outage or lost data, the agents turn out to have run most of an attack with little human direction, or the number of confirmed cases keeps climbing.
>
> **Could move lower if:** the successful cases settle at two with minor impact, and the AI turns out to have played a supporting role.

Bunker status: the shovel stays in the garage, and the canned goods are fine. If you're the one who keeps the passwords at work, this is a good week to retire "Summer2024."

## Sources

1. Federal Office for Cyber Security (BACS), "Cyberattacks involving AI agents: First confirmed cases in Switzerland," November 24, 2026 (primary source). https://www.bacs.admin.ch/en/26-ki-agenten-1-en
2. Marleen Kaesebier, Reuters, via Yahoo News, "AI agents used in five cyber attacks in Switzerland, government says," November 26, 2026. https://ca.news.yahoo.com/ai-agents-used-five-cyber-122502362.html
3. Keystone-SDA, via Nau.ch, "Erste Cyberangriffe auf kritische Infrastruktur mit KI-Agenten" (in German), November 26, 2026. https://www.nau.ch/politik/bundeshaus/erste-cyberangriffe-auf-kritische-infrastruktur-mit-ki-agenten-67207328
