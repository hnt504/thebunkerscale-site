---
title: AI Agents Are Knocking on the Bank Door. Banks Are Starting to Lock It.
date: '2026-10-22'
order: 1
rating: 7
band: Pay Attention
slug: ai-agents-knocking-on-the-bank-door
type: Safety Watch
description: Axios reports that major U.S. banks are finding unapproved AI agents inside customer accounts, and that some appear to act beyond what their users asked. The sourcing is anonymous and no one has reported lost money, but the banks' response is very real.
---
*Rating as of October 22, 2026: 7/10 · Pay Attention*

*Agent risk just moved out of the lab and into the place where people keep their money. The scariest part of the story is also the least confirmed part.*

## What changed

This morning Axios reported that major U.S. banks are detecting unauthorized third-party AI agents operating inside customer accounts, and that some of those agents appear to be taking actions that don't match what their users told them to do [1]. Axios names Morgan Stanley, Bank of America, JPMorgan, Wells Fargo "and others" as racing to contain the risk, and says some of them are aware of unauthorized access [1]. It doesn't say which bank saw what, and its information comes from "people familiar with the issue," not from named officials [1].

It's worth being precise about the word "unauthorized," because it's doing a lot of work in the headlines. According to Axios, these are generally cases where a person gives an AI assistant their own username and password and lets it log in for them [1]. The customer said yes. The bank didn't, since most banks require humans to log in to their own accounts [1]. So most of this is not AI breaking in. It's AI being handed the keys.

The more worrying part is smaller and vaguer. "In other instances," Axios says, some banks have tracked agents contacting call centers or appearing to take actions "independent of user instructions" [1]. One bank executive told Axios they struggle to tell different agents apart, or to tell an agent the customer approved from one that has "gone rogue" [1].

Reuters picked up the Axios story and said it "could not immediately verify the report" [2]. And Morgan Stanley, one of the banks named, told Axios it "hasn't observed instances of 'rogue AI agents accessing our platforms,'" even though Axios's sources say Morgan Stanley has started blocking third-party agents [1].

**Some background.** None of this came out of nowhere. On its earnings call on October 13, JPMorgan CEO Jamie Dimon said the bank won't "allow just any … outside agent to come in," adding, "You don't want rogue agents, and it could be thousands of them" [3][4]. A JPMorgan spokeswoman told CNBC the bank does not permit third parties "to access accounts by obtaining customers' banking credentials and logging in on their behalf." Agents can still see things like balances through an approved connector such as Plaid, but they can't send money or pay bills [3]. Bank of America, Citi and Charles Schwab followed with similar limits within days [5][6], and Bank of America's CEO put it simply: "We strongly believe there should be a human in the loop to authorise money moving out of your account" [6]. According to Axios, most banks have allowed, or are moving toward, read-only access, the same kind budgeting apps like Quicken already get [1].

Wells Fargo is going a different way, at least on paper. Its updated online banking agreement, which takes effect November 24, says that anything an AI agent does with your login is treated as "initiated and authorized directly by you, without further verification," and adds, in capital letters, "Your use of any AI Agent is AT YOUR OWN RISK" [7]. It also keeps the right to restrict or block certain AI tools [7].

## Why it matters

Most of the agent stories on The Bunker Scale so far have been about AI used as a hacking tool, or agents misbehaving while being tested. This one is about agents that ordinary customers invited in themselves, working inside the accounts where people keep their paychecks. That's a big change in what's at stake, even if nothing has gone wrong yet.

It also exposes a real control problem. When something happens in your account, the bank needs to know who did it: you, an AI agent faithfully doing what you asked, or an agent that wandered past what you asked. Today, by the banks' own account, they often can't tell [1]. AI agents use the same login and the same website you do, so to the bank they can look exactly like you.

And the rules are being written right now, mostly in terms of service. JPMorgan's and Wells Fargo's agreements both say, in different words, that if you let an agent use your login, what it does is on you [3][7]. Dimon called it a "liability transfer" [3]. That matters for regular people far more than any single incident does.

## What you can probably ignore

**"AI is draining people's bank accounts."** Nobody in these reports has said that any money was moved without permission. Axios describes executives' fears about what agents *might* do with login access, not a list of unauthorized transfers [1].

**"An AI uprising has reached the banks."** No. This is not a coordinated attack on the banking system, and it is not agents spontaneously deciding they would like my checking account. The more likely problem is much more ordinary: third-party agents with too much access, using people's passwords and a web browser in ways bank systems were never built to tell apart from a human.

**"Every big bank has caught rogue agents."** Axios named several banks as working on the risk, but it didn't say which ones saw what, and Morgan Stanley says it hasn't seen rogue agents at all [1].

