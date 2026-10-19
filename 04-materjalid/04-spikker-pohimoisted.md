# Põhimõistete spikker: võrk ja video

<p class="sub">Kohtumine 4 · sõnastik ja valemid</p>

## Valemid

| Mida | Valem |
|---|---|
| Mbps → MB/s | **Mbps ÷ 8 = MB/s** |
| Allalaadimisaeg (s) | **faili maht (MB) ÷ kiirus (MB/s)** |
| Tihendatud video maht (MB) | **bitikiirus (Mbps) × aeg (s) ÷ 8** |
| Tihendamata video maht (B) | **laius × kõrgus × 3 × fps × sekundid** |

**Töödeldud näited.**
(1) 100 Mbps = 100 ÷ 8 = **12,5 MB/s**; 2 GB (2000 MB) laadimine = 2000 ÷ 12,5 = **160 s**.
(2) 1080p, 8 Mbps, 60 s: 8 × 60 ÷ 8 = **60 MB**.
(3) 25 Mbps voog 1 h: 25 ÷ 8 = 3,125 MB/s × 3600 s = **11 250 MB ≈ 11,25 GB**.

## Võrk

| Mõiste | Tähendus | Ühik / näide |
|---|---|---|
| **Bit / bait** | bit on 0 või 1; **1 bait = 8 bitti** | Võrk: bitid (Mbps). Failid: baidid (MB). |
| **Ribalaius** (bandwidth) | kui palju andmeid mahub ajaühikus läbi | Mbps, Gbps |
| **Latentsus** (latency) | kui kaua andmetel teekond kestab | ms; ping |
| **Ping** | käsk, mis mõõdab ühe paketi edasi-tagasi aega | `ping -n 10 aadress` (Windows) |
| **Pakettide kadu** | osa andmepakette ei jõua kohale | %; pilt hangub või heli katkeb |
| **Latentsuse kõikumine** (jitter) | viivitus ei ole paketist paketini ühtlane | ping: 20, 22, 80, 21 ms; heli ja pilt jooksevad ebaühtlaselt |
| **Protokoll** | kokkulepitud reeglid andmete saatmiseks | TCP, UDP, HTTP |
| **TCP / UDP** | TCP saadab kadunud paketi uuesti (täpne, aeglasem); UDP mitte (kiire, kaod jäävad) | fail: TCP; videokõne: UDP |
| **Gateway** | seade, mille kaudu minnakse teise võrku (ruuter) | nt 192.168.1.1 |
| **Topoloogia (täht)** | kõik seadmed ühe kommutaatori / ruuteri taga | jagavad lüli ribalaiust |
| **Wi-Fi vs kaabel** | Wi-Fi mugav, kuid kõikuv; kaabel stabiilne | videol loeb stabiilsus |
| **Voogedastus** (streaming) | video edastus samal ajal kui seda vaadatakse | vajab ühtlast ribalaiust |
| **Puhverdus** (buffering) | mängija koondab mõne sekundi ette | lisab viivitust |

## Video

| Mõiste | Tähendus | Näide |
|---|---|---|
| **Resolutsioon** | laius × kõrgus pikslites | 1920 × 1080 (1080p) |
| **Kaadrisagedus (fps)** | kaadreid sekundis | 24, 30, 60 |
| **Värvisügavus** | bitte piksli kohta | 24 bitti = 3 baiti |
| **Bitikiirus** (bitrate) | bitte sekundis tihendatud videos | 8 Mbps |
| **Kodek** | tihendamise meetod | H.264, H.265, AV1 |
| **Konteiner** | faili vorming, kus pilt ja heli koos | mp4, mkv |
| **CBR / VBR** | konstantne / muutuv bitikiirus | CBR: ennustatav maht |
| **Tihendamine** | andmete väiksemaks tegemine | video ~100–200 korda |

## Meelde jätta

1. Võrgu kiirus on **bittides**, failid **baitides**: Mbps ÷ 8 = MB/s.
2. **Ribalaius ja latentsus on kaks eri asja**: suur ribalaius ei tee latentsust väiksemaks.
3. Video maht sõltub **bitikiirusest ja kodekist**, tihendus muudab mahtu sadu kordi.
4. Päris kiirus on tavaliselt **10–20 % väiksem** teoreetilisest.
