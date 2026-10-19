# Kohtumine 4 — Võrguressursid ja video kodeerimine

**Kuupäev:** 19.10.2026 (E) · **Kestus:** 2 ak. tundi (90 min)

**Materjalid:** esitlus „Kohtumine 4 — Võrguressursid ja video kodeerimine” (Claude Artifact) · koduülesanne: [04-ulesanne-4.md](04-ulesanne-4.md)

**A4 abimaterjalid (PDF, trükkimiseks; md-allikad samas kaustas):** [põhimõistete spikker](04-materjalid/04-spikker-pohimoisted.pdf) · [video kodeerimise spikker](04-materjalid/04-spikker-video-kodeerimine.pdf) · [OBS Studio juhend](04-materjalid/04-juhend-obs-studio.pdf) · [VLC praktika juhis](04-materjalid/04-juhend-vlc-voog.pdf) · [Windowsi vahendid võrgu jõudluse vaatamiseks](04-materjalid/04-spikker-windows-vorgu-joudlus.pdf) · [TCP ja UDP ning video edastuse protokollid](04-materjalid/04-spikker-tcp-udp-protokollid.pdf). PDF-i saab uuesti genereerida skriptiga `04-materjalid/build.py` (`python3 build.py sisend.md valjund.pdf`; vajab `markdown` ja `playwright`).

## Tunni eesmärk

Õpilane oskab hinnata, kui palju andmeid video tekitab, kui kiire võrk selle edastamiseks vaja on, ja mõõta seda ka päris seadmetel (OBS, VLC, `ping`). See laiendab Kohtumise 2 ühikuid (bit, bait, MB, GB) ja Kohtumise 3 kodeerimise ideed (sama sisu, erinev maht olenevalt kodeeringust) võrgule ja videole.

## Ajakava

| Aeg | Teema | Harjutus |
|---|---|---|
| 00:00–00:05 | Ülesande 3 tagasivaade: kuidas HTML-failid kuvati, krõbin ja meta charset | arutelu |
| 00:05–00:30 | Võrguressursid: ribalaius, latentsus, bit vs bait, Wi-Fi vs kaabel, topoloogia, **TCP ja UDP** | 1. `ping` ja latentsus; 2. Mbps ↔ MB/s |
| 00:30–00:50 | Video kodeerimine: resolutsioon, kaadrisagedus, värvisügavus, bitikiirus, kodek, **video edastuse protokollid** | 3. Tihendamata video maht |
| 00:50–01:15 | Praktika: OBS salvestus | 4. Kaks salvestust, tegelik suurus vs arvutus |
| 01:15–01:23 | Praktika: VLC ülekanne (**õpetaja demo**, paaris tegemine valikuline) | 5. Voog kahe arvuti vahel, latentsuse hindamine |
| 01:23–01:30 | Ülesanne 4 ja kokkuvõte | — |

Harjutus 5 (VLC) on tunnis **õpetaja demo** (~8 min), sest võrgu- ja tulemüüriprobleemid võivad paaristöö venitada. Paaris tegemine on **valikuline**: kes soovib, teeb tunni lõpus (kui aega jääb) või kodus. Selle tunni praktika vajab rohkem aega kui eelmised, seega teooria hoia lühike.

## 1. Tagasivaade: Ülesanne 3 (5 min)

- Mida nägid, kui UTF-8 fail oli märgitud `windows-1252`? Mida, kui ANSI fail oli märgitud `utf-8`?
- Küsi 2–3 õpilaselt, mis kõige rohkem üllatas. Seo järgmisega: **sama sisu, erinev kujutus baitides, seega erinev maht ja erinev tõlgendus**. Täpselt sama mõte kehtib ka videos.

## 2. Võrguressursid ja TCP/UDP (25 min koos harjutustega)

**Ribalaius (bandwidth)** on, kui palju andmeid võrk ajaühikus edastab. Mõõdetakse bittides sekundis: Mbps (megabitti sekundis), Gbps.

**Latentsus (latency)** on viivitus, kui kaua kulub andmetel teekond. Mõõdetakse millisekundites (ms). Suur ribalaius ei tähenda väikest latentsust: satelliitühendusel võib ribalaius olla hea, aga latentsus suur.

**Bit vs bait.** Võrgu kiirus on bittides, failid on baitides. 1 bait = 8 bitti, seega **Mbps ÷ 8 = MB/s**. 100 Mbps ühendus annab teoreetiliselt 12,5 MB/s ja päriselt tavaliselt 10–20 % vähem (päised, ülekoormus, Wi-Fi).

