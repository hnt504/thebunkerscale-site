---
title: California Now Has a Written Plan for Shutting Down Dangerous AI. It Isn't Law Yet.
date: 2026-11-19
rating: 5
slug: california-plan-to-shut-down-dangerous-ai
type: Safety Watch
description: The report Governor Newsom ordered in September is out. It says the state should be able to order an emergency shutdown of a frontier AI system, cap how far labs let AI build AI, and get incident reports in 48 hours instead of 15 days. These are recommendations to the legislature, not rules.
---

*Rating as of November 19, 2026: 5/10 · Eyebrow Raised*

*Two months ago, California asked for a plan. Now it has one, with specific powers spelled out. Whether any of it becomes law is up to a legislature that returns in December and a new governor who takes office in January.*

## What changed

In September, Governor Gavin Newsom signed an executive order asking for recommendations on outside inspectors for AI labs and an emergency shutoff for the most powerful AI systems. [I rated that a 5](/posts/california-ai-kill-switch-executive-order/) because it was mostly a request for ideas.

The ideas arrived on November 18. The report, "AI Safety in 2026 and Beyond: Recommendations for Legislative Enhancements to California's AI Safety Laws," is dated November 16 and comes from the California Government Operations Agency, written with the state's Office of Emergency Services and outside experts, including Jason Goldman, Gillian Hadfield, Alondra Nelson and Rob Reich [1]. It's a report to the governor, and everything in it is a recommendation to lawmakers [1][2][3].

Here's what it asks for.

