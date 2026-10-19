# Video kodeerimise spikker

<p class="sub">Kohtumine 4 · tihendamata maht, bitikiirus ja kodek</p>

**Video on kiiresti vahetuvad pildid (kaadrid).** Mida rohkem detaili, kaadreid ja värvi, seda suurem maht.

## 1. Neli tegurit ja valem

| Tegur | Tähendus | Näide |
|---|---|---|
| Resolutsioon | laius × kõrgus pikslites | 1920 × 1080 = 2 073 600 px |
| Kaadrisagedus | kaadreid sekundis (fps) | 30 |
| Värvisügavus | 24 bitti = **3 baiti** piksli kohta | 3 B |
| Kestus | sekundid | 60 s |

**Tihendamata maht (baiti) = laius × kõrgus × 3 × fps × sekundid**

**Näide, 1080p, 30 fps, 60 s:** 2 073 600 × 3 = 6 220 800 B/kaader → × 30 = **186 624 000 B/s ≈ 186,6 MB/s** → × 8 = **1,49 Gbps** → × 60 = **11,2 GB**.

## 2. Tihendamata video eri resolutsioonidel (30 fps, 24 bitti)

| Resolutsioon | Pikslit | MB/s | Mbps | 1 minut (GB) |
|---|---|---|---|---|
| 720p (1280 × 720) | 921 600 | 82,9 | 663,6 | 5,0 |
| 1080p (1920 × 1080) | 2 073 600 | 186,6 | 1 493 | 11,2 |
| 1440p (2560 × 1440) | 3 686 400 | 331,8 | 2 654 | 19,9 |
| 4K (3840 × 2160) | 8 294 400 | 746,5 | 5 972 | 44,8 |

## 3. Tihendatud video: bitikiirus

**Bitikiirus** (bitrate) = mitu bitti sekundis tihendatud video kasutab. Selle määrab kodek ja seade.

**tihendatud maht (MB) = bitikiirus (Mbps) × aeg (s) ÷ 8**

**Näide:** H.264, 8 Mbps, 60 s → 8 × 60 ÷ 8 = **60 MB**. Tihendamata oli 11,2 GB: ligikaudu **186 korda väiksem**.

**Võrdlus (YouTube'i üleslaadimissoovitus, SDR, 24–30 fps):**

| Resolutsioon | Soovitatav bitikiirus | Tihendamata Mbps | Tihendus (korda) |
|---|---|---|---|
| 720p | 5 Mbps | 663,6 | ~133 |
| 1080p | 8 Mbps | 1 493 | ~187 |
| 1440p | 16 Mbps | 2 654 | ~166 |
| 4K | 35–45 Mbps | 5 972 | ~150 (40 Mbps korral) |

<p class="note">Soovitused on ligikaudsed ja sõltuvad teenusest ning videost. Allikas: YouTube Help, „Recommended upload encoding settings".</p>

## 4. Kodek ja konteiner

| Mõiste | Mis see on | Märkused |
|---|---|---|
| **Kodek** | tihendamise meetod | **H.264 (AVC)** on kõige laiemalt toetatud. **H.265 (HEVC)** ja **AV1** annavad sama kvaliteedi väiksema bitikiirusega, kuid vajavad rohkem arvutusvõimsust. |
| **Konteiner** | fail, kus pilt, heli ja metaandmed koos | **mp4**, **mkv**. Konteiner ei muuda tihendust, aga mõjutab ühilduvust. |
| **CBR** | konstantne bitikiirus | Maht on täpselt ennustatav (sobib voogedastuseks). |
| **VBR / CRF** | muutuv bitikiirus | Staatiline pilt annab väiksema, liikuv pilt suurema faili. Kvaliteet püsib ühtlasem. |

## 5. Kompromiss

Väiksem bitikiirus → väiksem fail ja väiksem võrgukoormus, **kuid** kehvem kvaliteet (kuubikud, hägu). Kõrgem bitikiirus või resolutsioon → rohkem CPU/GPU tööd kodeerimisel ja rohkem ribalaiust edastamisel.

**Meeles pidada:** 24 bitti = **3 baiti** (mitte 24 baiti). Mahu ühikud: võrgus 1 MB = 1000 kB; Windows näitab Propertiesis 1 MB = 1024 kB (vahe ~5 %).
