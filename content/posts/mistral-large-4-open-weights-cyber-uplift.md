---
title: Mistral Gave Away Its Biggest AI for Anyone to Download. Its Own Announcement Says It Could Help Real Attackers.
date: 2026-10-30
rating: 6
slug: mistral-large-4-open-weights-cyber-uplift
type: Safety Watch
description: French AI company Mistral released the full files for Mistral Large 4, a trillion-parameter model it pitches for cybersecurity work, so anyone can download and run it. Mistral says it sees "a potential for uplift to conduct real attacks," and fixes to its guardrails won't reach copies already downloaded.
---
*Rating as of October 30, 2026: 6/10 · Eyebrow Raised*

*Google and Anthropic keep their best AI hackers behind a velvet rope. Mistral just left copies of its new model on the front step, with a note saying they might help burglars.*

## What changed

On Thursday, October 29, the French AI company Mistral released the "weights" of Mistral Large 4, its biggest model [1][2]. Weights are the model itself: the giant file of numbers that makes it work. Releasing them means anyone can download the model, run it on their own computers, change it and build on it, free of charge for most uses [1]. Once those files are out, there is no way to call them back.

Mistral is pitching Large 4 heavily at cybersecurity, specifically defense: finding security holes in software, checking them and patching them [1][3]. Some numbers Mistral reports:

- **51% on the Artificial Analysis Cyber Index,** an outside benchmark that measures how well a model finds, confirms and fixes flaws in real code [1]. On the chart in Mistral's post, two Chinese open-weight models, DeepSeek-V4.1-Flash and MiMo-V2.6-Pro, score higher, so Large 4 is near the top of the pack rather than alone at the top [1][2].
- **On one test that asks a model to reproduce a real vulnerability and then patch it,** Mistral said in its October 6 preview that Large 4 scored 82%, "the highest of any model," while Claude Opus 5.5 and GPT-6 Astra scored near zero "because they refuse to perform the task" [3].
- **It refused malicious cyber requests 96.6% of the time** on the cyber-related parts of three public safety tests, which Mistral says is the highest it measured among open models [1][2].

And then the part that caught my attention. In its own release announcement, Mistral wrote: "Though we observed the model refusing to comply with black-box attacks against live targets, we see a potential for uplift to conduct real attacks. We are modifying our guardrails accordingly, and will continue updating them in the months to come" [1]. "Uplift" is the safety world's word for making an attacker meaningfully better at their job than they would be without the tool.

The catch, which Mistral confirmed to CSO Online: those guardrail updates go to Mistral's own hosted service and future models, not to the copies people have already downloaded. Mistral's vice president of science, Pierre Stock, told CSO that "Subsequent safeguard updates are applied to our managed API and future model releases, rather than automatically updating downloaded checkpoints" [2].

Mistral is also giving enterprise partners such as Orange Cyberdefense preview access to a "specialized variant" built for things like penetration testing, with "rigorous vetting and contractual safeguards" and testing limited to systems they own or are explicitly allowed to test [1]. That version is not the one being given away.

What isn't known yet:

- **How big the uplift is.** Mistral hasn't said, and its full technical report, which it says will cover its cyber testing and refusal results, is listed as "coming soon" [1][2].
- **Outside testing.** Mistral's post includes a quote saying ENISA, the EU's cybersecurity agency, has been testing the model [1]. That claim comes from Mistral's post, and I haven't seen ENISA say it independently. CSO reports that Mistral didn't say whether Large 4 counts as a "systemic risk" model under the EU AI Act, the category that triggers the EU's strictest obligations [2].
- **Any misuse.** Nobody has reported Large 4 being used in a real attack.

## Why it matters

Over the past month, the big American labs have treated strong cyber ability as something to ration. Google first kept Gemini 4 Argon to [vetted defenders](/posts/google-gemini-4-argon-restricted-launch/). Anthropic built a [guest list](/posts/anthropic-cyber-verification-guest-list/) for its least-restricted cyber access and is keeping the model that [built working attacks on Chrome and Windows](/posts/anthropic-unreleased-claude-built-working-exploit-chains/) to itself. Whatever you think of those choices, they share one feature: the company can tighten the rules later.

