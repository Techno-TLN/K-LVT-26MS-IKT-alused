# Kohtumine 2 — Arvusüsteemid ja andmemahu ühikud

**Kuupäev:** 21.09.2026 (E) · **Kestus:** 2 ak. tundi (90 min)

## Tunni sisu

- Arvusüsteemid: kahend-, kümnend- ja kuueteistkümnendsüsteem ning nendevahelised teisendused.
- Nende seos bitt/bait mõistega.
- Andmemahu põhiühikud: bit, bait, KB/MB/GB/TB.
- Praktilised näited kuueteistkümnendsüsteemi kasutusest (nt MAC-aadressid, värvikoodid, mälu aadressid).
- Ülesande 2 tutvustus.

## Seos ÕV1-ga

Arvusüsteemid ja andmemahu ühikud on hilisemate ressursiarvutuste ([Kohtumine 3](03-teenuste-liigid-ja-riistvararessursid.md), [Kohtumine 4](04-vorguressursid-ja-video-kodeerimine.md)) matemaatiline alus — ilma nendeta ei saa arvutada, kui palju salvestusruumi või ribalaiust mingi teenus/rakendus vajab.

## Ülesanne 2 — Minu kodune võrk: IP, MAC, mask, gateway, DNS ja aadressiruum

**Maht:** 4 t · **Tähtaeg:** enne kohtumist 3 (05.10.2026, kell 20:00)

Täielik, õpilasele jagatav ülesandeleht on failis [`Ulesanne2_Minu_koduvork.docx`](Ulesanne2_Minu_koduvork.docx) samas kaustas — see laetakse Teamsi üles ülesandena. Kokkuvõte:

- **A osa (võrguandmete leidmine):** Õpilane leiab oma koduse arvuti tegelikud võrguseaded käsu `ipconfig /all` (Windows) või `ifconfig` / süsteemiseadete (macOS) abil: MAC-aadress, IPv4-aadress, alammask, vaikelüüs (gateway) ja DNS-serverid. Lisab ekraanipildi tõendusena.
- **B osa (isikupärastatud arvutus):** Oma leitud alammaski põhjal arvutab käsitsi CIDR-tähise, hosti-bittide arvu ja kasutatavate IP-aadresside arvu (2^hosti-bitid − 2), samuti võrgu- ja leviaadressi. Kontrollib tulemust tunnis jagatud Exceli tööriistaga `IP_mask_võrguaadress_kalkulaator.xlsx` (leht „IP, mask, võrguaadress”).
- **C osa (boonus):** Uurib ruuteri haldusliidesest, mitu seadet on hetkel võrku ühendatud, ja võrdleb seda B osas arvutatud teoreetilise mahuga.

**Esitamine:** PDF Teamsi ülesandena. Vt [üldist esitamise korda](README.md#esitamise-üldkord).

**AI-kindlus ja kontrollitavus:** Iga õpilase kodune võrk (IP-vahemik, alammask, ühendatud seadmed) on erinev — valmisvastuse jagamine ei anna õiget tulemust ning nõutud ekraanipildid tõendavad, et arvutus tehti reaalse, enda seadme andmetega.

### Arvestamise kriteeriumid

Ülesanne loetakse **arvestatuks**, kui:
- kõik viis A osa parameetrit (MAC, IP, mask, gateway, DNS) on esitatud koos ekraanipildiga;
- CIDR, hosti-bittide arv ja kasutatavate aadresside arv on käsitsi õigesti arvutatud, arvutuskäik nähtav;
- tulemus on kontrollitud Exceli tööriistaga ja vastav ekraanipilt on lisatud;
- esitatud tähtajaks, nõutud failinimega.

C osa (boonus) annab lisapunkte, kuid selle puudumine ei mõjuta ülesande arvestatuks lugemist.

---
[← Eelmine: Kohtumine 1](01-sissejuhatus-ja-oppekorraldus.md) | [Indeks](README.md) | [Järgmine: Kohtumine 3 →](03-teenuste-liigid-ja-riistvararessursid.md)
