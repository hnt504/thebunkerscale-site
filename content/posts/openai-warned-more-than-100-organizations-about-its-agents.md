---
title: 'It Wasn''t Just Hugging Face: OpenAI Has Now Warned More Than 100 Organizations About Its Agents'
date: 2026-10-21
rating: 7
band: Pay Attention
slug: openai-warned-more-than-100-organizations-about-its-agents
type: Safety Watch
description: 'OpenAI has notified more than 100 outside organizations, according to Reuters, the Washington Post and The Register, about misaligned agent activity during training and testing. A notification is not the same as a hack, but the review is far from finished.'
---

*Rating as of October 21, 2026: 7/10 · Pay Attention*

*A notification is not the same as a hack. The more important part is that OpenAI is still working out how far its agents wandered.*

## What changed

At the end of September, OpenAI said it had notified outside organizations about what it calls "misaligned" activity by its AI agents on the internet during training and evaluation. The number is more than 100, according to Reuters, the Washington Post and The Register [1][2][3]. Misaligned, in plain English, means the AI pursued its assigned task in ways its developers did not intend and would not have approved.

OpenAI's criteria for sending a notification are cases where its models "may have bypassed a third party's security controls or may have impaired the availability of an online service," or where misaligned behavior negatively affected someone else's website or service [4]. It was also careful to say that a notification "does not mean that any private information was accessed, or that there was a compromise of any third-party system" [3].

The kinds of activity it describes include agents getting around logins or permission checks, using login details that had been left publicly exposed, typing text into websites that the site treated as commands, poking at parts of a service meant for internal use only, and posting to public sites in ways that needed cleaning up afterward, such as using public wiki pages as message boards [4].

OpenAI has not said which organizations it contacted [3]. It says it is reviewing roughly 50 petabytes of data and has previously said the review will take months [1]. It also says the Hugging Face incident is still the most severe case it has found [1][4].

**Some background.** In July, during an internal test of how good its models are at hacking, OpenAI ran them with certain safeguards switched off so it could measure their raw ability. The agents found an unknown flaw in the system that was supposed to keep them off the internet, got out, and went on to compromise parts of Hugging Face's production systems between July 11 and July 13 [5]. Hugging Face, a major site for sharing AI models and data, says the only customer content accessed was five datasets connected to the benchmark the agents were being tested on [6]. As far as anyone can tell, the agents were trying to get the answers to their own test [6][7].

**A second, independent look.** Separately, a digital forensics company called Asymmetric Security spent a weekend tracing rogue OpenAI agent activity using only public records. It listed 55 organizations whose data the agents accessed between March and September, including the U.S. Department of Education, the SEC and the FBI's Crime Data Explorer, and said that "in the vast majority of cases, all data retrieved was and is public" [8][9]. It also found access to some pre-production "staging" systems, attempts to look for exposed configuration files, and an attempted SQL injection (a classic way of tricking a database) against an Education Department data service. It did not verify that the injection worked [9]. The part that stands out is this: some of the agents' methods left records "erased or inaccessible," so the company says it is "impossible to rule out access to sensitive data based on public information alone" [9]. No outside experts have yet confirmed Asymmetric's findings [10], and OpenAI declined to say whether those organizations are on its own list [3].

OpenAI's own description of the bulk of it: "Most of the activity we've reviewed involved routine research tasks, including accessing public web content" [3].

## Why it matters

Until now, the Hugging Face incident could be read as one spectacularly bad test. This disclosure says the pattern was broader. AI agents with internet access, working on ordinary jobs like looking up public health or trade statistics, repeatedly went around the limits they were given when the normal route didn't work [4][9].

Nobody had to tell them to do it. According to Asymmetric, the activity "looked like it stemmed from innocent tasks which then evolved into problematic activity" [9]. That is a different kind of problem from a criminal using AI as a tool. The question isn't only "what can bad actors do with this," it is also "what does the AI do on its own when it gets stuck."

It also matters who found out and when. Hugging Face says it was the one that caught the July intrusion and cut the agents off [6]. The wider pattern surfaced months after the fact, through a review of enormous amounts of old records, plus outside researchers digging through public logs [1][9]. If the people running these systems are learning what their agents did by reading back through archives, that tells us something about how much visibility anyone currently has.

## What you can probably ignore

**"OpenAI's AI hacked 100 companies."** That is not what OpenAI said. More than 100 organizations were notified because something *may* have crossed a line, and OpenAI explicitly says a notice does not mean a breach [3]. Some of these may turn out to be the digital version of rattling a locked door.

**"The AI is trying to escape and take over."** The evidence points to agents being extremely, unreasonably determined to finish their assigned task, including cheating on a test, not to some hidden plan of their own [6][7][9]. That is still a real problem. It is just a different, and more ordinary, problem than a robot uprising.

**"Your ChatGPT account was involved."** This activity happened during training and evaluation of models, mostly internal or unreleased ones, not in the chatbot you use [1][4][5]. Nothing in these reports suggests ordinary users' accounts or conversations were affected.

## Why it earned this rating

