#!/usr/bin/env python3
"""Style check for Bringing AI Home. Enforces the checkable rules in STYLE.md.

Usage:  python3 scripts/stylecheck.py [files...]   (default: every .html page in the repo root)
Exit code 0 = clean, 1 = problems found. Standard library only.
"""
import re
import sys
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SITE_CSS = ROOT / "assets" / "site.css"

PRIVACY_LINE = "Names, faces, and details are changed or invented to protect a real family."

# Words and phrases that never appear in visible text (STYLE.md, Voice and Naming).
BANNED = {
    r"\bthe patient\b": 'say the person\'s name ("Susan"), not "the patient"',
    r"\bdyads?\b": "jargon; say what you mean in plain words",
    r"\bJetson\b": "NVIDIA trademark; our home-compute node is Mojo",
    r"\bclinical depression\b": "overstates the source; see STYLE.md, Numbers and claims",
}
# Only white is allowed as a raw color in pages; everything else is a token in site.css.
ALLOWED_HEX = {"#fff", "#ffffff"}


class Page(HTMLParser):
    """Collects what the checks need: visible text by line, classes used, ids, links, and so on."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack = []
        self.text = []            # (line, text) of visible text
        self.classes = set()
        self.ids = set()
        self.footnotes = []       # (line, href) of <sup><a href="#...">
        self.imgs_without_alt = []
        self.html_lang = None
        self.has_title = False
        self.has_description = False
        self.links_site_css = False
        self.footer_text = []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        line = self.getpos()[0]
        if tag not in ("meta", "link", "img", "br", "input"):
            self.stack.append(tag)
        for c in (a.get("class") or "").split():
            self.classes.add((c, line))
        if a.get("id"):
            self.ids.add(a["id"])
        if tag == "html":
            self.html_lang = a.get("lang")
        if tag == "meta" and a.get("name") == "description" and a.get("content"):
            self.has_description = True
        if tag == "link" and a.get("rel") == "stylesheet" and (a.get("href") or "").endswith("assets/site.css"):
            self.links_site_css = True
        if tag == "img" and not a.get("alt"):
            self.imgs_without_alt.append(line)
        if tag == "a" and "sup" in self.stack and (a.get("href") or "").startswith("#"):
            self.footnotes.append((line, a["href"][1:]))

    def handle_endtag(self, tag):
        if tag in self.stack:
            while self.stack and self.stack.pop() != tag:
                pass

    def handle_data(self, data):
        if "script" in self.stack or "style" in self.stack:
            return
        if "title" in self.stack and data.strip():
            self.has_title = True
        if data.strip():
            self.text.append((self.getpos()[0], data))
            if "footer" in self.stack:
                self.footer_text.append(data)


def css_classes(css):
    css = re.sub(r"/\*.*?\*/", "", css, flags=re.S)
    selectors = re.sub(r"\{[^{}]*\}", " ", re.sub(r"@media[^{]*\{", "", css))
    return set(re.findall(r"\.([A-Za-z_][\w-]*)", selectors))


def check(path):
    src = path.read_text(encoding="utf-8")
    problems = []

    def add(line, msg):
        problems.append(f"{path.name}:{line}: {msg}")

    page = Page()
    page.feed(src)

    # Voice: em-dashes and banned words in visible text
    for line, text in page.text:
        if "—" in text:
            add(line, 'em-dash (—); use a period, colon, or parentheses (STYLE.md, Voice)')
        for pattern, why in BANNED.items():
            for m in re.finditer(pattern, text, re.I):
                add(line, f'"{m.group(0)}": {why}')
        # Internal field names such as dog_name leaking into the page
        for m in re.finditer(r"\b[a-z]+_[a-z_]+\b", text):
            add(line, f'"{m.group(0)}" looks like an internal field name; write it in plain words (STYLE.md, Privacy)')

    # Colors: raw hex values in the page (inline <style> or style="")
    for n, line_text in enumerate(src.splitlines(), 1):
        for m in re.finditer(r"#[0-9a-fA-F]{3,8}\b", line_text):
            before = line_text[:m.start()]
            if before.rstrip().endswith(("href=\"", "href='")) or 'href="' + m.group(0) in line_text:
                continue  # an in-page link like href="#src1"
            if m.group(0).lower() not in ALLOWED_HEX:
                add(n, f"raw color {m.group(0)}; use a token from assets/site.css (STYLE.md, Palette)")

    # Classes: every class used must be defined in site.css or the page's own <style>
    inline_css = "\n".join(re.findall(r"<style>(.*?)</style>", src, re.S))
    defined = css_classes(inline_css)
    if page.links_site_css:
        defined |= css_classes(SITE_CSS.read_text(encoding="utf-8"))
    for cls, line in sorted(page.classes, key=lambda x: x[1]):
        if cls not in defined:
            add(line, f'class "{cls}" is used but never defined (STYLE.md, Visual system)')

    # Page basics
    if not page.html_lang:
        add(1, '<html> is missing lang="en" (STYLE.md, Accessibility)')
    if not page.has_title:
        add(1, "missing <title> (STYLE.md, Accessibility)")
    if not page.has_description:
        add(1, 'missing <meta name="description"> (STYLE.md, Accessibility)')
    if not page.links_site_css:
        add(1, "does not link assets/site.css (STYLE.md, Visual system)")
    for line in page.imgs_without_alt:
        add(line, "image without alt text (STYLE.md, Accessibility)")

    # Footnotes point at an existing source
    for line, target in page.footnotes:
        if target not in page.ids:
            add(line, f'footnote links to "#{target}" but no element has that id (STYLE.md, Numbers and claims)')

    # Privacy: any page that shows the family carries the standard line in its footer
    visible = " ".join(t for _, t in page.text)
    if "Susan" in visible and PRIVACY_LINE not in " ".join(" ".join(page.footer_text).split()):
        add(1, f'mentions the family but the footer lacks the privacy line: "{PRIVACY_LINE}" (STYLE.md, Privacy)')

    return problems


def main(argv):
    files = [Path(a) for a in argv] or sorted(ROOT.glob("*.html"))
    problems = [p for f in files for p in check(f)]
    for p in problems:
        print(p)
    if problems:
        print(f"\n{len(problems)} style problem(s). See STYLE.md for the rules.")
        return 1
    print(f"Style check passed ({len(files)} page(s)).")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
