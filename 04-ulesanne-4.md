# Ülesanne 4 — Minu võrk ja minu film

**Seotud kohtumine:** [Kohtumine 4](04-vorguressursid-ja-video-kodeerimine.md) · **Maht:** ~3 t · **Tähtaeg:** 01.11.2026 kell 20:00 (Kohtumise 5 eelõhtu)

**Esitamine:** Teamsi Ülesanded (Assignments) rakenduses, ühe PDF-ina. Failinimi: `Perekonnanimi_Eesnimi_Ulesanne4.pdf`. Videofaile ei esitata, vaid nende ekraanipildid.

**Abimaterjalid:** [põhimõistete spikker](04-materjalid/04-spikker-pohimoisted.pdf) · [video kodeerimise spikker](04-materjalid/04-spikker-video-kodeerimine.pdf)

## Mida sa teada saad

Kui kiire on sinu internet päriselt? Mitu videot saab sinu kodus korraga vaadata? Ja kui kaua võtaks sinu lemmikfilmi allalaadimine? Kõik vastused tulevad sinu enda numbritest.

## 1. Mõõda oma võrku (~30 min)

1. Tee **kiirusmõõtmine** (nt speedtest-teenusega): allalaadimine (Mbps), üleslaadimine (Mbps), ping (ms). Lisa ekraanipilt koos kuupäeva ja kellaajaga.
2. Tee `ping` oma gateway'le ja `google.com`-ile (10 paketti): `ping -n 10 aadress` (Windows) või `ping -c 10 aadress` (macOS/Linux). Lisa ekraanipilt.
3. Kirjuta tulemused tabelisse ja **teisenda allalaadimiskiirus MB/s-ks** (Mbps ÷ 8).

| | Tulemus |
|---|---|
| Allalaadimine (Mbps) | |
| Allalaadimine (MB/s) | |
| Üleslaadimine (Mbps) | |
| Ping speedtestis (ms) | |
| Ping gateway'ni, keskmine (ms) | |
| Ping google.com'i, keskmine (ms) | |

## 2. Mitu videovoogu mahub minu koju? (~60 min)

**a) Mis on päris video bitikiirus?** Võta **fail, mille suurust tead**: tunnis tehtud OBS-salvestus *või* mõni **video oma telefonist**. Loe Propertiesist faili suurus (**Size**) ja video kestus sekundites. Arvuta:

**bitikiirus (Mbps) = maht (MB) × 8 ÷ kestus (s)**

Lisa Propertiesi ekraanipilt ja arvutuskäik. Kumb on suurem: sinu telefonivideo või OBS-salvestus? Kirjuta üks lause, miks sa arvad, et nii on.

**b) Mitu voogu mahub?** Eelda, et kasutatav ribalaius on **75 %** sinu allalaadimiskiirusest. Arvuta, mitu voogu korraga mahub:

| Voog | Bitikiirus | Mitu mahub minu koju |
|---|---|---|
| 1080p (YouTube soovitus) | 8 Mbps | |
| 4K (YouTube soovitus) | 40 Mbps | |

Kirjuta kaks lauset: kas sinu kodu võrk jätkab, kui kolm inimest vaatavad korraga 1080p videot?

## 3. Minu lemmikfilm (~45 min)

Vali üks **film, sari või video**, mida sa tõesti vaatad (kestus tead või leiad internetist). Arvuta:

1. Faili maht, kui video on 1080p ja 8 Mbps: **MB = Mbps × sekundid ÷ 8**.
2. Kaua võtaks selle allalaadimine **sinu** kiirusel (osast 1)?
3. Kui suur oleks sama film **tihendamata** (1920 × 1080, 24 bitti, 30 fps)? Kasuta valemit: **laius × kõrgus × 3 × fps × sekundid**.
4. Mitu korda suurem on tihendamata variant?

Lisa filmi nimi ja arvutuskäik (valem + väärtuste asendus + vastus).

## 4. Kokkuvõte (~15 min)

Kirjuta 3–4 lauset: mis üllatas sind kõige rohkem (nt tihendamata filmi maht, kodune kiirus või telefonivideo bitikiirus)?

## Valikuline (ei ole kohustuslik)

- Korda mõõtmist nii Wi-Fi kui kaabliga ja võrdle ping'i.
- Speedtesti ajal tee Task Manageri (*Performance → Ethernet/Wi-Fi*) ekraanipilt ja võrdle *Receive* tippu speedtesti tulemusega (vt [Windowsi vahendite spikker](04-materjalid/04-spikker-windows-vorgu-joudlus.pdf)).
- VLC voog paaris: tunnis näitas õpetaja demot, proovi ise kodus kahe seadme vahel (vt [VLC juhis](04-materjalid/04-juhend-vlc-voog.pdf)) ja hinda latentsust.
- Vaata OBS-salvestuse faili baite hex-vaates (vt Kohtumise 3 hex-juhend).

## Mida esitada (PDF)

1. Osa 1: ekraanipildid ja tabel.
2. Osa 2: Propertiesi ekraanipilt, bitikiiruse arvutus, voogude tabel ja kaks lauset.
3. Osa 3: filmi nimi ja neli arvutust.
4. Osa 4: kokkuvõte.

## Arvestamise kriteeriumid

Ülesanne loetakse **arvestatuks**, kui:

- osa 1 mõõtmised on tehtud ja ekraanipildid kuupäevaga lisatud, Mbps → MB/s teisendus on õige;
- osa 2 bitikiiruse arvutus on tehtud õigete ühikutega ja voogude tabel on täidetud (75 % kasutatavast ribalaiusest) ning käik on nähtav;
- osa 3 neli arvutust on tehtud ja vastused on mõistlikud (ühikud ja suurusjärgud);
- kokkuvõte on olemas.

## Õpetaja märkmed

- **Isikupärasus:** õpilase enda speedtest, ping-id, fail (telefonist või OBS-ist) ja film. Tulemused erinevad igal õpilasel, ekraanipildid on kuupäevaga.
- **Kontrollimine osa 2a:** bitikiirus = MB × 8 ÷ s. Näide OBS-salvestus 22,5 MB / 30 s → 6 Mbps. Telefonivideo on tavaliselt 10–20 Mbps (1080p/4K), seega sageli suurem kui OBS-i 6 Mbps.
- **Kontrollimine osa 2b:** voogude arv = 0,75 × allalaadimise Mbps ÷ voo Mbps, alla ümardatud. Näide 200 Mbps: 150 ÷ 8 = 18 voogu (1080p); 150 ÷ 40 = 3 voogu (4K).
- **Kontrollimine osa 3:** 2-tunnine film (7200 s) 8 Mbps: 8 × 7200 ÷ 8 = 7200 MB ≈ 7,2 GB. Tihendamata 1080p30: 186,624 MB/s × 7200 ≈ 1 343 693 MB ≈ **1,34 TB**; suhe ≈ 187.
- **Tüüpilised vead:** Mbps ja MB/s segamine (unustatud ÷ 8); minutid sekunditeks muutmata jätmine; kbps → Mbps vale teisendus; Properties *Size on disk* asemel *Size*; 24 bitti = 24 baiti (peab olema 3 baiti).
- **Märkus mahu kohta:** ÕV1 iseseisva töö kogumaht on 36 t. Ülesanne 4 on varasemast 4 t asemel ~3 t, ülejäänud maht tuleb jaotada teistele ülesannetele või jätta valikulisteks osadeks.

---
[← Kohtumine 4](04-vorguressursid-ja-video-kodeerimine.md) | [Indeks](README.md)
