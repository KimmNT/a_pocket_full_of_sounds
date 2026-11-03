"""Build the human HTML from the canonical Markdown using the existing style."""
from pathlib import Path
import hashlib
import html
import re

base = Path(__file__).resolve().parent
root = base if (base / 'GAME_DESIGN.md').exists() else base.parent / 'outputs'
source = root / 'GAME_DESIGN.md'
target = root / 'A Pocket Full of Sounds - Game Design.html'
text = source.read_text(encoding='utf-8')
old = target.read_text(encoding='utf-8', errors='replace')
style = re.search(r'<style>(.*?)</style>', old, re.S).group(1)

def inline(value):
    value = html.escape(value)
    value = re.sub(r'`([^`]+)`', r'<code>\1</code>', value)
    value = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', value)
    value = re.sub(r'\[([^\]]+)\]\((https://[^\s)]+)\)', r'<a href="\2">\1</a>', value)
    return value

lines = text.splitlines()
parts, headings = [], []
i = 0
while i < len(lines):
    line = lines[i]
    if not line.strip():
        i += 1
        continue
    heading = re.match(r'^(#{1,3}) (.+)$', line)
    if heading:
        level, title = len(heading[1]), heading[2]
        anchor = re.sub(r'[^a-z0-9]+', '-', title.lower()).strip('-')
        parts.append(f'<h{level} id="{anchor}">{inline(title)}</h{level}>')
        if level == 2:
            headings.append((anchor, title))
        i += 1
    elif line.startswith('|'):
        rows = []
        while i < len(lines) and lines[i].startswith('|'):
            rows.append([cell.strip() for cell in lines[i].strip().strip('|').split('|')])
            i += 1
        parts.append('<div class="table-wrap"><table><thead><tr>' + ''.join('<th>' + inline(c) + '</th>' for c in rows[0]) + '</tr></thead><tbody>')
        for row in rows[2:]:
            parts.append('<tr>' + ''.join('<td>' + inline(c) + '</td>' for c in row) + '</tr>')
        parts.append('</tbody></table></div>')
    elif line.startswith('- ') or re.match(r'^\d+\. ', line):
        ordered = bool(re.match(r'^\d+\. ', line))
        tag = 'ol' if ordered else 'ul'
        pattern = r'^\d+\. ' if ordered else r'^- '
        parts.append('<' + tag + '>')
        while i < len(lines) and re.match(pattern, lines[i]):
            parts.append('<li>' + inline(re.sub(pattern, '', lines[i])) + '</li>')
            i += 1
        parts.append('</' + tag + '>')
    else:
        para = [line]
        i += 1
        while i < len(lines) and lines[i].strip() and not re.match(r'^(#{1,3} |\||- |\d+\. )', lines[i]):
            para.append(lines[i])
            i += 1
        parts.append('<p>' + inline(' '.join(para)) + '</p>')

version = re.search(r'^- Version: ([\d.]+)\.$', text, re.M).group(1)
date = re.search(r'^- Updated: (.+)\.$', text, re.M).group(1)
digest = hashlib.sha256(source.read_bytes()).hexdigest()
nav = '<nav aria-label="Document sections">' + ''.join(f'<a href="#{a}">{html.escape(t)}</a>' for a,t in headings) + '</nav>'
extra = 'code{font:0.9em Consolas,monospace;overflow-wrap:anywhere;background:#eef0e6;padding:2px 4px;border-radius:3px}h2{scroll-margin-top:20px}nav{font-size:13px}table{min-width:520px}'
style = style.replace(extra, '').strip()
page = f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>A Pocket Full of Sounds - Game Design</title><meta name="design-version" content="{version}"><meta name="source-sha256" content="{digest}">
<style>{style}\n{extra}</style></head><body><main>
<header><div class="eyebrow">APFS / Game design / Version {version}</div><p class="muted">Updated {html.escape(date)} / Human-readable edition</p><p>Design, decisions, and progress. The companion <code>GAME_DESIGN.md</code> carries the same record for future AI sessions.</p></header>
{nav}
{chr(10).join(parts)}
<footer>Generated from GAME_DESIGN.md. Both editions share version {version}. All game features remain in planning unless explicitly recorded as implemented.</footer>
</main></body></html>'''
target.write_text(page, encoding='utf-8')
assert '\ufffd' not in page
assert not any(ord(c) < 32 and c not in '\n\r\t' for c in page)
assert len(headings) > 0
assert f'content="{digest}"' in page
print(f'Generated HTML v{version}: {len(headings)} sections; Markdown source hash embedded; encoding checks passed.')
