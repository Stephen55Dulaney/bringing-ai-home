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

## 4. Visual system

Shared styles live in **`assets/site.css`**: tokens, the base layout, and the common components. Every page links it. A page's inline `<style>` holds only what is unique to that page (the dialogue on Rose, the chat mock on the demo). If two pages need the same style, move it into `site.css`.

A page can no longer be shared as a single standalone file; share the link, or the folder.

### Tokens (canonical)

```css
:root{
  --rose:#b03a5b;       /* links, h2 labels, gradient start */
  --rose-deep:#7d2742;  /* h3, names, quotes, gradient end */
  --rose-soft:#f7e7ec;  /* highlighted card, system chips */
  --ink:#2b2228;        /* body text */
  --muted:#6f626a;      /* secondary text (passes AA on white and --bg) */
  --line:#ecdce1;       /* borders and dividers */
  --bg:#fbf6f4;         /* page background */
  --card:#fff;          /* card surface */
  --rose-line:#f0d0da;  /* border of the highlighted card */
  --label:#b76e79;      /* small uppercase labels (fails AA, see below) */
  --faint:#9a8b92;      /* timestamps, source notes (fails AA) */
  --unsure:#b8860b;     /* "Rose is checking this" (fails AA) */
  --max:840px;          /* content width */
}
```

- **Rule:** Use a token, not a raw hex value. If you need a color the tokens don't have, add a token and document it here.
- **Rule:** Define every class you use. (`.muted` was once used on the home page without being defined.)

### Typography

| Element | Spec |
|---|---|
| Body | 17px / 1.7, system font stack |
| Banner `h1` | `clamp()`, tight tracking (−.02em), line-height ≈1.05 |
| Section `h2` | 13px, uppercase, .13em tracking, `--rose`. Works as a label, not a headline |
| `h3` / card title | 16–18px, `--rose-deep` |
| Small labels | 11.5–12.5px, uppercase, bold. Must still meet contrast (see below) |

### Components

| Component | Behavior |
|---|---|
| **Banner** | Rose gradient (135°, `--rose` to `--rose-deep`), white text, a kicker above the `h1`, rounded bottom corners |
| **Back link** | "← Bringing AI Home" at the top of every page except home |
| **Section** | Padding plus a `--line` bottom border. One idea per section |
| **Card** | `--card` surface, `--line` border, radius 14px. Use `.card.rose` for the one card you want the reader to click |
| **Dialogue** | Speaker label above each line. Rose's lines are tinted `--rose-deep` |
| **Closing quote** | Each page ends its argument with one italic `blockquote`: the line you want remembered |
| **Footer** | Muted, 14px, and it always carries the privacy line |

### Accessibility

- **Rule:** Every page has `lang="en"`, a `<title>`, a meta description, and `alt` text on images.
- **Rule:** Text meets WCAG AA contrast: 4.5:1 for small text. Our readers skew older.
- **Open (known failures):** These colors are currently below AA for small text:
  - `#b76e79` room and speaker labels, about 3.8:1
  - `#9a8b92` timestamps and "from what you told her", about 3.2:1
  - `#b8860b` "Rose is checking this", about 3.3:1

  Each is now a token in `site.css`, so the fix is a one-line change per color. Proposed replacements: `--rose-deep` or `--muted` for the labels, and a darker amber for "unsure".

---

## 5. Before you commit

- [ ] No em-dashes, and no commas standing in for one
- [ ] Hyphenated compound modifiers
- [ ] Rose is "she"; people are named, not "the patient"
- [ ] No internal field names or trademarks on the page
- [ ] Privacy line in the footer
- [ ] Every statistic has a footnote, and the wording matches the source
- [ ] Colors come from tokens; every class used is defined
- [ ] `lang`, title, meta description, and `alt` text are present

---

## Open decisions

The current pages don't settle these yet.

| Decision | Options | Current state |
|---|---|---|
| **Rose's side in dialogue** | Always left (she responds) or always right | Left in `rose.html`, right in `cards-demo.html` |
| **Contrast fixes** | Replace the values of `--label`, `--faint`, `--unsure` | Tokenized, values unchanged |
| **Automated checks** | Pre-commit script for em-dashes, banned words, raw hex values, and missing `lang` | Not built |

Decided: "we" as the point of view, one sample family, one privacy line, footnoted sources, a shared stylesheet (see the sections above).