**Wi-Fi vs kaabel.** Kaabel: stabiilne latentsus, vähem häireid. Wi-Fi: mugav, kuid ribalaius ja latentsus kõiguvad (kaugus, seinad, teised võrgud, jagatud ribalaius). Reaalajas edastuse (video, kõned) jaoks loeb kõige rohkem **stabiilsus**, mitte tipukiirus.

**Topoloogia.** Täht (kõik seadmed ühe kommutaatori/ruuteri taga) on tavaline ka koolis ja kodus. Ühise lüli ribalaius jagatakse seadmete vahel: 100 Mbps lüli, millel on 10 aktiivset voogu, annab igaühele keskmiselt ~10 Mbps.

**TCP ja UDP (5 min).** Võrgus liiguvad andmed pakettidena ja transpordiprotokoll otsustab, mis juhtub kadunud paketiga. **TCP** loob ühenduse, saadab kadunud paketi uuesti, hoiab järjekorra ja aeglustab ülekoormuse korral: täpne, aga viivitusega (veeb, e-post, failid). **UDP** saadab kohe ja ei saada kadunud paketti uuesti: kaod jäävad kaduma, aga viivitust ei ole (videokõne, otseülekanne, mängud). **Mõju kasulikule andmemahule:** päised võtavad ~5 % lingi kiirusest (1500 B pakett: TCP-ga 1460 B andmeid, UDP-ga 1472 B); TCP kordussaatmine ja kiiruse vähendamine pakettide kao korral vähendavad kasulikku mahtu lisaks; üks kadunud pakett peatab TCP-s järgmised andmed, mistõttu pilt hangub. Vt A4 spikker „TCP ja UDP ning video edastuse protokollid". VLC HTTP-voog (harjutus 5) kasutab TCP-d.

### Harjutus 1 — `ping` ja latentsus (5 min)

1. Ava käsurida. Windows: `ping -n 10 <aadress>`; macOS/Linux: `ping -c 10 <aadress>`.
2. Tee kolm mõõtmist: oma **gateway** (Ülesandes 2 leitud aadress), `1.1.1.1` ja `google.com`.
3. Kirjuta tabelisse minimaalne, keskmine ja maksimaalne aeg (ms) ning kadunud pakettide arv.

| Siht | Min | Keskmine | Max | Kadunud |
|---|---|---|---|---|
| Gateway | | | | |
| 1.1.1.1 | | | | |
| google.com | | | | |

Oodatav: gateway on kõige kiirem (tavaliselt alla ~5 ms), internetisihid aeglasemad. Küsi: miks? (rohkem lülisid, kaugem füüsiline vahemaa). Võrdle Wi-Fi-ga ühendatud arvuteid kaabliga ühendatuga, kui klassis on mõlemaid.

**Windowsi vahendid:** näita õpilastele lühidalt, kuidas oma arvutis võrku jälgida: Task Manager → Performance → Ethernet/Wi-Fi (*Send*, *Receive*), Resource Monitor (`resmon` → Network) ja `netsh wlan show interfaces`. Täpsed sammud on A4 spikris „Windowsi vahendid võrgu jõudluse vaatamiseks". Kasuta seda ka harjutuse 5 (VLC demo) ajal: vaata saatja *Send* ja vastuvõtja *Receive* väärtust.

### Harjutus 2 — Mbps ↔ MB/s (5 min)

Paberil või kalkulaatoriga. Kasuta lihtsuse mõttes 1 GB = 1000 MB.

a) 100 Mbps = ? MB/s
b) 1 Gbps = ? MB/s
c) Kui kaua võtab 2 GB faili allalaadimine 100 Mbps ühendusel (ideaalsel juhul)?
d) 4K voog kasutab 25 Mbps. Mitu GB andmeid kulub 1 tunni vaatamiseks?
e) Mitu 8 Mbps videovoogu mahub 100 Mbps lülile (ideaalis ja realistlikult, kui kasutatav ribalaius on ~75 %)?

**Vastused (õpetajale):** a) 12,5 MB/s. b) 125 MB/s. c) 2000 MB ÷ 12,5 MB/s = 160 s ≈ 2 min 40 s (päriselt veidi rohkem). d) 25 ÷ 8 = 3,125 MB/s × 3600 s = 11 250 MB ≈ 11,25 GB. e) 100 ÷ 8 = 12,5, seega 12 voogu ideaalis; 75 Mbps ÷ 8 ≈ 9 voogu realistlikult.

## 3. Video kodeerimine ja protokollid (20 min koos harjutusega)

Video on pildid ühe teise järel. Selle maht sõltub neljast asjast:

