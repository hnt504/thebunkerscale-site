---
title: Outside Auditors Checked Whether AI Is Speeding Up Anthropic's AI. Their Answer Is Roughly Twice as Fast.
date: 2026-11-09
rating: 8
rating_history:
  - date: 2026-11-09
    rating: 7
    note: Original rating.
  - date: 2026-11-13
    rating: 8
    note: Anthropic has since said, in an updated filing, that it has met its own threshold for AI speeding up AI research, one of the things this post said would move it up.
slug: metr-ai-roughly-doubling-anthropic-progress
type: Safety Watch
description: The independent research group METR spent about eleven weeks with inside access at Anthropic and estimates its models have been improving about 1.9 times faster since October 2025, with AI likely behind most of that. Anthropic redacted most of the evidence METR found most informative.
---
*Rating as of November 13, 2026: 8/10 · Pay Attention*

*A week ago, Anthropic told investors it may soon hit its own warning line for AI speeding up AI. Now someone from outside has measured the speed, and it came out higher than Anthropic's own published number.*

## What changed

**Update, November 13, 2026:** The first thing on my watch list below was Anthropic's response, and whether it would say how METR's numbers fit its own threshold. It has now answered the second part. An updated filing for its stock market listing, dated November 10, says Anthropic "made a determination that we have met this threshold based on what we expect from future models and our overall rate of progress, rather than on what we have observed from current models" [4]. It also says "our use of AI systems has already been accelerating our research and development" [4]. I covered that in [a rating change to the November 3 post](/posts/anthropic-may-imminently-meet-its-own-ai-acceleration-threshold/), which moved to 8 [2].

That was one of the two main things this post said would move it up, so I'm moving it to 8 as well. Two things haven't changed: nothing I've read of the filing connects it to METR's work, and the decision rests on what Anthropic expects from future models, not on something a current model was seen doing [4]. METR's redactions and the dropped compute check still stand. Everything below is the original post.

METR, a nonprofit that tests AI systems for dangerous capabilities, published "Independent Assessment of AI R&D Acceleration at Anthropic in October 2026" on November 5 [1]. ("AI R&D" means AI research and development: the work of building the next, better model.) The engagement ran from August 12 to October 29 [1].

It asked three questions: has the pace at which Anthropic's models get more capable sped up, how much of that is because of AI, and what is slowing it down [1].

**The headline number.** Using an index of benchmark scores for Anthropic's models, including ones that haven't been released, METR estimates that progress has "accelerated 1.9x [95% confidence interval: 1.5–2.8x] since October 2025" [1]. METR's definition: "a 2x acceleration means that 2 years of historical progress is made in 1 year" [1]. In its own summary, Anthropic is likely improving capabilities on well-specified tasks "at around twice the rate they did between March 2024 and October 2025" [1].

**How much of that is AI.** "We guess that a majority (perhaps ≈80%) of the current (October 2026) acceleration is due to AI," METR writes, and it flags substantial uncertainty around that guess [1]. It also says it received "convincing evidence that the acceleration was not due to an acceleration in the scale of training compute" [1]. In other words, this isn't just Anthropic buying more computers faster.

**Higher than Anthropic's own figure.** METR says its estimate "is greater than that reported in the Haiku 5.5 system card (1.7x)," mainly because it included newer, unreleased models [1].

**How sure they are.** Not very, and they say so: "We would not be surprised if the current rate of growth was closer to 1.3x or 3x the historical rate" [1]. They list ways they could be too high (other causes, progress limited to tidy, well-defined tasks, an unusually slow starting point) and ways they could be too low, starting with "We may have missed recent further acceleration" [1].

**What METR couldn't show you.** This is the part that gave me pause. "Anthropic had unilateral redaction rights over all non-public information in this report," and "Anthropic redacted a majority of the evidence we found most informative for these conclusions" [1]. Anthropic's stated reason was removing confidential information "that could accelerate other AI developers" [1]. METR's conclusion is blunt: as a result, "the public has to rely on METR's judgment much more than would be ideal" [1].

Two more limits. METR did not ask for or get the ability to run Anthropic's unreleased models itself [1]. And a planned check of how Anthropic splits its computing power between building capabilities and safety work was dropped partway through: "Anthropic changed the scope of this project midway to exclude compute verification" [1]. METR adds that "staff-level access would enable a significantly deeper assessment" [1].

**What it doesn't say.** It doesn't say Anthropic has crossed its own safety threshold. METR notes that Anthropic's Responsible Scaling Policy treats AI R&D acceleration as a key risk indicator, then says: "In this assessment, we do not pay special attention to the thresholds set in the RSP" [1]. Whether 1.9x on this index trips Anthropic's tripwire is a question METR deliberately left alone, and I haven't seen Anthropic answer it.

## Why it matters