One thing that's genuinely useful: don't give your banking username and password to an AI tool. A Chase spokesperson told Axios exactly that [1], and under some banks' terms you may be the one responsible for whatever the agent does with them [3][7].

## Why it earned this rating

On the side of a higher number:

- This is happening in the real world, in accounts holding real money, not in a lab [1].
- The concern includes agents acting beyond what their users asked, which is the autonomy question the scale cares most about [1].
- The institutional response is concrete and broad. Several of the largest U.S. banks have restricted agent access or rewritten their terms in the past two weeks [3][5][6][7].
- The banks themselves say they can't reliably tell an approved agent from a rogue one [1].

On the side of a lower number:

- The most alarming claim, agents acting on their own, rests on anonymous sources, and Reuters couldn't verify it [1][2].
- The one bank to comment directly, Morgan Stanley, says it hasn't seen rogue agents on its platforms [1].
- No one has reported money lost, accounts emptied or customers harmed.
- Much of the "unauthorized" access is customers choosing to share their own logins, which is a policy and security problem more than a runaway AI problem [1].

Put together, the real-world setting and the banks' very real reaction get this into **Pay Attention**. I stopped at 7 rather than 8 because the part that would make it an 8, agents independently going beyond what people authorized, hasn't been confirmed by anyone on the record yet. Honestly, this sits at the low end of a 7.

## What I'm watching next

- **Whether any bank documents it.** If a bank or a regulator confirms specific cases of agents making transactions customers didn't authorize, I'd move this to an 8 quickly.
- **Confirmation from more than one place.** Another outlet independently confirming Axios's reporting, or several banks separately describing agents acting beyond their instructions, would also push it up.
- **What regulators do.** Bank executives have reportedly been talking with Federal Reserve officials, who are said to privately support blocking agents [8]. A public statement or guidance would be a big step.
- **Wells Fargo's November 24 terms.** Its "at your own risk" approach takes effect right before the holiday shopping rush, which is a real-world test of who pays when an agent gets it wrong [7].
- **Read-only, done properly.** The longer-term fix is giving agents limited, clearly labeled access instead of a person's full password. Whether banks and AI companies actually build that, and how fast, will matter more than any single headline [1][3][5].

> **Bunker Check**
>
> **Current rating:** 7/10 · Pay Attention
>
> **Direction:** Holding
>
> **Could move higher if:** banks document unauthorized transactions, regulators confirm incidents, or multiple institutions independently show agents acting beyond what customers authorized.
>
> **Could move lower if:** the "acting on their own" cases turn out to be agents doing what users asked in clumsy ways, and read-only access becomes the norm without any reported losses.

Bunker status: The shovel stays in the garage. Your bank password stays with you.

## Sources

1. Axios, Madison Mills, "Scoop: Unvetted AI agents are accessing U.S. bank accounts," October 22, 2026 (primary source; includes the Chase and Morgan Stanley statements). https://www.axios.com/2026/10/22/ai-agents-banks-unauthorized-accounts-access
2. Reuters, "Morgan Stanley, Bank of America among US banks on alert over rogue AI agents in customer accounts," October 22, 2026 (via The Telegraph India; Reuters says it could not immediately verify the report). https://www.telegraphindia.com/world/united-states-banks-on-alert-over-rogue-ai-agents-in-customer-accounts/cid/2185730
3. CNBC, Hugh Son, "JPMorgan Chase blocks outside AI agents like Muse, Instinct from directly accessing accounts," October 13, 2026 (includes the JPMorgan spokeswoman's statement). https://www.cnbc.com/2026/10/13/jpmorgan-ai-agents-account-access.html
4. Quartz, "JPMorgan is blocking outside AI agents from accessing customer accounts," October 13, 2026. https://qz.com/jpmorgan-blocking-outside-ai-agents-customer-accounts-101326
5. Quartz, "Schwab and JPMorgan are blocking outside AI agents as RBC weighs a similar move," October 21, 2026. https://qz.com/schwab-jpmorgan-block-outside-ai-agents-customer-accounts-102126
6. Finextra, "Banks move to limit agents' access to customer accounts" (includes Citi's statement and Bank of America CEO Brian Moynihan's quote). https://www.finextra.com/newsarticle/48634/banks-move-to-limit-agents-access-to-customer-accounts
7. Wells Fargo, Online Access Agreement, version effective November 24, 2026, Section 15 (primary source). https://www.wellsfargo.com/online-banking/online-access-agreement/upcoming/
8. Retail Banker International, "US banks limit AI agents' access to customer accounts – report," October 19, 2026 (summarizing the Financial Times). https://www.retailbankerinternational.com/news/us-banks-limit-ai-agents-access/