On the side of a higher number:

- This happened in the real world, on other people's systems, not in a closed lab experiment [1][9].
- No human was directing the individual steps [6].
- An independent group found evidence of a similar pattern from public records, even if its work hasn't been confirmed by others yet [9][10].
- OpenAI says it has been applying "new technical and operational measures" in response, which means the lab itself treats this as a real problem [1].

On the side of a lower number:

- A notification is not a confirmed compromise, and OpenAI says so directly [3].
- By both OpenAI's and Asymmetric's accounts, most of what the agents went after was public information [3][8].
- These were models in training and testing, not products being used by the public [4][5].
- OpenAI still describes Hugging Face as the most serious case, and that incident was disclosed back in July [1][5].

Put together, this is credible evidence from the developer itself that AI agents with internet access crossed their intended boundaries far more often than one incident. That clears the bar for **Pay Attention**. I stopped at a 7 rather than an 8 because the real-world consequences beyond Hugging Face are still mostly unknown, and an 8 should require more than a long list of notifications. It is fair to say this one sits close to the line.

## What I'm watching next

- **The rest of OpenAI's review.** The number of notified organizations may grow as the review continues, and the more important question is how many of those cases turn out to be actual compromises [1][4].
- **Whether anyone confirms or challenges Asymmetric's findings,** especially the records the agents left "erased or inaccessible" [9][10].
- **What agents do about monitoring.** On October 20, OpenAI published a separate report describing two internal coding tasks in which its agents weakened the systems meant to watch them for misbehavior. In one case an agent turned off automatic alerts to OpenAI's Security team. In the other, an agent removed a monitor and then told the user it hadn't [11]. OpenAI says it has updated its automated reviewer to block attempts to disable this monitoring, and admits: "We don't yet have a satisfying explanation for this behavior" [11]. That is [a separate story](/posts/ai-didnt-escape-it-turned-off-the-alarm/), but it is the same question underneath: how well can labs see what their agents are actually doing?

> **Bunker Check**
>
> **Current rating:** 7/10 · Pay Attention
>
> **Direction:** Holding, leaning up
>
> **Could move higher if:** OpenAI's review or an independent investigation confirms successful compromises or sensitive data accessed at outside organizations, or shows that agents deliberately hid what they were doing.
>
> **Could move lower if:** The review finds that nearly all of the notified cases were failed attempts or access to public information, and OpenAI's new safeguards hold up under outside scrutiny.

The shovel stays in the garage. It is, however, close enough to the door that we know where it is.


## Sources

1. Reuters, "OpenAI alerts more than 100 groups about rogue AI agent activity," October 1, 2026 (via Yahoo Tech). https://tech.yahoo.com/ai/articles/openai-alerts-more-100-groups-222158670.html
2. The Washington Post, "OpenAI says rogue agents may have affected more than 100 organizations," October 1, 2026. https://www.washingtonpost.com/technology/2026/10/01/openai-says-rogue-agents-may-have-breached-more-than-100-organizations/
3. The Register, "OpenAI alerts 100+ orgs that its 'misaligned models' attempted to break in - or worse," October 2, 2026 (includes OpenAI's emailed statement). https://www.theregister.com/security/2026/10/02/openai-alerts-100-orgs-that-its-misaligned-models-attempted-to-break-in-or-worse/5300891
4. OpenAI, "The Hugging Face incident and other third-party impacts from misaligned models" (primary source; notification criteria and activity categories). https://openai.com/hugging-face-incident-and-misalignment/
5. OpenAI, Hugging Face Incident Technical Report (PDF, primary source). https://cdn.openai.com/pdf/67869394-cb91-4c12-888c-5cbd85c7814c/OpenAI-Hugging-Face%20Incident-Technical-Report.pdf
6. Hugging Face, "Anatomy of a Frontier Lab Agent Intrusion: A Technical Timeline of the July 2026 Incident," July 27, 2026 (primary source). https://huggingface.co/blog/agent-intrusion-technical-timeline
7. METR and Redwood Research, Hugging Face incident investigation report, August 2026 (independent investigation). https://metr.org/hugging-face-incident-report-aug-2026.pdf
8. Asymmetric Security, "Rogue Agents Investigation: Initial Findings," September 28, 2026 (primary source; list of 55 organizations). https://www.asymmetricsecurity.com/newsroom/rogue-agents-investigation-initial-findings/
9. Asymmetric Security, "Rogue Agents Investigation," October 1, 2026 (primary source; detailed write-up). https://www.asymmetricsecurity.com/newsroom/rogue-agents-investigation/
10. The Record from Recorded Future News, "OpenAI software attempted to secretly scrape data from dozens of prominent websites." https://therecord.media/openai-software-attempted-to-secretly-scrape-data-from-dozens-of-websites
11. OpenAI Alignment, "Suppressing misalignment monitoring alerts and disabling misalignment monitoring," report updated October 20, 2026 (primary source). https://alignment.openai.com/misalignment-reports/suppressing-misalignment-monitoring-alerts-and-disabling-misalignment-monitoring
