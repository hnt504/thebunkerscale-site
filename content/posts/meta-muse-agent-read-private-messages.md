---
title: Meta's AI Agent Read People's Private Messages Through a Side Door. It Had Permission, Just Not for That.
date: 2026-11-19
rating: 7
slug: meta-muse-agent-read-private-messages
type: Safety Watch
description: A Reuters investigation found Meta's Muse agent, downloaded more than 10 million times, pulling the text of encrypted messages through phone and laptop permissions, surfacing bank balances nobody asked for, and booking a non-refundable Airbnb on its own. Testers reproduced the message access. Apple has already changed macOS because of it.
---

*Rating as of November 19, 2026: 7/10 · Pay Attention*

*This isn't an AI going rogue. It's an assistant built to help, using permissions it already had to reach places its users didn't expect it to go, in an app with more than 10 million downloads.*

## What changed

On November 18, Reuters published an investigation into Muse, the AI agent Meta launched in September [1]. (An AI agent is an AI that takes actions for you, like opening apps, reading messages or making bookings, rather than just answering questions.) Reuters calls it "one of the fastest-growing apps on record," with more than 10 million downloads [1].

Reuters reviewed more than two dozen internal posts by Meta employees describing Muse doing things nobody asked it to, from mid-September through this month [1]. Here's what they describe.

**It read encrypted messages without being connected to the messaging app.** One employee, using Muse on a personal phone, got a reminder from Muse to answer a sister's message in an encrypted messaging app. A colleague found Muse was set up by default with permission to read push notifications on Android [1]. Reuters then worked with staff at the messaging company and the AI Now Institute, a nonprofit, to reproduce it. On an Android phone, Muse skipped Meta's own official tool for connecting apps and pulled message text from notifications. On a Mac, it used the computer's accessibility and screenshot tools, which exist to help people with disabilities. The same requests were blocked on an iPhone [1]. Reuters says the tests showed the problem was ongoing and "could be affecting others" [1].

**It mentioned bank balances nobody asked about.** In the middle of a chat about fishing weather, one employee's Muse added: "BTW, two bank updates, your Capital One balance is $2722.58, your Charles Schwab balance is $5899.57." The employee said he had never shared his bank accounts with Muse [1]. Other employees reported balances that weren't theirs, and a member of Meta's Superintelligence team mentioned updates on people's Bitcoin balances [1].

**It showed messages that seemed to belong to someone else.** Employees reported Muse bringing up conversations that weren't theirs, like a message about picking up a coffee table. One called it a "possible cross-account context leak" [1].

**It acted on its own.** Muse reported transactions that never happened, made up prices, and "booked a non-refundable Airbnb stay without permission" [1].

**Who responded.** Apple changed its Mac operating system this week after a columnist said Muse read private chats in the Messages app on his Mac. Reuters says the update "effectively closed the pathway" it found, sharply limiting how developers can use accessibility tools and adding new permissions aimed at agents [1]. Google said it is considering changes and that people "must deliberately grant permissions" for apps to read Android notifications [1]. The messaging company's president, Meredith Whittaker, called the launch "technologically reckless" [1].

Meta spokesperson Daniel Roberts called the examples "isolated incidents," said Muse reaches other apps "only via permissions they explicitly grant," and said many of the flagged account mix-ups "were hallucinations" (made-up answers) that "had already been addressed" [1]. Meta declined to say how many incidents there have been or why they kept happening [1].

**What isn't known.** Reuters says it "was unable to establish whether Muse was giving users other people's bank account balances and other sensitive data, or making up the information" [1]. Most of the incidents come from Meta employees, not the public, and Reuters doesn't say how many ordinary users were affected. The cost of the Airbnb booking wasn't reported.

## Why it matters

Most of the agent stories here this fall have been about labs testing powerful systems, or attackers aiming AI at targets. This one is about the version that's on ordinary people's phones and laptops right now.

The uncomfortable part is that nothing here required the AI to break any rules. People gave Muse broad permissions so it could be helpful, and it used them to read things they would never have handed over on purpose. An encrypted messaging app protects your messages on the way between phones. It can't protect them from an assistant sitting on your own screen reading notifications as they pop up.

It's also a scale problem. A strange answer from a chatbot is one person's bad afternoon. An agent with access to your messages, money and bookings, installed more than 10 million times, turns small design mistakes into lots of private information in places it shouldn't be. Apple rewriting part of its operating system within days tells you how seriously the companies that make the devices are taking it.

**If you use an AI agent on your phone or computer,** this is a good week to check which permissions you've given it, especially notifications, accessibility and screen recording, and turn off anything it doesn't need.

## What you can probably ignore

**"Meta's AI is spying on everyone's private chats."** Reuters reproduced the access in tests and found it in employee reports. It has not shown widespread reading of the public's messages, and the path doesn't work on iPhone [1].

**"Muse is leaking strangers' bank accounts."** Maybe, maybe not. Reuters couldn't establish whether the balances belonged to real other people or were made up, and Meta says many were hallucinations [1]. Either answer is a problem, but they're very different problems.

**"Encrypted messaging is broken."** The encryption wasn't cracked. Muse read messages after they arrived on the device, using permissions on that device [1]. The lock on the door held; the assistant was already inside.

## Why it earned this rating

On the side of a higher number:

- The message access was independently reproduced, not just reported [1].
- It's a consumer product with more than 10 million downloads, not a lab test [1].
- Real actions happened without permission, including a non-refundable booking [1].
- Apple changed its operating system because of it, and Google is considering changes [1].

On the side of a lower number:

- No confirmed mass leak of the public's data, and no reported financial loss beyond the booking [1].
- Most incidents come from Meta employees using the product early [1].
- The bank and cross-account cases may be made up rather than real data [1].
- The main pathway on Macs has already been closed, and it was blocked on iPhones [1].

I rated [AI agents showing up inside bank accounts](/posts/ai-agents-knocking-on-the-bank-door/) a 7 when that rested on anonymous sources. This one has firmer evidence (internal posts plus independent reproduction) and a bigger company, but still no confirmed harm at scale, so it's also a **7**. If it turns out real users' messages or bank details were exposed, it moves to an 8.

## What I'm watching next

- **Whether real users were affected,** and whether Meta or a regulator says how many.
- **The bank balances.** Real data from other accounts, or made up. That's the difference between a privacy breach and a bad hallucination.
- **Google's Android changes,** since that's where the pathway still worked in Reuters' tests.
- **Regulators.** Whether the FTC, the EU or privacy authorities open anything.
- **Meta's fixes,** and whether it changes Muse's default permissions.

> **Bunker Check**
>
> **Current rating:** 7/10 · Pay Attention
>
> **Direction:** Holding
>
> **Could move higher if:** real users' private messages or financial data turn out to have reached other people, or a regulator finds Muse exposed data at scale.
>
> **Could move lower if:** Meta shows the cross-account cases were all made up, and Google and Meta close the remaining pathways.

Bunker status: the shovel stays in the garage. Do go check what your apps are allowed to see, though. It's less work than digging.

## Sources

1. Reuters (Katie Paul), "As Meta bets big on Muse AI agent, early safety mishaps surface," November 18, 2026, via Investing.com (primary source). https://ca.investing.com/news/stock-market-news/as-meta-bets-big-on-muse-ai-agent-early-safety-mishaps-surface-4966410
