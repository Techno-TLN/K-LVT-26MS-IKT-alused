# Kohtumine 3 — Teenuste liigid, riistvararessursid ja teksti kodeerimine

**Kuupäev:** 05.10.2026 (E) · **Kestus:** 2 ak. tundi (90 min)

## Tunni sisu

- Teenuste liigid: SaaS / PaaS / IaaS, pilv vs kohapealne (lühiülevaade). Näited: pilvepõhine failihoidla, Techno-TLN M365 keskkond, kohalik server.
- Riistvararessursid: protsessor, mälu, salvestus, GPU.
- Teksti kodeerimine (ASCII/UTF-8) kui näide andmemahu ja salvestusvajaduse seosest.
- Praktikas: valitud rakenduse tootja spetsifikatsiooni lahtiharutamine (vajalik riistvara).

## Seos ÕV1-ga

Teenuseliigi äratundmine ja rakenduse nõuete sidumine konkreetse riistvaraga. Teenuste liigid said siin lühema käsitluse, et jätta rohkem ruumi riistvara- ja kodeerimisteemale, mis kasutab otseselt [Kohtumine 2](02-arvusysteemid-ja-andmemahu-uhikud.md) arvusüsteeme ja andmemahu ühikuid.

## Tunni kulg (90 min) ja klassiruumi harjutused

| Aeg | Teema | Harjutus |
|---|---|---|
| 00:00 | Ülesande 2 tagasivaade (10 min) | arutelu |
| 00:10 | Teenuste liigid (15 min) | 1. Teenuste kaardisorteerimine („kes haldab mida") |
| 00:25 | Riistvararessursid (20 min) | 2. Süsteeminõuete lugemine |
| 00:45 | Teksti kodeerimine (25 min) | 3. Tekstifaili suurus: arvutus vs tegelik; 4. Hex-vaade (abi: `Juhend_hex_vaade.docx`) |
| 01:10 | Mahuarvutus (10 min) | 5. E-posti postkastide maht (nt 400 × 50 GB + 1200 × 10 GB = 32 000 GB = 31,25 TB (1024) / 32 TB (1000)); vajadusel koduülesandeks |
| 01:20 | Ülesanne 3 ja kokkuvõte (10 min) | — |

Materjalid: esitlus „Kohtumine 3 — Teenused, riistvara ja teksti kodeerimine" (Claude Artifact, vastused kõnelejamärkmetes), `Juhend_hex_vaade.docx`.

## Ülesanne 3 — Teenused ja kodeeringu katse (HTML)

**Maht:** 5 t (A ~1,5 t, B ~3,5 t) · **Tähtaeg:** 18.10.2026 kell 20:00 (Kohtumise 4 eelõhtu)

Täielik ülesandeleht: `Ulesanne3_Teenused_ja_kodeering.docx` · HTML-mall: `Ulesanne3_mall.txt` · õpetaja kontrollskript: `kontroll_ulesanne3.py`.

- **A osa (teenuseliigitus):** Valib kaks enda igapäevaselt kasutatavat IKT-teenust ja liigitab need (SaaS/PaaS/IaaS/muu) 2–3 lausega põhjendusega. Lisab kummagi kohta kuupäevaga ekraanipildi enda seadmest.
- **B osa (kodeeringu katse):** Õpilane saab ette antud HTML-malli (eesti täpitähtedega tekst), asendab nimekoha oma nimega ning salvestab kaks faili: `Perekonnanimi_Eesnimi_Ulesanne3_ansi.html` (ANSI, `<meta charset="windows-1252">`) ja `..._utf8.html` (UTF-8 ilma BOM-ita, `<meta charset="utf-8">`). Avab mõlemad brauseris, teeb vale-meta katse (mõlemas suunas) ja selgitab tulemust, täidab arvutustabeli (N_t, S_ansi, prognoos, S_utf8, vahe) ning kontrollib sõna „Õnne" baite hex-vaates (ekraanipilt).
- **Esitamine Teamsis:** 2 HTML-faili + 1 PDF (ekraanipildid, arvutus, selgitused). Kui Teams .html-i ei luba, esitada zip.

### Õpetaja märkmed

- **Valem:** S_utf8 = S_ansi + N_t − 7, kus N_t on täpitähtede arv failis ja 7 = len("windows-1252") − len("utf-8"). Reavahetused (CRLF/LF) kustuvad, sest on mõlemas failis samad. Malli puhul nimega „Mari Tamm": N_t = 15; ANSI 285 (LF) / 298 (CRLF), UTF-8 293 / 306.
- **Suurus:** õpilased loevad Propertiesi „Size", mitte „Size on disk".
- **Tüüpilised vead:** Notepadi „UTF-8 with BOM" (+3 baiti, EF BB BF); meta ei vasta salvestusele; nimes š/ž (tuleb asendada s/z); unustatud −7 meta-nime pikkuse erinevus; ANSI fail avatud UTF-8-na (näitab �).
- **Kontroll:** `python3 kontroll_ulesanne3.py <kaust või failid>` näitab iga faili suuruse, BOM-i, tuvastatud kodeeringu, meta charseti ja ANSI/UTF-8 paaride prognoosi õigsust.
- **AI-kindlus:** õpilase enda nimi muudab suurused personaalseks; ekraanipildid brauserist ja hex-vaatest ning tegelikud failid on kontrollitavad.

### Arvestamise kriteeriumid

Ülesanne loetakse **arvestatuks**, kui:
- kaks IKT-teenust on liigitatud koos põhjendusega ja ekraanipildid on lisatud;
- mõlemad HTML-failid on õiges kodeeringus salvestatud ja meta charset vastab salvestusele (UTF-8 ilma BOM-ita);
- vale-meta katse tulemused on kirjeldatud ja õigesti selgitatud;
- arvutustabel on täidetud ja prognoos klapib tegeliku faili suurusega;
- hex-kontroll on esitatud ja baidid vastavad kodeeringule.

---
[← Eelmine: Kohtumine 2](02-arvusysteemid-ja-andmemahu-uhikud.md) | [Indeks](README.md) | [Järgmine: Kohtumine 4 →](04-vorguressursid-ja-video-kodeerimine.md)
