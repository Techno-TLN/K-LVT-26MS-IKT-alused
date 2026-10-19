# Windowsi vahendid võrgu jõudluse vaatamiseks

<p class="sub">Kohtumine 4 · Task Manager, Resource Monitor, käsurida ja PowerShell · Windows 10/11</p>

**Eesmärk:** näha oma arvutis, kui palju andmeid võrgus liigub, milline programm seda kasutab ja kui kiire ning stabiilne ühendus on.

## 1. Mida vaadata ja kust

**Praegune liiklus:** Task Manager · **Milline programm:** Resource Monitor · **Ühenduse kiirus:** `netsh` või `Get-NetAdapter` · **Latentsus ja pakettide kadu:** `ping`, `tracert`, `pathping`.

## 2. Task Manager: reaalajas liiklus

1. Ctrl+Shift+Esc → vasakult **Performance** → vali **Ethernet** (kaabel) või **Wi-Fi**.
2. Graafik **Throughput** näitab liiklust. Allpool on **Send** (saadetud) ja **Receive** (vastu võetud) ühikutes **Kbps/Mbps** (bitid sekundis, nagu ribalaius).
3. Katsetus: käivita speedtest ja jälgi, kuidas **Receive** tõuseb ligikaudu sinu allalaadimiskiiruseni.

## 3. Resource Monitor: kes võrku kasutab

1. Win+R → `resmon` → vahekaart **Network**.
2. **Processes with Network Activity**: iga programmi *Send*, *Receive* ja *Total* (**baiti sekundis**). Sorteeri veeru *Total* järgi.
3. **TCP Connections**: veerud **Packet Loss (%)** ja **Latency (ms)** näitavad pakettide kadu ja latentsust iga ühenduse kohta.

## 4. Käsurida (Command Prompt)

| Käsk | Mida näitab | Mida lugeda |
|---|---|---|
| `ipconfig` | IP, mask, gateway | *IPv4 Address*, *Default Gateway* |
| `ping -n 10 google.com` | latentsus ja pakettide kadu | *Minimum / Maximum / Average*, *Lost* |
| `tracert google.com` | tee sihini, latentsus iga hüppe kohta | kus latentsus järsult kasvab |
| `pathping -q 10 google.com` | pakettide kadu iga hüppe kohta (võtab ~1–2 min) | veerg *Lost/Sent* |
| `netsh wlan show interfaces` | Wi-Fi ühendus | *Signal*, *Receive rate (Mbps)*, *Transmit rate (Mbps)* |

## 5. PowerShell

**Eeltingimused:** moodul **NetAdapter** on Windows 10/11 sees olemas (*Install-Module* pole vaja), ühendamist (*Connect-…*) ei vaja ja lugemiseks piisab tavalisest kasutajast (administraatori õigusi ei vaja). Ava *Windows PowerShell* (Start → otsi „PowerShell").

```
Get-NetAdapter | Format-Table Name, Status, LinkSpeed
Get-NetAdapterStatistics | Format-Table Name, ReceivedBytes, SentBytes
```

Esimene näitab **ühenduse kiirust** (*LinkSpeed*, nt 1 Gbps), teine kokku liikunud baite. **Baidid ja bitid:** Resource Monitor annab **baite**, Task Manager **bitte**: B/s × 8 ÷ 1 000 000 = Mbps (1 250 000 B/s = 10 Mbps).

## 6. Mini-harjutus (5 min)

| Mida teed | Mida loed | Tulemus |
|---|---|---|
| Speedtest | speedtesti allalaadimine (Mbps) | |
| Sama ajal Task Manager | *Receive* tipp (Mbps) | |
| VLC voog (saatja) | *Send* (Mbps) | |
| VLC voog (vastuvõtja) | *Receive* (Mbps) | |
| `Get-NetAdapter` | *LinkSpeed* | |

**Küsimus:** miks on *Receive* tipp tavaliselt veidi väiksem kui speedtesti tulemus? Kuidas VLC voo *Send* võrdub valitud bitikiirusega?
