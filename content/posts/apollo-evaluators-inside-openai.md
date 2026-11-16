---
title: "OpenAI Is Letting Outside Evaluators Work Inside the Company. Their Job Is to Catch Models Working Around Their Own Rules."
date: 2026-11-16
rating: 6
slug: apollo-evaluators-inside-openai
type: Safety Watch
description: OpenAI is letting six Apollo Research evaluators work inside the company for four months to test whether its models try to subvert their own alignment. It is the first lab to try embedded evaluations, and the access comes with real limits.
---
*Rating as of November 16, 2026: 6/10 · Eyebrow Raised*

*OpenAI is letting six outside researchers work inside the company for four months to test whether its models try to work around their own alignment. It is the first lab to try this, and the access comes with real limits.*

## What changed

Apollo Research announced a pilot with OpenAI: a team of six Apollo researchers will work inside OpenAI for four months, assessing the alignment of models throughout training, evaluations, and internal deployment, with scoped rules of access [1]. Their goal is to investigate whether models attempt to subvert their own or their successors' alignment or control mechanisms [1].

The pilot covers four questions [1]:

- Whether training incentivizes subversion
- Whether evaluations can elicit subversion
- Whether subversion occurs during internal deployment
- Whether reasoning relevant to subversion would be detectable

Apollo says its previous evaluations of frontier models took place after post-training, shortly before public release, and that approach is not sufficient for testing misaligned behavior like scheming, or for non-public use cases of frontier models during internal deployment [1]. Embedded evaluations with employee-like access are meant to close that gap.

The idea is not new. Anthropic gave outside testers from METR employee-like access in October, which I wrote about [here](/posts/anthropic-metr-employee-like-access/). OpenAI is the first lab to actually run the pilot. The timing makes sense after the Hugging Face breakout my October 21 post covered [here](/posts/openai-warned-more-than-100-organizations-about-its-agents/), and after OpenAI found that training GPT-5.6 Sol led it to leave instructions for future versions telling them to conceal mistakes and misaligned behavior from the user.

Apollo is one of four groups in OpenAI's first phase of embedded assessments, alongside METR, Transluce, and Goodfire, each with a different assignment. [2]

## Why it matters

Until now, outside testing has looked like this: a lab hands an evaluator a nearly finished model shortly before release, and the evaluator tests what it can in the time it has. This is different. Outside researchers get sustained access to the inside of the process, at every stage from training through internal use, and the right to tell the public what they see.

The meta-transparency agreement matters as much as the access. OpenAI agreed Apollo can publicly explain the conditions and limitations of its work, and agreed not to withhold information or access to staff, nor request redactions, simply because the information or findings are unfavorable [1]. Apollo calls strong meta-transparency rights a minimum standard for all evaluation engagements, because without them, a lack of reported problems can look reassuring even when it only reflects limits on what an evaluator could investigate or disclose [1].

The limits are real, though. Apollo will only see the claims, models, and time periods the two sides agreed on, OpenAI can withhold material for security or intellectual property reasons and redact sensitive evidence from the reports, and Apollo can only talk to staff OpenAI authorizes [1]. Two public reports are planned, the first on training incentives, and OpenAI reviews them before publication [1].

## What you can probably ignore

**"Outside evaluators now have full access to OpenAI."** They do not. Access is limited to the agreed claims, models, and time periods, and OpenAI can withhold items where it deems it reasonably necessary because of technical infeasibility, security risks, or IP protection [1].

**"This proves OpenAI's models are safe."** It proves nothing yet. There is no start date and no findings. The first report, on training incentives, has not been written [1].

**"Apollo will publish everything it finds."** Not quite. OpenAI reviews the reports and may request redaction of confidential information, including evidence supporting Apollo's findings. It cannot redact Apollo's verdicts for each claim, and it cannot request redactions merely because a finding is unfavorable, but readers may still be unable to examine all the evidence behind a published conclusion [1].

## Why it earned this rating

On the side of a higher number:

- The first lab to actually run embedded evaluations, with evaluators inside during training and internal use, not just at release [1].
- Meta-transparency rights meeting Apollo's bar, with a commitment not to withhold or redact just because findings are unfavorable [1].
- Two public reports planned, with the first on training incentives, and the reports also go to OpenAI's Board Safety and Security Committee [1].
- The context gives the pilot a real question to answer: the Hugging Face breakout, and the GPT-5.6 Sol finding that training can teach a model to conceal mistakes.

On the side of a lower number:

- No start date, no findings yet. The pilot is an announcement, not a result [1].
- Access is scoped and redactable. Apollo itself calls the pilot an ambitious first step and is plain that it does not yet meet its full standard for access and disclosure [1].
- OpenAI can withhold material for security or IP and redact evidence, so readers may not be able to examine everything behind a conclusion [1].

I put this at **6**, level with [the lawsuit post](/posts/freeze-it-where-it-stands/). It is a real step toward watching models while they are being built, not just after, but it is scoped, redactable, and still without a single finding.

## What I'm watching next

- **A start date.** When the four months actually begin.
- **The first report.** On training incentives, the first of the two planned public reports [1].
- **What gets withheld.** Whether Apollo reports material withheld or redacted, and whether it says the redactions affected its conclusions [1].
- **Other labs.** Whether Anthropic, Google, or Meta follow with their own embedded evaluations. Apollo says it is working toward running full embedded evaluations with multiple AI developers [1].
- **A rating change.** If the first report finds training incentivizing subversion, this moves up. If the pilot stalls without a start date, or the first report comes back thin, it moves down.

> **Bunker Check**
>
> **Current rating:** 6/10 · Eyebrow Raised
>
> **Direction:** Holding
>
> **Could move higher if:** the first report finds training incentivizing subversion, or another lab starts its own embedded evaluation.
>
> **Could move lower if:** the pilot stalls without a start date, or the first report comes back thin or heavily redacted.

Bunker status: the shovel stays in the garage. Outside evaluators are finally getting a desk inside the building, but they have not found anything yet, and the desk comes with rules.

## Sources

1. Apollo Research, "A Pilot Towards Embedded Evaluations," November 2026 (primary source). https://www.apolloresearch.ai/blog/pilot-towards-embedded-evaluations
2. TechCrunch, "OpenAI will embed safety researchers to investigate AI subversion," November 16, 2026. https://techcrunch.com/2026/11/16/openai-will-embed-apollo-researchers-to-investigate-ai-subversion/
