# Ülesanne 4 — Võrgukiirus ja video maht

**Seotud kohtumine:** [Kohtumine 4](04-vorguressursid-ja-video-kodeerimine.md) · **Maht:** ~4 t · **Tähtaeg:** 01.11.2026 kell 20:00 (Kohtumise 5 eelõhtu)

**Esitamine:** Teamsi Ülesanded (Assignments) rakenduses, ühe PDF-ina. Failinimi: `Perekonnanimi_Eesnimi_Ulesanne4.pdf`. Videofaile ei esitata, vaid nende **Properties-akna ekraanipilt**.

## Eesmärk

Mõõta oma seadmetel võrgu kiirust ja video mahtu ning seostada tulemused arvutusega tunnis õpitud valemitega.

## A osa — Minu võrgu kiirus (kohustuslik, ~1 t)

1. Tee oma kodus (või koolis) **kiirusmõõtmine** (nt speedtest-teenusega): allalaadimine (Mbps), üleslaadimine (Mbps), ping (ms). Lisa ekraanipilt kuupäeva ja kellaajaga.
2. Tee `ping` kolmele sihile (oma gateway, `1.1.1.1`, `google.com`), 10 paketti. Esita tabelina min / keskmine / max ning ekraanipilt.
3. Teisenda allalaadimise kiirus **MB/s**-ks (Mbps ÷ 8) ja arvuta, kui kaua võtaks 4 GB faili allalaadimine (arvutuskäik nähtav).
4. **Kui võimalik**, korda kiirusmõõtmist ja `ping`-i nii Wi-Fi kui kaabliga ning kirjuta 2–3 lauset, kuidas need erinesid. Kui kaablit pole, kirjuta, kuidas tulemus muutub, kui seisad ruuterist kaugemal.

## B osa — Video maht (kohustuslik, ~2 t)

**B1. Tihendamata video (arvutus).** Võta **oma arvuti ekraani resolutsioon** (lisa Seadete ekraanipilt), 24 bitti piksli kohta, 30 kaadrit sekundis, kestus 60 sekundit. Arvuta:

- baite kaadris;
- baite sekundis (MB/s);
- 60 s kogumaht (GB);
- vajalik ribalaius (Mbps).

**B2. OBS salvestus (mõõtmine).** Salvesta OBS-iga oma ekraanist **30 sekundit** kahe seadega:

| | Resolutsioon | FPS | Bitikiirus |
|---|---|---|---|
| Salvestus 1 | 1920 × 1080 | 30 | 6000 kbps |
| Salvestus 2 | 1280 × 720 | 30 | 2500 kbps |

Lisa kummagi faili **Properties-akna ekraanipilt** (Size, mitte Size on disk). Arvuta oodatav maht (bitikiirus × aeg ÷ 8) ja võrdle tegelikuga.

**B3. Võrdlus ja selgitus (3–5 lauset).** Mitu korda väiksem on 1080p salvestus (6000 kbps) võrreldes oma B1 tihendamata arvutusega? Miks erineb tegelik suurus arvutatust? Miks tuleb video enne edastamist tihendada?

## C osa — Valikuline

- **VLC ülekanne:** korda tunnis tehtud VLC voogu kodus kahe seadme vahel (nt telefon ja arvuti, või kaks arvutit) ja hinda latentsust (sekundites).
- **Mahutavus:** arvuta, mitu 1080p 6000 kbps vood mahuks sinu allalaadimiskiiruse (või üleslaadimise) peale, kasutades 75% kasutatavat ribalaiust.

## Mida esitada (PDF)

1. A osa: kiirusmõõtmise ja `ping`-i ekraanipildid, tabel, MB/s ja 4 GB allalaadimise arvutus.
2. B1: Seadete ekraanipilt ja arvutuskäik (valem + väärtuste asendus + vastus).
3. B2: kaks Properties-akna ekraanipilti, oodatav vs tegelik maht.
4. B3: lühike selgitus.

## Arvestamise kriteeriumid

Ülesanne loetakse **arvestatuks**, kui:

- A osa mõõtmised on tehtud, ekraanipildid kuupäevaga lisatud ja Mbps → MB/s ning allalaadimisaja arvutus on õige ja käik nähtav;
- B1 arvutus on tehtud õiges järjekorras oma resolutsiooniga ja tulemus on mõistlik (õiged ühikud);
- B2 mõlema salvestuse suurus on näidatud ekraanipildiga ja oodatud/tegelik võrreldud;
- B3 selgitus on sisuliselt korrektne.

## Õpetaja märkmed

- **Isikupärasus:** oma ekraani resolutsioon, oma speedtest, oma `ping`-id ja oma OBS-failid. Õpilaste vastused erinevad, mistõttu AI-ga teha ei saa.
- **Kontrollimine B1:** laius × kõrgus × 3 × 30 = baite sekundis. Näide 1920 × 1080: 186 624 000 B/s ≈ 186,6 MB/s; 60 s ≈ 11,2 GB; ≈ 1,49 Gbps. 2560 × 1440: 3 686 400 px × 3 = 11 059 200 B/kaader; × 30 = 331 776 000 B/s; 60 s ≈ 19,9 GB; ≈ 2,65 Gbps.
- **Kontrollimine B2:** 6000 kbps × 30 s ÷ 8 = 22,5 MB; 2500 kbps × 30 s ÷ 8 ≈ 9,4 MB; lubatud hälve ~±15 % (heli, konteiner). Suurem hälve tähendab sageli, et bitikiirus või Rate Control jäi valesti.
- **Tüüpilised vead:** Mbps ja MB/s segamine (unustatud ÷ 8); kbps → Mbps vale teisendus; „Size on disk” asemel Size; värvisügavus 24 bitti on 3 baiti (mitte 24 baiti).

---
[← Kohtumine 4](04-vorguressursid-ja-video-kodeerimine.md) | [Indeks](README.md)
