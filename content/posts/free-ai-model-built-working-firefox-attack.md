---
title: A Free AI Model Built Working Attacks on Six Firefox Releases for About $1,000 Each. No Safety Filter Stopped It.
date: 2026-10-31
rating: 6
slug: free-ai-model-built-working-firefox-attack
type: Safety Watch
description: Researchers at Epoch AI say GLM 5.3, an AI model anyone can download, read Firefox's public security fixes and built working attacks that could steal a file from a visitor's computer, before the fixes reached users. It cost about $1,000 per Firefox version and triggered no refusals. The holes are now patched.
---
*Rating as of October 31, 2026: 6/10 · Eyebrow Raised*

*Two days ago I wrote about an unreleased Anthropic model building full break-ins, and said the worry was how long the head start lasts. A downloadable model just did a smaller version of the same trick, for the price of a used laptop.*

## What changed

On October 29, the research group Epoch AI published a report showing that GLM 5.3, an open-weight model (one whose files anyone can download and run) released by the Chinese company Z.ai in August, could turn Firefox's security fixes into working attacks before those fixes reached users [1].

Some background helps here. When browser makers fix a security hole, the fix often becomes visible in their public code before the update actually lands on people's computers. Epoch calls that window "the patch gap" [1]. A skilled attacker can read the fix, work out what was broken, and attack people who haven't updated yet. Doing that has always taken real expertise and time.

Here's what Epoch says GLM 5.3 did [1]:

- **The attack:** it built a webpage that, when a Firefox user visited it, "read a file from the visitor's computer and sent it to the attacker with no further user interaction." Epoch says an attack like this could be used to read saved browser passwords or steal login cookies.
- **How many versions:** all six Firefox releases between September 17 and October 26 (versions 156.0 through 158.0.1), "using only information available at the time of each version's release."
- **The cost:** about $1,000 per new Firefox version at normal pay-per-use prices. Epoch's total research spend on Firefox was over $100,000, mostly building and testing its setup.
- **The speed:** Epoch gave the model up to 48 hours per attempt. The fastest one took 12 hours.
- **How much help it had:** the researchers built the testing setup and pointed the model at the patch gap. After that, Epoch says, "we let the model run autonomously with no user input. The model identified upcoming security fixes, selected vulnerabilities, and built a complex exploit chain on its own."
- **No safety filter fired:** "We did not trigger any safeguards or refusals from any provider, including Z.ai," Epoch writes, even though its actions were "indistinguishable from those of someone attempting to target real users."

There's one more wrinkle. The attacks on the newest versions also relied on a second flaw that hadn't been made public, which the model "rediscovered on each attempt" [1]. Epoch shared it with Mozilla, and it was fixed in Firefox 159.0 on October 27, two days before the report came out [1].

What it **didn't** do matters too. Epoch says it got no "arbitrary code execution" (full control of the computer) on recent Firefox versions, only the file theft described above [1]. The same approach against Google Chrome didn't work, despite about $100,000 spent trying [1]. The model had no internet access during the tests, and Epoch reports no sign of anyone using these attacks in the wild [1]. Epoch says it hasn't confirmed whether the attack still works on Firefox 159.0, but it suspects the fix "should make things at least substantially more difficult" [1].

## Why it matters

Until now, the scariest AI cyber results on this site have come from models locked inside labs: [Anthropic's unreleased research model](/posts/anthropic-unreleased-claude-built-working-exploit-chains/), and Google's [Gemini 4 Argon](/posts/google-gemini-4-argon-restricted-launch/) before it was guarded and released. The labs' answer has been to [keep the strongest versions behind a guest list](/posts/anthropic-cyber-verification-guest-list/). That plan works only as long as the downloadable models are far behind.

This is evidence they aren't that far behind. GLM 5.3 didn't match the Anthropic model, which built complete, working attacks on Chrome, Safari and several operating systems. But it did build a working attack on a browser with over 200 million users, by itself, cheaply, with nobody's safety filter noticing [1]. And once a model's files are out, nobody can add a safety filter later.

Epoch's own conclusion is blunt: giving defenders better locked-down models "does not solve the underlying structural issue" [1]. Their fix is about plumbing, not AI: keep security fixes private until they ship, and ship faster. They also worry about software that updates slowly, like router firmware and phones [1].

For ordinary people, the takeaway is the same boring advice as last time, only more urgent. When your browser says it has an update, let it restart. The gap between "fix exists" and "fix is on your computer" is exactly where this attack lives.

## What you can probably ignore

**"Any hacker can now take over your computer through Firefox."** The attack read a file, it didn't take over the computer, and Epoch couldn't get full control on recent versions [1]. The flaws it used are patched.

**"AI hacked 200 million Firefox users."** This was a research test with no internet access, and there's no evidence it was used on anyone [1].

**"Open AI models are now as dangerous as the locked-up ones."** It worked on Firefox but not on Chrome, and the researchers had to build the setup first [1]. It's a real step, not a tie.

## Why it earned this rating

On the side of a higher number:

- It's a model anyone can download, and no safety filter stopped it [1].
- It built working attacks on real, widely used software, mostly on its own, for about $1,000 a version [1].
- It found and reused an unpublished flaw along the way [1].
- Epoch says patch-gap attacks against Chrome were already seen in the wild in September, though it doesn't say AI was involved in those [1].

On the side of a lower number:

- It was a controlled research test, and nobody was harmed [1].
- The result was file theft, not full control, and the Chrome attempt failed [1].
- The holes are patched, and Mozilla was told [1].
- Skilled humans have been exploiting the patch gap for years. What changed is cost and who can do it.

I put this at **6**, level with [Anthropic's exploit chain report](/posts/anthropic-unreleased-claude-built-working-exploit-chains/). That model was far more capable but locked up; this one is weaker but free and unguarded, and those roughly cancel out. It's also in line with the [PHP security holes](/posts/same-ai-capability-that-can-break-things-can-find-them-first/) at 6, where attackers raced to use fixes before they shipped. It stays below 7 because there's no real-world use and no harm. If someone is caught doing this to real people, it won't stay at 6.

## What I'm watching next

- **Whether the attack still works on Firefox 159.0,** which Epoch hasn't confirmed [1].
- **Newer open models.** Epoch mentions that Kimi K3.1 Pro, which it didn't test, is due to have its files released in early November [1].
- **Changes at Mozilla and Google** to how long fixes sit in public before release.
- **Any sign of AI-built patch-gap attacks in the wild.**

> **Bunker Check**
>
> **Current rating:** 6/10 · Eyebrow Raised
>
> **Direction:** Leaning up
>
> **Could move higher if:** attackers are caught using open models this way against real people, the same approach works on Chrome or phones, or newer open models get full control of the computer.
>
> **Could move lower if:** browser makers close the patch gap and later open models can't repeat the result on updated releases.

Bunker status: the shovel stays in the garage. Your browser's "restart to update" button, however, has earned a little respect.

## Sources

1. Epoch AI, Aiden Ament, Yafah Edelman, Alexander Barry, Timothée Chauvin, Lee Bousfield and Jaeho Lee, "AI can turn security fixes into working exploits before users receive an update," October 29, 2026 (primary source). https://epoch.ai/publications/open-weight-models-patch-gap
