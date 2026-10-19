# OBS Studio: ekraani salvestamine ja faili suuruse kontroll

<p class="sub">Kohtumine 4 · Harjutus 4 · ~25 min · Windows, OBS Studio (ingliskeelne liides)</p>

**Eesmärk:** salvesta kaks 30-sekundilist ekraanivideot erinevate seadetega ja võrdle faili tegelikku suurust arvutatuga.

## 1. Ettevalmistus

1. Ava **OBS Studio**. Kui käivitub *Auto-Configuration Wizard*, vajuta **Cancel** (muidu muudab see seaded ise).
2. Paneelis **Sources** vajuta **+** → **Display Capture** → OK. Eelvaates peaks nähtuma sinu ekraan. Kui pilt on must, proovi **Window Capture**.
3. Liidese keel: *Settings → General → Language: English* (vajab OBS-i taaskäivitust). Siis klapivad juhendi menüünimed.

## 2. Seaded (Settings, nupp all paremal)

| Vahekaart | Väli | Väärtus |
|---|---|---|
| **Output** | Output Mode | **Advanced** |
| Output → Recording | Type | Standard |
| | Recording Path | vali kaust, kust faili leiad |
| | Recording Format | **mkv** (OBS soovitus: fail ei rikne katkestamisel) või mp4 |
| | Video Encoder | **x264** (võib olla nimetatud *Software (x264)*) |
| | Rate Control | **CBR** |
| | Bitrate | vt tabel allpool |
| **Video** | Base (Canvas) Resolution | sinu ekraani resolutsioon |
| | Output (Scaled) Resolution | vt tabel allpool |
| | Common FPS Values | **30** |

Vajuta **Apply**, siis **OK**. Muudatuse tegid õigesti, kui *Output → Recording* all näed valitud x264 ja CBR-i.

## 3. Salvestus 1 ja 2

| | Output Resolution | FPS | Bitrate |
|---|---|---|---|
| **Salvestus 1** | 1920 × 1080 | 30 | **6000** kbps |
| **Salvestus 2** | 1280 × 720 | 30 | **2500** kbps |

1. Pane õige seade paika (Settings → Apply → OK).
2. Vajuta **Start Recording**, oota **30 sekundit** (liiguta hiirt, ava aknaid ja kaustu), siis **Stop Recording**.
3. Failid leiad: *File → Show Recordings*.
4. Korda teise seadega.

## 4. Mõõda ja arvuta

Failil paremklõps → **Properties** → loe **Size** (mitte *Size on disk*). Tee ekraanipilt.

**oodatud maht (MB) = bitikiirus (kbps) × aeg (s) ÷ 8 ÷ 1000**

| | Oodatud (arvuta) | Tegelik (Properties) | Vahe (%) |
|---|---|---|---|
| Salvestus 1 (6000 kbps, 30 s) | | | |
| Salvestus 2 (2500 kbps, 30 s) | | | |

Kontroll: 6000 × 30 ÷ 8 ÷ 1000 = 22,5 MB. Hälve kuni ~10 % on normaalne (helirada, konteiner, Windows loeb 1 MB = 1 048 576 B).

## 5. Kui midagi ei tööta

- **Pilt must:** kasuta Window Capture'i; kahe graafikakaardiga sülearvutil käivita OBS ja brauser sama kaardiga.
- **Teade *Encoding overloaded*:** arvuti ei jõua x264-ga. Vähenda Output Resolution või FPS ja märgi üles, mida muutsid.
- **Faili pole:** salvestus peab olema lõpetatud (**Stop Recording**), mitte OBS lihtsalt suletud.
- **Faili ei mängita:** mkv avab VLC alati. Windowsi esitaja ei pruugi.
- **Heli puudub:** ei ole viga, selle harjutuse jaoks pole heli vaja.

**Arutelu:** kas märkasid kvaliteedierinevust? Mis juhtuks, kui Rate Control oleks *VBR* või *CRF*?