When I wrote about [Anthropic's filing saying it "may imminently" meet its own threshold](/posts/anthropic-may-imminently-meet-its-own-ai-acceleration-threshold/), the first thing on my watch list was outside checking. This is that check, and it didn't come back smaller.

The worry with AI speeding up AI isn't a single dramatic moment. It's that each generation arrives sooner, so the time to test it, understand it and put protections around it shrinks. If progress at one frontier lab really is running about twice its old pace, and AI is doing most of the pushing, the people responsible for the brakes have about half the time they used to.

It's also a real test of outside oversight. When [Anthropic gave METR a desk inside the building](/posts/anthropic-metr-employee-like-access/) in October, I rated it as good news with real limits. Both halves turned out to be true. The assessment happened and was published, which is more than most labs offer. But the company being checked decided what the public gets to see, and redacted most of the best evidence.

For ordinary people, nothing about your phone or your job changes today. What changes is that "AI is accelerating AI" is no longer just a lab's own claim. An independent group looked and broadly agreed.

## What you can probably ignore

**"Anthropic's AI is now improving itself."** METR measured how fast Anthropic's models get better with people building them, with AI tools doing more of the work. Nothing in the report describes a model improving itself on its own [1].

**"AI progress has doubled everywhere."** This is one company's internal index, measured mostly on well-defined tasks, with a wide range of uncertainty [1]. METR is careful not to stretch it to the whole field.

**"METR proved Anthropic broke its own safety rules."** METR says it didn't assess the policy's thresholds at all [1].

**"The redactions mean Anthropic is hiding something sinister."** Anthropic's stated reason is keeping competitors from learning how it works faster [1]. That's a business reason, and it's plausible. It's still a problem for public oversight, whatever the motive.

## Why it earned this rating

On the side of a higher number:

- An independent group, not the company, estimates that a frontier lab's progress has roughly doubled, with AI likely responsible for most of it [1].
- The estimate is higher than the company's own published figure [1], and METR says it may be missing further recent acceleration [1].
- The company under review redacted most of the most useful evidence and dropped the compute check partway through [1].
- It lands a week after Anthropic told investors it may soon hit its own warning line for exactly this [2].

On the side of a lower number:

- It's a measurement of pace, not an incident. Nobody was harmed, and no model did anything it shouldn't have.
- The uncertainty is wide, from about 1.3x to 3x by METR's own judgment [1], and it's based on benchmark scores for well-defined tasks [1].
- Outside auditing actually happened, and was published with its limits spelled out. That's a safeguard working, if imperfectly.

*Originally:* I'm keeping this at 7, the same as the filing it follows up on. The filing was a forecast; this is a measurement that backs it up, which is why it isn't lower. It isn't 8 because nothing has gone wrong, METR didn't say any line was crossed, and the range of uncertainty is wide enough that the real number could be modest. If you think outside confirmation of AI doubling a lab's pace deserves an 8, I understand that view.

*Update, November 13:* I've now moved it to 8. METR's measurement on its own hasn't changed, but Anthropic has said its threshold has been met, which this post named as a reason to go up [4]. The outside measurement and the company's own determination now point the same way. It isn't higher, because nobody was harmed, the uncertainty is still wide, and Anthropic's decision rests on expectations rather than a model it can point to. If you'd keep this at 7 because METR's report itself didn't change, that's a reasonable view too.

## What I'm watching next

- **Anthropic's response,** and whether it says how this fits its own threshold.
- **The Responsible Scaling Policy update** Anthropic said it was considering, and whether it adds real human checkpoints.
- **Fewer redactions next time,** or other ways for outsiders to check the hidden evidence.
- **The compute check** Anthropic dropped, and whether it comes back.
- **Other labs.** Whether OpenAI, Google DeepMind or others allow a similar outside measurement.

> **Bunker Check**
>
> **Current rating:** 8/10 · Pay Attention
>
> **Direction:** Up (from 7 on November 13)
>
> **Could move higher if:** later assessments find the pace is closer to 3x, Anthropic names a current model as driving the speed-up, or another lab's outside check shows the same thing.
>
> **Could move lower if:** fuller evidence points to the low end of METR's range, or Anthropic's policy update adds clear, checkable human checkpoints and outsiders get the access METR says it lacked.

Bunker status: the shovel stays in the garage. Someone finally put a speedometer on the car, though, and it reads about twice what it used to.

## Sources

1. METR, "Independent Assessment of AI R&D Acceleration at Anthropic in October 2026," November 5, 2026 (primary source). https://metr.org/blog/2026-11-05-anthropic-ai-rd-acceleration-assessment/
2. The Bunker Scale, "Anthropic Told Investors It May Soon Hit Its Own Line for AI Speeding Up AI. No Model Has Crossed It Yet," November 3, 2026. https://thebunkerscale.com/posts/anthropic-may-imminently-meet-its-own-ai-acceleration-threshold/
3. METR linkpost on LessWrong, "METR: Independent Assessment of AI R&D Acceleration at Anthropic in October 2026," November 5, 2026. https://www.lesswrong.com/posts/N5AmYkRks5CqAxvBg/metr-independent-assessment-of-ai-r-and-d-acceleration-at
4. CASRAI, "Anthropic S-1 says it met its AI-progress bar," November 12, 2026, quoting Anthropic's Form S-1/A Amendment No. 2 dated November 10, 2026 (the filing itself is the primary source, but I couldn't open it in this run). https://casrai.org/news/anthropic-ipo-s1-accelerated-ai-progress-disclosure
