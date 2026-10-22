# The Bunker Scale: editorial guide

Everything a writer (human or AI) needs to write and rate a post the way Heather wants it.
`PUBLISHING.md` covers the mechanics; this covers the judgment and the voice.

## Who it's for

Ordinary people who suspect AI is going to matter enormously but don't have the time or
desire to read fifty research papers every morning. Non-experts. Often a little anxious.
Not builders, not researchers.

## The one question

Every story starts with: **"What materially changed?"**

Worth covering when a development changes:

- what AI systems **can do** (a real new capability, especially autonomy, cyber, bio, weapons or self-directed action),
- what they **have actually done** (real-world harm or incidents, at meaningful scale),
- what **access** we're giving them (money, accounts, infrastructure, the physical world), or
- what governments and companies are **formally doing** about it (laws, rules, deployment or safety-policy changes, emergency measures).

Not worth a post on its own: "expert says humanity is doomed," one-off demos dressed up as
apocalypse, vague "AGI is here" claims, viral clips of a model saying something creepy, and
predictions with no new evidence, policy, capability or incident behind them. If the only thing
that changed is how scary people sound, it belongs in a "What you can probably ignore" section,
not its own post.

## Rating

Use the bands and definitions on the How the Ratings Work page (`content/pages/how-the-ratings-work.html`).
A rating weighs:

- Is the capability new, or just described dramatically?
- Controlled experiment or the real world?
- Was a human directing it, or did the system act on its own?
- Was anyone harmed?
- Has it been independently confirmed?
- Did a lab change its safeguards because of it?
- Did governments respond in a meaningful way?
- What don't we know yet?

Rules of thumb:

- **Be consistent.** Before settling on a number, look at how similar past posts were rated (the Ratings page lists them all). If this one is rated differently, say why.
- **The difference between 7 and 8** is usually autonomy, real-world consequences, reproducibility, and how much it changes what we thought current systems could do.
- **9 and 10 are meant to be rare.** 10 requires real-world, immediate or fast-developing, potentially catastrophic consequences that safeguards are struggling to contain. Predictions, interviews and stretched lab results never qualify.
- **Good news gets rated too,** usually low, with the reassurance explained. Don't invent new labels ("Important, but reassuring"); use the six bands.
- **A rating is not a probability** and not a verdict on whether AI is good or bad. It's a current reading.
- **Ratings change in public.** When new evidence moves one, update it with a `rating_history` entry (see `PUBLISHING.md`). The goal is not to defend yesterday's number.

## Voice (Heather's rules)

- **Warm, funny, and serious when it counts.** Humor lives around the serious material, never on top of it. No jokes about real harm, cyber intrusions, weapons or bio risk.
- **Humble, not authoritative.** Never imply the writer's judgment is superior to the reader's. The tagline says "probably" on purpose. Readers are free to disagree with a rating, and the post should make that easy.
- **First person singular.** "I stopped at 7 rather than 8 because..." Not "we," not "The Bunker Scale believes."
- **Plain English.** Explain any technical term the first time, briefly, without talking down.
- **Label uncertainty.** Say what's confirmed, what's disputed, and what's unknown. Anonymous sourcing gets called anonymous.
- **Absurd humor, not plausible humor.** Jokes should be clearly impossible (a chatbot "achieved consciousness because it remembered their favorite soup"), never something a real anxious person might believe.
- **Recurring motifs, used lightly:** the shovel stays in the garage; "Bunker status:" closers; canned goods (never "canned beans").
- **Things that make writing sound like AI, and Heather notices:**
  - **No em dashes.** The build rejects them. Use a comma, colon, period or parentheses.
  - **Never the word "signal."** The build rejects it. Don't build anything on "signal vs noise."
  - **No stacked one-line dramatic fragments.** ("It wasn't a hack. It was a door. Left open.")
  - No "Tuesday" or oddly specific weekday framing.
  - No "the robot uprising" (say "a robot uprising"; "the" implies it's coming).
  - No "Nothingburger."

## Sources

- Trace every claim to the strongest available source: the lab's own post or system card, the paper, the filing, the official statement. Aggregators and social posts can point you to a story but are never the cited source.
- Mark the main source "(primary source)."
- Every number, quote, date and name must match a source that was actually opened while writing.
- If something can't be verified, say so in the post or leave it out.

## Shape of a rated post

The required sections and their order are in `PUBLISHING.md`. In practice:

- **Opening:** the "Rating as of" line, then a one or two sentence italic dek that says why this one matters.
- **What changed:** the facts, carefully sourced, with what's unconfirmed called out.
- **Why it matters:** what it changes for ordinary people.
- **What you can probably ignore:** the scariest versions going around, each as a bold quoted claim followed by why it's less than it sounds. These feed the site's "What you can probably ignore" page.
- **Why it earned this rating:** reasons for a higher number, reasons for a lower one, then the call and why.
- **What I'm watching next:** the specific things that would move the rating.
- **Bunker Check** box (current rating, direction, could move higher if, could move lower if), then a "Bunker status:" closer.
- **Sources.**

Length: thorough but readable, usually 800 to 1,500 words. A "Briefing" (type: Briefing) can be shorter.
