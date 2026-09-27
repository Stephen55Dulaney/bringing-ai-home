# Bringing AI Home: Style Guide

How these pages sound, look, and protect the family behind them. Read this before adding a page or editing copy.

Every rule below is marked one of two ways:

- **Rule**: already applied across the site. Follow it.
- **Open**: a decision we haven't made yet. Don't treat the current pages as the answer; see [Open decisions](#open-decisions).

---

## 1. Voice

We write for a smart reader who is not in AI: an investor, a caregiver, a grown child worried about a parent. They should never need to decode anything.

### Rules

- **Plain words over jargon.** If a word needs a glossary, cut it. Past examples: "dyad" (cut), "privacy-enforced device" (kept, because it says what it does).
- **No em-dashes (—).** Use a period, a colon, or parentheses instead.
  - Hyphens are fine and required in compound modifiers: *doctor-ready report*, *per-person memory*, *local-first*.
  - En-dashes are fine for ranges: *1959–1969*.
- **Don't replace an em-dash with a comma.** That usually makes a comma splice. Pick the fix that matches the job:

  | Job the dash was doing | Use | Example |
  |---|---|---|
  | Joining two full sentences | Period | "She never invents. If she doesn't know, she says so." |
  | Introducing an explanation or list | Colon | "Susan's People: what Rose remembers" |
  | An aside inside a sentence | Parentheses | "The hyperscalers (Codex, Claude Desktop, the Copilots) are racing…" |

- **No trademarks we don't own**, not even as shorthand. We call our home-compute node **Mojo**, not "Jetson".
- **We, not I.** The site speaks as the company: "We call her Susan." First person singular appears only inside quoted speech.
- **Short sentences carry the emotion.** "He was. He really was." Don't pad them.

### People, not patients

The Rose pages are about dignity. The words have to match.

- **Rule:** Use the person's name ("Susan"). Never "the patient", "the user", or "the subject" in anything a reader sees. That includes sample data and generated card text.
- **Rule:** Describe what someone still has, not what they've lost. "Engage what she still has", not "compensate for her deficits".
- **Rule:** Rose never quizzes and never corrects. Copy and sample dialogue must show this.

### Rose

- **Rule:** Rose is **she**, every time. Never "it", even in a sentence about the hardware. ("Rose lives with the family… She even travels with them.")
- **Rule:** One tense per sentence. If a sentence opens in the present, keep it there.

### Numbers and claims

- **Rule:** Wrap every statistic in `<span class="stat">`.
- **Rule:** Every statistic and research claim gets a numbered footnote (`<sup><a href="#src1">1</a></sup>`) that points to a **Sources** section at the end of the page. Prefer peer-reviewed papers and systematic reviews, and link them by DOI.
- **Rule:** Say only what the source says. Don't write "clinical depression" when the studies used screening questionnaires, and don't write "the strongest intervention" when a systematic review disagrees. When in doubt, soften the wording: "often", "among the most promising".

---

## 2. Naming

Products are named for **a role in the household**, not given a product brand.

| Name | Room | Role |
|---|---|---|
| Mojo | The home brain | Local server that runs the models |
| Mrs. Hudson | The kitchen | House manager |
| Miss Watson | The study | Kids' tutor |
| Rose | The bedside | Caregiver companion |

When naming something new:

1. Would a family say this name out loud without feeling silly?
2. Does it suggest a role in the household, not a feature?
3. Is it clear of trademarks? Check before it goes on a page.

### Every product passes the three questions

Every product and every page should pass the three questions on the home page:

1. Does it live in someone's home?
2. Does it serve the people who live there?
3. Does it run on our substrate (embodied, persistent, local-first, sub-$200 hardware)?

---

## 3. Privacy and sample data

- **Rule:** Real names, faces, and identifying details never appear. Susan is not her real name.
- **Rule:** Every page that shows family content ends with a privacy line in the footer.
- **Rule:** Sample data reads like a real person wrote it. Internal field names (`dog_name`, `relation_type`) never reach the page; write "his dog's name".
- **Rule:** The privacy line reads, word for word: *Names, faces, and details are changed or invented to protect a real family.*
- **Rule:** Every page uses the same fake family:

  | Person | Who they are |
  |---|---|
  | Susan | Has Alzheimer's. Loves "Moon River" and songs from 1959–1969 |
  | Tom | Her husband and primary caregiver. Retired high-school music teacher. Built the dock at the lake house |
  | Emily | Daughter, in Portland. Calls on Sundays. Children Lily (7) and Sam (4) |
  | Michael | Son, lives nearby. Visits on Thursdays. Fixed the porch step |
  | Carol | Susan's younger sister. They grew up in Ohio and sang in the church choir. May live in Florida now (unconfirmed) |
  | Biscuit | Susan's small terrier |

  Add people as needed, but keep these facts consistent from page to page.

---

## 4. Visual system: Editorial Rose

The look is **Editorial Rose**. The structure comes from an editorial-magazine design brief: full-width color blocks, a serif for display, monospace for labels, watermark words, and square cards with hairline borders. The colors come from Rose. (A royal blue version was tried and dropped, because cool blue clashed with Rose's warmth.)

Shared styles live in **`assets/site.css`**: tokens, the base layout, and the common components. Every page links it, plus the Google Fonts stylesheet for Playfair Display and Inter. A page's inline `<style>` holds only what is unique to that page (the dialogue on Rose, the chat mock on the demo). If two pages need the same style, move it into `site.css`. Pages can't be shared as single standalone files; share the link, or the folder.

### Palette

| Role | Color | Token | Contrast |
|---|---|---|---|
| Full-width blocks, banner | Wine `#7d2742` | `--wine` | Cream text 8.7:1 |
| Light sections | Warm cream `#fbf6f4` | `--cream`, `--bg` | n/a |
| Body text, footer block | Plum ink `#2b2228` | `--plum`, `--ink` | 14.4:1 on cream |
| Secondary text | `#6f626a` | `--muted`, `--faint` | 5.4:1 on cream |
| Labels, links on light sections | Rose `#b03a5b` | `--rose`, `--label` | 5.4:1 on cream |
| Accent on wine | Blush `#f2c4d0` | `--blush` | 6.1:1 on wine |
| Cards | White `#fff` | `--card` | n/a |

- **Rule:** Use a token, not a raw hex value. If you need a new color, add a token here with its contrast.
- **Rule:** No cool colors: no blues, grays with a blue cast, or greens. Everything stays in the wine, rose and cream family.
- **Rule:** `--accent` is for thin rules, markers and borders. It is rose on cream and switches to blush inside wine sections automatically.
- **Rule:** Never use pure white for a large background. White is only for cards.

### Tokens flip inside wine sections

Every even `section` inside `.wrap` becomes a full-width wine block, and it redefines the text tokens (`--ink`, `--muted`, `--rose`, `--accent`, `--line`) to light values. Cards, the dialogue box and the chat mock reset them to dark values, so they read correctly on either background. **Practical effect:** color new elements with tokens and they work in both kinds of section without extra rules.

### Typography

| Role | Font | Used for |
|---|---|---|
| Display | Playfair Display, 400–500, italic for quotes | `h1`, `h3`, card names, `.big` / `.lead` openers, closing quote, Rose's lines in dialogue |
| Reading | Inter, 300 (600 for bold) | Body copy, card text, lists |
| Utility | System monospace, 10.5–12px, uppercase, wide tracking | `h2` section labels, kicker, back link, timestamps, source notes, tags, footer |

`h2` is a label, not a headline: mono, uppercase, with a short accent rule before it.

### Components

| Component | Behavior |
|---|---|
| **Banner** | Flat wine, white serif `h1`, mono kicker above, and a huge faded watermark word set with `data-watermark` (HOME, ROSE, PEOPLE, MEMORY) |
| **Back link** | "← Bringing AI Home" in mono, at the top of every page except home |
| **Section** | 88px vertical padding. Alternates cream and wine. One idea per section |
| **Card** | White, square corners, 1px hairline border. `.card.rose` adds a 2px accent line on top for the one card you want clicked |
| **Dialogue** | Rose is always on the **left**; the person she's talking with is on the right. Mono speaker label or timestamp with each line. Rose's lines are wine serif italic. In chat mock-ups, name the classes after the speaker (`.msg.rose`, `.msg.husband`), not "me" and "them" |
| **Images** | Grayscale, framed with a hairline border and white mat |
| **Closing quote** | Each page ends its argument with one serif italic `blockquote`: the line you want remembered |
| **Sources** | Numbered list at the end of the page, linked from `<sup>` footnotes |
| **Footer** | Full-width plum block, mono text, and it always carries the privacy line |

### Accessibility

- **Rule:** Every page has `lang="en"`, a `<title>`, a meta description, and `alt` text on images.
- **Rule:** Text meets WCAG AA contrast: 4.5:1 for small text. Our readers skew older. Every pair in the palette above passes; check any new one before using it.

## 5. Before you commit

### The automated check

`scripts/stylecheck.py` enforces the rules a script can check. It runs on GitHub for every push and pull request (the **Style check** job). A red check means a rule was broken; the output names the file, the line, and the rule.

Run it yourself any time:

```
python3 scripts/stylecheck.py
```

To run it before every commit on your machine, turn on the hook once: `git config core.hooksPath .githooks`. To skip it for a single commit, use `git commit --no-verify`.

It checks:

- **Voice:** no em-dashes; none of the banned words ("the patient", "dyad", "Jetson", "clinical depression")
- **Privacy:** no internal field names like `dog_name` on the page; any page that mentions the family carries the privacy line in its footer
- **Colors:** no raw color values in pages except white; use tokens from `site.css`
- **Classes:** every class used is defined
- **Page basics:** `lang`, a title, a meta description, `alt` text, and a link to `site.css`
- **Footnotes:** every footnote points to a source that exists

To ban a new word, add it to `BANNED` at the top of the script, with the reason.

### Still checked by a person

- [ ] No commas standing in for an em-dash (comma splices)
- [ ] Hyphenated compound modifiers
- [ ] Rose is "she", and the site says "we"
- [ ] Every statistic has a footnote, and the wording matches what the source says
- [ ] Rose is on the left in any dialogue

---

## Decisions

All open decisions are settled: "we" as the point of view, one sample family, one privacy line, footnoted sources, a shared stylesheet, Editorial Rose as the one look, Rose always on the left in dialogue, and an automated style check (see the sections above).