- **Resolutsioon** (nt 1920 × 1080 = 2 073 600 pikslit kaadris).
- **Kaadrisagedus** (fps, nt 30 kaadrit sekundis).
- **Värvisügavus** (tavaliselt 24 bitti = 3 baiti piksli kohta).
- **Kestus**.

**Tihendamata video maht** = laius × kõrgus × baiti piksli kohta × fps × sekundid.

Näide, 1920 × 1080, 24 bit, 30 fps:

- Kaader: 2 073 600 × 3 = 6 220 800 baiti (≈ 6,2 MB).
- Sekund: 6 220 800 × 30 = 186 624 000 baiti ≈ **186,6 MB/s**, ehk ≈ **1,49 Gbps**.
- Minut: ≈ 11,2 GB.

See on liiga palju edastamiseks ja salvestamiseks, seega videot **tihendatakse kodekiga** (H.264, H.265, AV1 jt). Tihendus jätab välja detaile, mida silm vaevalt märkab, ja kasutab ära sarnasust kaadrite vahel. **Bitikiirus (bitrate)** ütleb, kui palju bitte sekundis tihendatud video kasutab. Näiteks 1080p30 H.264 voogedastuseks sobib tavaliselt umbes 4–8 Mbps. Failimaht = bitikiirus × kestus ÷ 8.

Näide: H.264, 8 Mbps, 60 s → 8 × 60 ÷ 8 = 60 MB. Võrreldes tihendamata 11,2 GB-ga on see ligikaudu 186 korda väiksem.

**Kompromiss:** väiksem bitikiirus = väiksem fail ja väiksem võrgukoormus, kuid halvem kvaliteet ning vajab rohkem arvutusvõimsust kodeerimiseks (seos Kohtumise 3 CPU/GPU-ga).

**Video edastuse protokollid (5 min, maailmapilt).** **RTP/RTSP** (UDP; IP-kaamerad, IPTV), **RTMP** (TCP; saatmine serverisse, OBS-i vaikeviis), **SRT** (UDP + vigade parandus; ebastabiilne võrk), **HLS/MPEG-DASH** (HTTP, TCP; vaatajale jagamine, viivitus kümneid sekundeid), **WebRTC** (UDP; videokõned, alla 0,5 s), **NDI/SMPTE ST 2110** (kohtvõrk; stuudio ja AV). Mida väiksem viivitus, seda tihedamini UDP. Latentsused on ligikaudsed. Täpsem tabel on A4 spikris.

### Harjutus 3 — Tihendamata video maht (5 min)

Video: 1280 × 720 (720p), 24 bit, 30 fps, 10 sekundit.

a) Mitu baiti kaadris?
b) Mitu MB/s?
c) Mitu MB 10 sekundi kohta?
d) Mitu Mbps?
e) Kui sama video on H.264-ga 5 Mbps, siis mitu MB on 10 s? Mitu korda väiksem?

**Vastused:** a) 1280 × 720 = 921 600 pikslit × 3 = 2 764 800 baiti. b) × 30 = 82 944 000 B/s ≈ 82,9 MB/s. c) × 10 = 829 440 000 B ≈ 829 MB. d) 82 944 000 × 8 = 663 552 000 bit/s ≈ 663,6 Mbps. e) 5 × 10 ÷ 8 = 6,25 MB; 829,44 ÷ 6,25 ≈ 133 korda väiksem.

## 4. Praktika: OBS (25 min)

**Tööriist:** OBS Studio. Kontrolli enne tundi, et see on klassi arvutites olemas või lubatud paigaldada (vajadusel kasuta portable-versiooni).

**Harjutus 4 — Kaks salvestust, kaks suurust**

1. Seaded → **Output** → Output Mode: **Advanced** → vahekaart **Recording**: Type Standard, Format mp4 (või mkv), Encoder **x264**, Rate Control **CBR**.
2. **Esimene salvestus:** Seaded → **Video**: Output (Scaled) Resolution **1920 × 1080**, FPS **30**; Output → Recording → Bitrate **6000 kbps**. Salvesta **30 sekundit** (Start Recording, 30 s, Stop). Liiguta hiirt ja ava aknaid.
3. **Teine salvestus:** resolutsioon **1280 × 720**, FPS 30, Bitrate **2500 kbps**. Salvesta taas 30 sekundit.
4. Vaata mõlema faili suurust (Properties → Size, mitte „Size on disk”) ja kirjuta üles.
5. Arvuta oodatav maht: bitikiirus (kbps) × kestus (s) ÷ 8 ÷ 1000 = MB. Võrdle tegelikuga.

