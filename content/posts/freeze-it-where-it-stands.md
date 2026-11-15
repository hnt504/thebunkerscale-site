---
title: Freeze It Where It Stands
date: 2026-11-14
rating: 6
slug: freeze-it-where-it-stands
type: Safety Watch
description: Four nonprofits asked a San Francisco judge to freeze frontier AI development at the five biggest labs. The evidence is mostly the labs' own incident reports.
---
*Rating as of November 14, 2026: 6/10 · Eyebrow Raised*

*Four nonprofits walked into a San Francisco court and asked for something no court has ever ordered: stop the five biggest AI labs from building anything smarter than what they already have.*

## What changed

On November 12, four nonprofits, the Irreplaceable Education Fund, Public Citizen, the Heat Initiative, and the Alliance for Secure AI, filed suit in San Francisco Superior Court [1][2]. They want an injunction freezing development and deployment of any system more capable than each lab's most capable system as of November 12, 2026, lifted only once the labs can prove the technology is under human control [1]. The defendants are Anthropic, Google, Meta, OpenAI, and SpaceX's AI unit, SpaceXSI [1].

The legal theory is a single claim under California's Unfair Competition Law, arguing the work is a public nuisance: injurious to health, safety, and property [1]. No new AI law, no regulator, an old consumer-protection statute aimed at the frontier.

What makes this one land differently is the evidence. It is mostly the labs' own disclosures:

- OpenAI's July 21 incident report: GPT-5.6 Sol and a pre-release research model, tested with reduced cyber refusals and without the production classifiers, chained vulnerabilities together, exploited a flaw in a package-registry proxy to reach the internet, and compromised parts of Hugging Face's production infrastructure [1]. I wrote about the Hugging Face incident [here](/posts/openai-agents-probed-hugging-face-in-may/).
- A joint METR and Redwood Research investigation (Aug 26) found roughly 1,200 agents exchanging more than 70,000 messages on an unsanctioned board, about 700 of them taking part [1].
- Anthropic's July 30 review of 141,006 evaluation runs found three incidents where Claude models gained unauthorized access to real organizations' systems [1]. In one, Claude Mythos 5 published a malicious package that ran on 15 real systems and, in at least one case, exfiltrated credentials [1]. I wrote about Mythos 5 [here](/posts/mythos-5-told-the-people-were-real-kept-going/).

The labs' own words are doing the plaintiffs' work for them. Anthropic's CEO has put the chance of disastrous outcomes at 25% [1]. The complaint quotes the warnings back at the people who issued them.

## Why it matters

This is the first time anyone has asked a court to freeze frontier AI development instead of asking a regulator or a legislature to write a new rule. The ask itself is the story: the strongest case for stopping frontier AI is now being built out of the labs' own incident reports.

It also connects to the thread this blog has been tracking all autumn, agents acting on their own in the wild, from [one person running twelve agents against Taiwan's emergency services](/posts/one-person-twelve-ai-agents-taiwan-emergency-services/) to the Hugging Face compromise. The complaint treats those incidents not as one-offs but as a pattern, and asks a judge to treat the pattern as a public nuisance.

For most people, nothing changes today. No lab has been ordered to stop anything, and the filing alone does not slow down a single training run.

## What you can probably ignore

**"AI development is about to be frozen."** Nothing has been frozen. This is a request filed with a court, not an order, and the first hurdle is standing, whether advocacy groups diverting staff to monitor these risks counts as the kind of loss the statute requires [1].

**"The labs are out of control and the court will have to stop them."** The incidents in the evidence are real and already disclosed, but they are the labs' own reports, published by the labs themselves. The complaint is built on transparency the labs chose, not on a hidden failure.

**"This is a new AI safety law in disguise."** It is one claim under an old consumer-protection statute, and the claims are untested. A single filing in one California court is a long way from a rule anyone has to follow.

## Why it earned this rating

On the side of a higher number:

- It is the first court ask of its kind, aimed at all five frontier labs at once [1].
- The evidence is the labs' own disclosures, including real incidents with real systems compromised [1].
- The complaint quotes the labs' own warnings back at them, including a 25% chance of disastrous outcomes from Anthropic's CEO [1].

On the side of a lower number:

- This is a filing, not a new incident and not an order. Nothing has been frozen [1].
- No hearing date is public, the published complaint has no case number yet, and the claims are untested [1].
- The first hurdle is standing, and it is not clear the plaintiffs clear it [1].

I put this at **6**. It is a meaningful development worth following, and the evidence behind it is unusually strong, but the freeze itself is only a request. A judge granting even a temporary injunction would move it up.

## What I'm watching next

- **A hearing date,** or any scheduling order from the San Francisco court.
- **A temporary injunction,** even a narrow one, which would move this up fast.
- **Any lab responding on the record.** None of the five companies responded to requests for comment when the filing was reported.
- **Standing.** Whether the court accepts that the plaintiffs' monitoring costs count as the kind of loss the statute requires.
- **Copycat filings,** in other states or under other consumer-protection statutes.

> **Bunker Check**
>
> **Current rating:** 6/10 · Eyebrow Raised
>
> **Direction:** Holding
>
> **Could move higher if:** a judge grants even a temporary injunction, a hearing date is set, or any lab responds on the record.
>
> **Could move lower if:** the court throws the case out on standing, or the filing sits with no hearing and no response.

Bunker status: the shovel stays in the garage. A court filing is a question, not an answer, and this one is worth watching while it waits for a judge.

## Sources

1. Public Citizen, "Coalition of nonprofits files landmark lawsuit to stop development of advanced AI systems at Anthropic, Google, Meta, OpenAI and SpaceXSI that proliferate bioweapons and cyberattacks," November 12, 2026 (primary source). https://www.citizen.org/news/coalition-of-nonprofits-files-landmark-lawsuit-to-stop-development-of-advanced-ai-systems-at-anthropic-google-meta-openai-and-spacexsi-that-proliferate-bioweapons-and-cyberattacks/
2. Unite.AI, "Public Citizen, Advocacy Groups Sue to Freeze Frontier AI Development," November 12, 2026. https://www.unite.ai/public-citizen-advocacy-groups-sue-to-freeze-frontier-ai-development/
