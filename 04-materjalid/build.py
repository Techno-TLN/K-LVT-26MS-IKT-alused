#!/usr/bin/env python3
"""Md -> A4 PDF (markdown + Chromium). Kasutus: build.py <sisend.md> <valjund.pdf>"""
import sys, markdown
from playwright.sync_api import sync_playwright

CSS = """
@page { size: A4; margin: 0 }
* { box-sizing: border-box }
html { font-family: 'Inter', 'DejaVu Sans', Arial, sans-serif; color: #1a1a1a; font-size: 9pt; line-height: 1.32 }
body { margin: 0; padding: 11mm 13mm 8mm 13mm }
h1 { font-size: 17pt; margin: 0 0 1mm 0; color: #17233b; line-height: 1.15 }
h2 { font-size: 11pt; margin: 3mm 0 1.2mm 0; padding-bottom: 0.7mm; color: #17233b; border-bottom: 1.4px solid #c1662e }
p { margin: 1mm 0 1.4mm 0 }
p.sub { color: #6a7179; font-size: 8.6pt; margin: 0 0 2.6mm 0 }
p.note { color: #6a7179; font-size: 8pt; margin-top: 1mm }
ol, ul { margin: 0.6mm 0 1.4mm 0; padding-left: 5mm }
li { margin: 0.4mm 0 }
table { border-collapse: collapse; width: 100%; margin: 1.2mm 0 1.8mm 0; font-size: 8.4pt }
th, td { border: 1px solid #d6d2c6; padding: 1mm 1.6mm; text-align: left; vertical-align: top }
th { background: #17233b; color: #fff; font-weight: 600 }
tr:nth-child(even) td { background: #f7f6f2 }
code { font-family: 'DejaVu Sans Mono', monospace; font-size: 8.4pt; background: #eef0e9; padding: 0 1mm; border-radius: 1mm }
strong { color: #17233b }
pre { background: #17233b; color: #eef0e9; padding: 1.6mm 2.4mm; border-radius: 1.4mm; margin: 1.2mm 0 1.6mm 0; font-size: 8.4pt }
pre code { background: none; color: inherit; padding: 0 }
"""

def build(src, dst):
    md = open(src, encoding='utf-8').read()
    body = markdown.markdown(md, extensions=['tables', 'md_in_html', 'fenced_code'])
    html = f"<!doctype html><html lang='et'><head><meta charset='utf-8'><style>{CSS}</style></head><body>{body}</body></html>"
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page()
        pg.set_content(html)
        pg.pdf(path=dst, format='A4', print_background=True, margin=dict(top='0', bottom='0', left='0', right='0'))
        b.close()

if __name__ == '__main__':
    build(sys.argv[1], sys.argv[2])
