# VLC praktika: video voog kahe arvuti vahel

<p class="sub">Kohtumine 4 · Harjutus 5 · õpetaja demo tunnis (~8 min), paaris tegemine valikuline · VLC 3.x</p>

**Eesmärk:** edasta video üle võrgu ühest arvutist teise ja hinda latentsust sekundites.

## 0. Enne alustamist

1. Leia oma IP: Windowsis käsurea `ipconfig` → *IPv4 Address*. Kirjuta üles: **saatja IP** …………………… · **vastuvõtja IP** ……………………
2. Kontrolli, et IP-aadressi esimesed kolm numbrit klapivad (maski 255.255.255.0 korral on arvutid samas võrgus).
3. Proovi `ping partneri-IP`. Kui vastuseid ei tule, siis tõenäoliselt blokeerib tulemüür või klassi Wi-Fi ei lase seadmetel omavahel suhelda: vaata osa 5 või kasutage kaablit.

## 1. Saatja (üks paarilistest)

1. **Media → Stream…** (Ctrl+S).
2. Vahekaart **File** → **Add…** → vali video → alt **Stream** → **Next**.
3. *Destination Setup*: vali **HTTP** → **Add**. **Port: 8080**, **Path: /demo** (kui Path-välja pole, jäta vaikeväärtus). **Next**.
4. *Transcoding Options*: märgi **Activate Transcoding**, *Profile*: **Video - H.264 + MP3 (TS)**. **Next**.
5. Vajuta **Stream**. Kui Windows küsib luba (*Windows Security Alert*): märgi **Private networks** → **Allow access**.

## 2. Vastuvõtja

1. **Media → Open Network Stream…** (Ctrl+N).
2. Network URL: `http://SAATJA-IP:8080/demo` (asenda SAATJA-IP).
3. Vajuta **Play**. Video peaks hakkama mängima mõne sekundi pärast.

## 3. Töölaua voog (latentsuse mõõtmiseks)

Saatja asemel allikaks töölaud: **Media → Open Capture Device…** → *Capture mode:* **Desktop**, *Desired frame rate:* **10** → nupu *Play* kõrvalt ▾ → **Stream** ja jätka sammust 3 (HTTP, 8080, /demo, H.264). Vastuvõtja avab sama aadressi.

## 4. Mõõda latentsus

1. Saatja avab oma ekraanil stopperi (Windows: *Clock → Stopwatch*) ja käivitab selle.
2. Vastuvõtja ekraanil mängib voog, kus saatja stopper on näha. Tee telefoniga **üks foto**, kus on korraga näha mõlemad ekraanid: saatja päris stopper ja selle koopia vastuvõtja ekraanil.
3. **Latentsus = saatja päris stopperi aeg − vastuvõtja ekraanil nähtav aeg.**

| Mõõtmine | Ühendus (Wi-Fi / kaabel) | Latentsus (s) |
|---|---|---|
| 1 | | |
| 2 | | |
| 3 | | |
| **Keskmine** | | |

**Samal ajal:** ava saatjal ja vastuvõtjal Task Manager (Ctrl+Shift+Esc → Performance → Ethernet/Wi-Fi) ja kirjuta üles *Send* ja *Receive* (Mbps). Vt Windowsi võrguvahendite spikker.

**Arutelu:** miks viivitus on mitu sekundit, kui võrk on kiire? (Vihje: puhverdus, kodeerimine, dekodeerimine.) Kuidas muutub tulemus Wi-Fi ja kaabliga?

## 5. Kui midagi ei tööta

| Probleem | Mida teha |
|---|---|
| Vastuvõtja ei ühendu | Kontrolli IP, porti (8080), kirjutamisviisi (`http://`, mitte `https://`) ja `ping`-i. |
| Windowsi tulemüür | *Windows Security → Firewall → Allow an app* → lisa **VLC** ja märgi **Private**. |
| Klassi Wi-Fi ei lase seadmeid kokku | Kasutage kaablit või tehke demo õpetaja arvutiga. VPN peab olema välja lülitatud. |
| Pilt hangub või kaadreid jääb vahele, protsessor 100 % | Vähenda töölaua *frame rate* 5-ni või kasuta lühemat/väiksemat videot. |
| Viivitust tahaks vähendada | Vastuvõtja: *Tools → Preferences → Show settings: All → Input/Codecs → Network caching (ms)* = 300. Liiga väike väärtus tekitab katkeid. |
| Voo lõpetamine | Saatja vajutab VLC-s **Stop**. |