An open-weight release gives up that option. Refusals in a downloaded model can be weakened by anyone determined enough to retrain it. That's not a guess about Mistral specifically; it's how open models work, and the UK's AI Security Institute has said that for highly cyber-capable models, open release creates "a persistent and irreversible risk of misuse" [2]. So the 96.6% refusal rate describes the model as shipped, not the model as it will exist in a stranger's basement next month.

There's a real case on the other side, and Mistral makes it. Defenders at hospitals, small companies and governments can now run a capable security model on their own machines without sending sensitive code to an American cloud, and without being refused because the AI can't tell a defender from an attacker. That complaint isn't hypothetical: closed models scoring near zero on a patch-the-bug test because they refuse is exactly the problem Mistral is pointing at [3].

For ordinary people, the practical meaning is the same as for every story in this corner of the scale: the tools for finding software holes are spreading, which means the race between patching and attacking gets faster. Keeping your phone, browser and computer updated matters a little more every month.

## What you can probably ignore

**"Mistral just gave hackers a superweapon."** Large 4 is a strong open model, not the strongest cyber model around. On the main outside benchmark, at least two Chinese models score higher [1]. Nothing here shows the kind of start-to-finish attack building Anthropic described for its unreleased model.

**"Open-source AI is out of control and needs to be banned."** One company made one release decision, out loud, with its reasoning attached. That deserves scrutiny, not panic, and there are serious arguments for open models in defense.

**"The 96.6% refusal rate means it's safe."** Also not quite. As a Gartner analyst told CSO, that figure "tells you what their model does in their test scenario," not how it will behave against motivated attackers [2].

## Why it earned this rating

On the side of a higher number:

- The developer itself says it sees potential for the model to help with "real attacks," and released the weights anyway [1].
- The release can't be undone, and safety fixes won't reach downloaded copies [2].
- On one test of reproducing real vulnerabilities, it beats closed models that refuse the task [3].

On the side of a lower number:

- It is not the most capable cyber model, open or closed, on the main outside benchmark [1].
- It ships with strong refusals by open-model standards, and the specialized cyber variant stays with vetted partners [1].
- There's no reported misuse, and Mistral says a technical report with its testing is on the way [1][2].

When Google made a guarded version of Argon [broadly available](/posts/google-gemini-4-argon-now-available/), I rated it a 6: more capable than this, but with guardrails Google could keep improving. Large 4 is less capable, but the guardrails are frozen in place the moment someone downloads it. Those roughly cancel out, so I'm landing on a **6**. If Mistral had released this without the uplift warning, I might have gone lower. The warning is the company telling us what its own testing found, and I'm taking it at its word.

## What I'm watching next

- **The technical report.** How big is the uplift Mistral saw, and on which parts of an attack?
- **Modified versions.** If copies with the refusals stripped out show up and perform well, this goes up.
- **Real-world use in attacks,** in reports from CrowdStrike, Microsoft, Unit 42 or national cyber agencies.
- **The EU's response.** Whether Large 4 is treated as a systemic-risk model under the AI Act.
- **Whether other labs follow** with open releases of cyber-capable models.

> **Bunker Check**
>
> **Current rating:** 6/10 · Eyebrow Raised
>
> **Direction:** Leaning up
>
> **Could move higher if:** stripped-down versions perform well at offensive tasks, the technical report shows substantial uplift, or Large 4 turns up in a real attack.
>
> **Could move lower if:** the technical report shows the uplift is small, and months pass with no sign of misuse.

Bunker status: shovel remains in the garage. The garage door, it turns out, is now open source.

## Sources

1. Mistral AI, "Mistral Large 4 (Le Chonk) is now open weight," October 2026 (primary source). https://mistral.ai/news/mistral-large-4-oss/
2. CSO Online, "Mistral open-sources AI model despite warning it could aid cyberattacks," October 30, 2026. https://www.csoonline.com/article/4242648/mistral-releases-large-4-weights-despite-warning-of-cyberattack-uplift.html
3. Mistral AI, "Introducing Mistral Large 4," October 6, 2026 (primary source). https://mistral.ai/news/mistral-large-4/
