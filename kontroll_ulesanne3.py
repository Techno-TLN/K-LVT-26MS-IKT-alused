#!/usr/bin/env python3
"""Ülesande 3 kiirkontroll õppejõule.

Kasutus:  python3 kontroll_ulesanne3.py kaust_esitustega
          python3 kontroll_ulesanne3.py fail1_ansi.html fail1_utf8.html ...

Iga .html faili kohta: suurus, BOM, baitide põhjal tuvastatud kodeering,
meta charset, kooskõla ja täpitähtede arv. Kui kaustas on paar
*_ansi.html + *_utf8.html, kontrollitakse ka mahu prognoosi:
    S_utf8 = S_ansi + N_t - (len(ansi_nimi) - len(utf8_nimi))
"""
import re
import sys
from pathlib import Path

TAPID = set("õäöüÕÄÖÜ")
META = re.compile(rb'<meta[^>]+charset\s*=\s*["\']?([A-Za-z0-9_\-]+)', re.I)


def analyse(path: Path):
    data = path.read_bytes()
    bom = data.startswith(b"\xef\xbb\xbf")
    nonascii = any(b > 127 for b in data)
    try:
        data.decode("utf-8")
        valid_utf8 = True
    except UnicodeDecodeError:
        valid_utf8 = False
    if not nonascii:
        actual = "ASCII (täpitähti pole)"
    elif valid_utf8:
        actual = "UTF-8" + (" + BOM" if bom else "")
    else:
        actual = "ANSI/8-bitine (mitte UTF-8)"
    m = META.search(data[:1024])
    declared = m.group(1).decode("ascii") if m else None
    text = data.decode("utf-8") if valid_utf8 else data.decode("cp1252", errors="replace")
    if not valid_utf8:
        # ANSI-failis on iga täpitäht 1 bait, loe baitidest (cp1252/cp1257 annavad samad koodid)
        n_t = sum(1 for b in data if b in (0xF5, 0xE4, 0xF6, 0xFC, 0xD5, 0xC4, 0xD6, 0xDC))
    else:
        n_t = sum(1 for c in text if c in TAPID)
    d = (declared or "").lower()
    if declared is None:
        ok = "PUUDUB meta charset"
    elif d == "utf-8" and valid_utf8 and nonascii and not bom:
        ok = "OK"
    elif d in ("windows-1252", "iso-8859-1", "windows-1257") and nonascii and not valid_utf8:
        ok = "OK"
    else:
        ok = "VIGA: silt ja baidid ei klapi"
    return dict(path=path, size=len(data), actual=actual, declared=declared, ok=ok, n_t=n_t, bom=bom)


def main(args):
    files = []
    for a in args:
        p = Path(a)
        files += sorted(p.rglob("*.html")) if p.is_dir() else [p]
    if not files:
        print(__doc__)
        return
    res = {}
    for f in files:
        r = analyse(f)
        res[f.name.lower()] = r
        print(f"{f.name}\n  suurus: {r['size']} B | tegelik: {r['actual']} | meta: {r['declared']} | {r['ok']} | täpitähti: {r['n_t']}")
    for name, a in res.items():
        if name.endswith("_ansi.html"):
            u = res.get(name[: -len("_ansi.html")] + "_utf8.html")
            if not u:
                continue
            diff = len((a["declared"] or "")) - len((u["declared"] or ""))
            pred = a["size"] + a["n_t"] - diff
            flag = "OK" if pred == u["size"] else f"LAHKNEB ({u['size'] - pred:+d} B)"
            print(f"PAAR {name[:-10]}: prognoos {pred} B, UTF-8 tegelik {u['size']} B -> {flag}")


if __name__ == "__main__":
    main(sys.argv[1:])