**Oodatav tulemus:** 6000 kbps × 30 s ÷ 8 = 22 500 kB ≈ 22,5 MB; 2500 kbps × 30 s ÷ 8 ≈ 9,4 MB. Päris fail on tavaliselt veidi suurem (helirada, konteiner) või veidi erinev (kodek ei hoia bitikiirust täpselt). Kui heli ei salvestata, on erinevus väiksem. Hälve kuni ~10 % on normaalne.

**Arutelu:** mis juhtuks, kui Rate Control oleks VBR või CRF? (Staatilise ekraani puhul fail oluliselt väiksem, sest tihendus kasutab kaadrite sarnasust.) Kes märkas kvaliteedierinevust?

## 5. Praktika: VLC ülekanne (õpetaja demo, ~8 min)

**Harjutus 5 — Voog kahe arvuti vahel (õpetaja demo; paaris tegemine valikuline)**

Õpetaja teeb demo kahe seadmega (nt oma arvuti saatjaks, üks õpilase arvuti vastuvõtjaks) ja õpilased vaatavad ning hindavad latentsust. Kes soovib, saab sama paaris järele proovida tunnis (kui aega jääb) või kodus; juhis on A4 spikris „VLC praktika juhis”. Paaris tehes on üks saatja, teine vastuvõtja ning kasutatakse Ülesandes 2 leitud IP-aadresse.

*Saatja:*

1. VLC → Media → **Stream…** (Ctrl+S) → lisa video fail → **Stream**.
2. Destination: **HTTP** → Add → port **8080**, path `/demo`.
3. Transcoding profiil: **Video – H.264 + MP3 (TS)** → Stream.

*Vastuvõtja:* Media → **Open Network Stream…** → `http://<saatja-IP>:8080/demo` → Play.

*Latentsuse hindamine:* saatja valib allikaks töölaua (Media → Open Capture Device → Capture mode: Desktop → Stream) ja avab oma ekraanil käimasoleva stopperi (nt Windowsi Kell). Vastuvõtja ekraanil nähtav stopper on tagasi jäänud: vahe saatja ja vastuvõtja stopperi vahel on ligikaudne latentsus sekundites. Võrrelge Wi-Fi ja kaabliga, kui võimalik.

**Võimalikud takistused (õpetaja kontrollib enne tundi):**

- Windowsi tulemüür küsib luba: lubada **privaatvõrgus**.
- Mõnes Wi-Fi-võrgus ei suhtle seadmed omavahel (klientide eraldamine). Siis kasuta kaablit või tee demo ainult õpetaja arvutiga.
- VLC vaikimisi puhverdus (network caching, ~1000 ms) lisab viivitust. Seda saab vähendada, kuid ebastabiilne võrk annab siis katkeid.

**Arutelu:** miks ülekanne viibib mitu sekundit, kuigi võrk on kiire? (puhverdus + kodeerimine + dekodeerimine). Ribalaius ei ole latentsus.

## Ülesanne 4 ja kokkuvõte (7 min)

Tutvusta ülesannet „Minu võrk ja minu film” (täpne juhend: [04-ulesanne-4.md](04-ulesanne-4.md), ~3 t). Soovita OBS-failid alles hoida, neid kasutatakse koduülesandes. Tähtaeg **01.11.2026 kell 20:00**.

Kolm mõtet, mida meelde jätta:

- Võrgu kiirus on bittides, failid baitides: Mbps ÷ 8 = MB/s.
- Ribalaius ja latentsus on kaks eri asja.
- Video maht sõltub resolutsioonist, kaadrisagedusest, kestusest ja **kodekist/bitikiirusest**, tihendus muudab mahtu sadu kordi.

**Järgmine kohtumine (02.11.2026):** Infrastruktuuriressursid. Tund algab CSV-formaadi sissejuhatusega (kodeering, eraldaja, import Outlooki veebi).

## Õpetaja ettevalmistus

- [ ] OBS ja VLC on klassi arvutites või lubatud paigaldada.
- [ ] VLC demo jaoks on kaks seadet samas võrgus (või kaabliga); kui klassi Wi-Fi eraldab kliendid, kasuta kaablit või näita demot ühe arvuti peal (voog `localhost`-i kaudu).
- [ ] Testi VLC voog enne tundi läbi, sh tulemüüri küsimus.
- [ ] Kontrolli, et `ping` ei ole võrgus blokeeritud.
- [ ] Trüki või jaga arvutuste valemid (slaidid ja see fail).

---
[← Eelmine: Kohtumine 3](03-teenuste-liigid-ja-riistvararessursid.md) | [Indeks](README.md) | [Järgmine: Kohtumine 5 →](05-infrastruktuuriressursid.md)