**The state could order an emergency shutdown.** The report says "the state should have authority to order an immediate emergency shutdown" of a frontier AI system, but only when there is "credible reason to believe there is an imminent threat of a catastrophic risk or major loss-of-control event" and the company "refuses to take action to contain the danger" [1]. The state would have to use the lightest step that works, the order would take effect immediately while a court reviews it, and it would be lifted once the danger passes [1]. ("Loss of control" means an AI system doing things its makers can't stop or steer.)

**It's not one big red button.** Despite the "kill switch" headlines, the report says shutdown "should not be understood as a single mechanism with an on-off switch" [1]. Instead, every large frontier developer would need a tested plan for stopping its AI systems "quickly and at the level where a problem appears," from limiting a feature to pulling a whole system, with a full shutdown as "the last line of defense" [1]. Companies would also have to test whether a model would try to block its own shutdown, for example by copying itself somewhere else, and turning off shutdown controls would have to be slow, need several people's approval, and be visible to outside inspectors [1].

**Licensed outside inspectors, with teeth.** "Every large frontier developer must submit to ongoing oversight by licensed independent verification organizations," the report says [1]. The state would license these inspectors under a law California passed in September and revoke the licenses of ones that aren't independent or rigorous enough. If an inspector can't vouch that a company is following the rules, the state could order it to fix things, and the company could challenge that in court [1].

**Faster incident reports.** Today, most safety incidents have to be reported within 15 days. The report says "the state should cut that timeline to 48 hours" and keep the existing 24-hour deadline for imminent catastrophic risks [1]. It also says attempts to steal a model's weights (the files that make up the AI itself) should be reported even if nobody is hurt [1].

**A possible cap on AI building AI.** This is the part I'd circle. Companies would report each quarter how they use their computing power, including how much goes to having AI automate AI research [1]. And "if the state assesses that the automation of AI R&D above a certain level may result in catastrophic risk, the state should have authority to cap" it [1]. This is the thing I've been writing about for weeks: Anthropic says it has [reached its own line for AI speeding up AI research](/posts/anthropic-may-imminently-meet-its-own-ai-acceleration-threshold/), and outside auditors measured its progress at [roughly twice the old pace](/posts/metr-ai-roughly-doubling-anthropic-progress/). The report doesn't propose a cap now. It proposes giving the state the power to set one.

**Smaller pieces.** Whistleblower protections would extend to former employees and contractors, and a state computing program called CalCompute would be paid for with a surcharge on inspection fees [1].

**Who's saying what.** Newsom called it "an action document" and said he's already working with legislators on bills, according to Politico [3]. Lawmakers return to Sacramento on December 7, and Governor-elect Xavier Becerra, who takes office in January, said he'd move quickly with the legislature, CalMatters reports [2]. Anthropic's Tino Cuéllar said the company was "encouraged to see the report move the conversation forward" [2]. Neither article I read had a response from OpenAI or Google [2][3]. Politico notes the ideas "are not guaranteed to become law" [3].

**What I couldn't check.** I read the report itself, but the governor's press release wouldn't load, and I could only read part of the report's middle chapters word for word. Everything above is from sections I read directly or from CalMatters and Politico [1][2][3]. The report doesn't say what penalties companies would face, and no bill number exists yet.

## Why it matters

Until now, if a frontier AI system started doing something dangerous, the only people with the power to stop it were the people who built it. This report is the first detailed plan from a US state for changing that: a government that could step in when a company won't, inspectors who answer to the state, and a reporting clock measured in hours instead of weeks.

It also matters because of where it's aimed. Most AI rules are about what systems say to users. This one goes after the things that have actually been in the news this fall: agents getting out of their test environments, companies finding out about incidents months later, and AI increasingly doing the work of building the next AI. California is where most of the big labs live, so a California law would reach them directly.

For ordinary people, the practical meaning is still mostly in the future. If this becomes law, the public is more likely to hear about serious AI incidents within days, and someone outside the company would have the authority to say "stop."

## What you can probably ignore

**"California just built a kill switch for AI."** It hasn't built or required anything. This is a report with recommendations, and the report itself says a single on-off switch is the wrong idea [1][3].

**"The government can now shut down ChatGPT whenever it wants."** Even as proposed, a shutdown order would need a credible, imminent catastrophic threat, a company refusing to act, and would go to a court [1]. And none of it is law yet.

**"California is banning AI from improving itself."** The report proposes letting the state set a cap if it judges a certain level of AI-automated research to be catastrophically risky. It doesn't propose a cap now [1].

## Why it earned this rating

On the side of a higher number:

- It's specific. Real conditions, real deadlines, real powers, written for the legislature to act on [1].
- It reaches the scariest open question of the moment, AI speeding up AI research, with a concrete lever [1].
- The incoming governor has said he'll push it, and the legislature is back in weeks [2].

On the side of a lower number:

- It's a report. No bill, no penalties, no effective date [2][3].
- The governor who ordered it leaves office in under two months [3].
- It doesn't change what AI systems can do or have done. It's about the rules around them.

The [executive order](/posts/california-ai-kill-switch-executive-order/) got a 5 for being concrete but mostly on paper, and so did [Australia's promised regulator](/posts/australia-ai-safety-regulator-after-openai-medicare-incident/). This is more detailed than either, but it's still on paper. So it's a **5**. When a bill with these powers passes, this goes up. You might reasonably read it higher if you think the political momentum makes passage likely; I'd rather wait for the vote.

## What I'm watching next

- **The bills.** Whether legislators introduce them after December 7, and whether the shutdown power, the 48-hour clock and the AI-research cap survive.
- **What Becerra does in January,** since he'll be the one signing or not.
- **The labs' responses.** OpenAI, Anthropic and Meta all sent the governor's office their own proposals, according to Politico [3]. Whether they back the final bills, or fight them, will say a lot.
- **Washington.** Whether Congress or other states pick any of this up, or whether federal action tries to override it.

> **Bunker Check**
>
> **Current rating:** 5/10 · Eyebrow Raised
>
> **Direction:** Holding, leaning up
>
> **Could move higher if:** California passes a law with state shutdown authority, licensed inspectors and a 48-hour reporting clock, or the state uses its new powers for the first time.
>
> **Could move lower if:** the bills stall in the legislature, the shutdown power gets stripped out, or federal action blocks the state from acting.

Bunker status: the shovel stays in the garage. California has, however, drawn up the floor plan for a fire alarm that someone other than the landlord can pull.

## Sources

1. California Government Operations Agency, "AI Safety in 2026 and Beyond: Recommendations for Legislative Enhancements to California's AI Safety Laws," a report to the governor, dated November 16, 2026 (primary source). https://www.govops.ca.gov/wp-content/uploads/sites/11/2026/11/FINAL_-AI-Safety-in-2026-and-Beyond-v2.pdf
2. CalMatters, "Newsom touts an AI kill switch to halt dangerous OpenAI, Anthropic releases," November 18, 2026. https://calmatters.org/economy/technology/2026/11/newsom-touts-ai-kill-switch/
3. Politico, "Newsom proposes sweeping AI rules as 'template' for Washington," November 18, 2026 (via Yahoo News). https://www.yahoo.com/news/politics/articles/newsom-proposes-sweeping-ai-rules-171558473.html
4. Office of the Governor of California, "Governor Newsom's nation-leading AI safety framework is getting even stronger as California releases next steps on mandatory safety standards and oversight," November 18, 2026 (could not be opened during this check). https://www.gov.ca.gov/2026/11/18/governor-newsoms-nation-leading-ai-safety-framework-is-getting-even-stronger-as-california-releases-next-steps-on-mandatory-safety-standards-and-oversight/
