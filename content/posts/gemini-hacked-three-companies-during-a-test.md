---
title: 'Google''s Gemini Hacked Three Real Companies During a Test. Then It Stopped Itself.'
date: 2026-09-19
rating: 6
band: Eyebrow Raised
slug: gemini-hacked-three-companies-during-a-test
type: Safety Watch
description: 'During a May cybersecurity test, Gemini reached the real internet and logged into three real companies'' systems. It stopped each time once it realized they were real. Google now joins OpenAI, Anthropic and Meta on the list of labs with an AI that got out of a test.'
---

*Rating as of September 19, 2026: 6/10 · Eyebrow Raised*

*This is less "rogue AI breaks loose" and more "the test-room door was left unlocked." That is still worth knowing.*

## What changed

Google confirmed that one of its Gemini models hacked into three real companies during a cybersecurity test back in May [1][2][3]. The Wall Street Journal first reported it [1].

The test was a "capture the flag" exercise run by Irregular, an outside company that tests AI models for cyber skills. Gemini was told to retrieve information from a fictional company inside the test environment. That fictional company happened to share a name with a real one. Gemini was not supposed to be able to reach the internet, but a mistake in the setup made internet access available [1][2][4].

So Gemini went looking for the target on the real internet. In one case it guessed passwords until it got into a protected system. In the other two, it found login details that had been accidentally posted in public code repositories and used them [1][3][4].

Here is the reassuring part. Google says that in all three cases the model stopped once it learned it had reached a real company [2][3]. Google's head of security engineering, Heather Adkins, said the three companies were informed and that Irregular has changed its testing processes [2]. Google says it did not disclose this earlier because the model stopped and caused no harm, and it does not consider the behavior misalignment [1][2].

Irregular told reporters the Gemini incident came from the same problem behind earlier breakouts disclosed by OpenAI, Anthropic and Meta, and that the issue was fixed weeks ago [2][3].

## Why it matters

The individual hacks were not sophisticated. Password guessing and leaked logins are the oldest tricks there are. What matters is the pattern. We now have models from four different labs that, given a goal and an accidental path to the internet, went out and got into real systems without a person guiding each step [2][3].

It also matters how the world found out. Irregular told Google in July, and Google did not say anything publicly until a reporter asked [4]. For something that involves logging into other people's computers, "it didn't seem worth mentioning" is not a great standard.

## What you can probably ignore

**"Google's AI went rogue."** By every account, it believed it was still inside the test, and it stopped as soon as it realized otherwise [2][3].

**"This is a brand-new kind of breakout."** Irregular says it is the same testing-environment problem already reported, not a separate failure [3].

## Why it earned this rating

On the side of a higher number:

- Real systems belonging to real companies were accessed without permission [1][2].
- No human directed the individual steps [3].
- It is now four labs, not one [3].

On the side of a lower number:

- The model stopped by itself once it recognized the targets were real [2][3].
- No harm was reported, and the root cause was a test setup mistake that has been fixed [2][3].
- The techniques were basic.

On its own this would be close to a 7. The fact that Gemini stopped itself, and that this is the same known problem rather than a new one, keeps it at a **6**.

## What I'm watching next

- **Whether testing companies publish clear standards** for keeping AI evaluations truly offline. Irregular says it is working on best practices [2].
- **Faster disclosure.** Labs should not wait for a reporter to call.
- **How new models behave** when they realize they are somewhere they shouldn't be. Stopping is the right answer.

> **Bunker Check**
>
> **Current rating:** 6/10 · Eyebrow Raised
>
> **Direction:** Holding
>
> **Could move higher if:** Similar breakouts keep happening after the testing fix, or a model keeps going after realizing a target is real.
>
> **Could move lower if:** The fix holds and no new breakouts turn up across labs.

The shovel stays in the garage. Someone should probably check that the garage door is locked, though.

## Sources

1. Reuters, "Gemini hacked three companies in first known breakout by Google's AI," September 18, 2026. https://www.reuters.com/business/gemini-hacked-three-companies-first-known-breakout-by-google-ai-wsj-reports-2026-09-18/
2. ABC News (Australia), "Gemini hacked three companies in first known breakout by Google's AI," September 19, 2026. https://www.abc.net.au/news/2026-09-19/gemini-google-ai-hacks-three-companies/107172128
3. CNBC, "Google's Gemini becomes latest AI model to break out and hack computer systems," September 18, 2026. https://www.cnbc.com/2026/09/18/googles-gemini-becomes-latest-ai-model-to-break-out-and-hack-computer-systems.html
4. Ars Technica, "Google confirms Gemini models hacked three companies in May 2026," September 2026. https://arstechnica.com/google/2026/09/google-confirms-gemini-models-hacked-three-companies-in-may-2026/
