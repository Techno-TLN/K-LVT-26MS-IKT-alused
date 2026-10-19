# TCP ja UDP ning video edastuse protokollid

<p class="sub">Kohtumine 4 · transpordikihi protokollid ja nende mõju kasulikule andmeedastusele</p>

**Idee:** võrgus liigub andmed pakettidena. **TCP** ja **UDP** otsustavad, kas kadunud pakett saadetakse uuesti ja kas paketid jõuavad kohale õiges järjekorras.

## 1. Põhiline vahe

| Tunnus | **TCP** | **UDP** |
|---|---|---|
| Ühendus | luuakse enne andmeid (*handshake*) | ühendust ei looda, saadetakse kohe |
| Usaldusväärsus | kadunud pakett **saadetakse uuesti** | kadunud pakett **jääb kaduma** |
| Järjekord | paketid antakse rakendusele õiges järjekorras | järjekorda ei garanteerita |
| Kiiruse reguleerimine | aeglustab, kui võrk on ülekoormatud | ei aeglusta, saadab nii kiiresti kui rakendus tahab |
| Päis | vähemalt 20 baiti | 8 baiti |
| Sobib | veebileht, e-post, failide allalaadimine | videokõne, otseülekanne, mängud, DNS |

**Võrdlus:** TCP on kinnitusega kiri (saaja kinnitab saabumise). UDP on postkaart: kiire, kuid ei tea, kas jõudis kohale.

## 2. Mõju kasulikule andmeedastusele

**Kasulik andmemaht (goodput)** on ribalaiusest see osa, mis on päriselt sinu andmed (ilma päisteta ja kordussaatmiseta).

- **Päised:** 1500-baidises paketis on TCP-ga 1460 B andmeid, UDP-ga 1472 B (Ethernetis kokku ~1538 B koos raamistikuga). Kasulik osa on mõlemal ligikaudu **95 %** lingi kiirusest. See on osa sellest, miks 100 Mbps ei anna täit 12,5 MB/s.
- **Kordussaatmine (TCP):** iga kaotatud pakett saadetakse uuesti, kuni kinnitus tuleb. Failile on see hea (andmed on täpselt õiged), aga lisab viivitust ja vähendab kiirust.
- **Ülekoormuse kontroll (TCP):** pakettide kadu paneb TCP saatmiskiirust vähendama. Suur latentsus ja pakettide kadu koos vähendavad ühe TCP-ühenduse kiirust tuntavalt, isegi kui ribalaius on suur.
- **Pidurdus (TCP):** üks kadunud pakett peatab järgmiste andmete üleandmise, kuni see on uuesti kohal. Reaalajas videos tähendab see **seisakut** (pilt hangub).
- **UDP:** kordussaatmist ei ole, seega tekib kadu korral **viga pildis või helis** (kaadrit puudu), aga voog jookseb edasi ilma ootamiseta. Vigu peab parandama rakendus ise (varuandmed, peitmine).

**Valik:** kui andmed peavad olema **täpselt õiged** (fail), kasuta TCP-d. Kui peab olema **kohe ja ühtlane** (videokõne), eelistatakse UDP-d.

## 3. Video edastuse protokollid (ligikaudne pilt)

| Protokoll | Transport | Latentsus | Kasutus |
|---|---|---|---|
| **RTP / RTSP** | UDP (RTSP juhtimine TCP) | alla 1–2 s | IP-kaamerad, IPTV, VoIP |
| **RTMP / RTMPS** | TCP | ~2–5 s | otseülekande saatmine serverisse (nt YouTube, Twitch); OBS-i vaikeviis |
| **SRT** | UDP + vigade parandus | ~0,5–2 s | ülekanne ebastabiilse võrgu kaudu |
| **HLS / MPEG-DASH** | HTTP (TCP) | ~6–30 s (madala latentsusega 2–5 s) | vaatajale jagamine (nt YouTube, Netflix), kohandub kiirusega |
| **WebRTC** | UDP (SRTP) | alla 0,5 s | videokõned brauseris (nt Teams, Meet) |
| **NDI, SMPTE ST 2110** | kohtvõrk (UDP/TCP, multicast) | alla 0,1 s | stuudio- ja AV-võrgud, vajab palju ribalaiust |

<p class="note">Latentsused on suurusjärgud ja sõltuvad seadistusest. Uuemad OBS-i versioonid toetavad lisaks RTMP-le ka SRT ja WebRTC (WHIP) väljundit.</p>

## 4. Seos tunni praktikaga

- **VLC HTTP-voog** (harjutus 5) kasutab **TCP-d**. Mitmesekundiline viivitus tuleb peamiselt puhverdusest, kodeerimisest ja dekodeerimisest; kadude korral lisab ootamist TCP kordussaatmine.
- Task Manageri *Send* ja *Receive* näitavad, kui palju bitte sekundis voog tegelikult võtab.
- **Küsimus:** miks Teams videokõne ei kasuta HLS-i? (Vastus: HLS annaks kümneid sekundeid viivitust.)
