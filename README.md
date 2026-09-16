# 🂡 Skat-Liste

Punkteliste für Skat mit 3–5 Spielern — eine einzige HTML-Datei, kein Server, kein Build, funktioniert offline.

**▶ Live:** https://kambodscharoger294-cyber.github.io/skat-liste/

## Was sie kann

- **3–5 Spieler** mit Namen, faire Geber-Rotation automatisch:
  - 3 Spieler → alle spielen jede Runde
  - 4 Spieler → der Geber setzt aus
  - 5 Spieler → Geber **und** ein weiterer setzen aus — niemand setzt zweimal hintereinander
- **Solo-Einträge**: nur der Solospieler bekommt ± Spielwert, die Gegner keinen Eintrag
- **Runde zurücknehmen** (Undo) und Liste zurücksetzen (Spieler bleiben erhalten)
- **Schriftgröße** (A−/A+) und **Hell/Dunkel-Theme**
- **Offline-fähig** durch Service Worker — einmal geladen, geht auch ohne Netz (z. B. am Kaffeetisch)
- **Zum Home-Bildschirm**: in Safari „Teilen“ → „Zum Home-Bildschirm“ → startet wie eine eigene App im Vollbild (iPhone/iPad)

## Liste teilen & sichern

- **Sichern / Laden**: Liste als Text sichern, auf anderem Gerät wieder einfügen
- **QR-Code**: aktueller Listenstand als QR zum Scannen — praktisch, um den Stand nach dem Abendspielen mitzunehmen
- Der Stand liegt außerdem im `localStorage` des Browsers und überlebt dadurch Neustarts

## Starten

### Online
Einfach den Live-Link oben öffnen. HTTPS ist Pfad (Service Worker), Chrome/Safari laden die Seite in den Cache.

### Lokal
```bash
python3 serve.py          # http://localhost:8787
```
Alternativ `index.html` direkt per Datei-URL öffnen — das Spiel selbst läuft auch ohne HTTP, nur der Service Worker (Offline-Cache) braucht einen kleinen lokalen Server.

## Technik

- **Eine Datei**: `index.html` enthält Markup, CSS und JavaScript (Vanilla, kein Framework)
- **Service Worker** (`sw.js`, Cache `skat-liste-v6`): App-Shell offline cachen, Navigate-Requests als Fallback auf `/`
- **QR-Code**: eingebetteter Generator (qrcode-generator, MIT-Lizenz)
- Kein Tracking, keine externen Requests außer dem eigenen Hosting

## Deployment

Die Seite läuft auf **GitHub Pages** (legacy Build aus `main`):

1. Änderungen an `index.html` machen
2. Commit + `git push`
3. GitHub baut automatisch neu (dauert ~1 Minute)

Nach Änderungen am Offline-Cache die Versionsnummer in `sw.js` (`skat-liste-v6`) hochziehen, damit Clients den neuen Stand laden.

---

*© 2026 — gebaut für den eigenen Skatabend.*
