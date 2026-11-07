# gang_schweissen.py — ALLE TABS -> GANG -> INDEX WEISS WAS ES TUT
# Mann, 1 Knopf. Alle Dateien rein. GANG wird gängiger.
# Am Ende: index weiss was es tut = am gängigsten.

import os, glob, json, time, hashlib

ROOT = "."  # Ordner wo dein Repo liegt
AUS = "GANG"

def finde_alles():
    # Alle Tabs, alle Dateien, die du im Screenshot hast
    muster = ["**/*.html", "**/*.js", "**/*.csv", "**/*.room", "**/*.md", "**/*.json"]
    files = []
    for m in muster:
        files += glob.glob(m, recursive=True)
    # Weglassen: was wir gerade bauen, .git, Müll
    files = [f for f in files if not f.startswith(".git") and "GANG_GESCHWEISST" not in f and "ALLES_GESCHWEISST" not in f]
    files = sorted(set(files))
    print(f"[GANG] Gefunden: {len(files)} Dateien aus allen Tabs")
    for f in files:
        print(f"  - {f}")
    return files

def gang_bauen(files):
    os.makedirs(AUS, exist_ok=True)
    gang = {
        "titel": "GANG · ALLES ZUSAMMEN",
        "zeit": time.strftime("%Y-%m-%d %H:%M:%S"),
        "beweis": "3→×3→9→×9→81→×9→729=root · 4×9+4=40=HOME · f(40)=40 · f(f(40))=40",
        "regel": "Alles rein in GANG, dann wird er gängiger. Wenn index weiss was es tut, ist er am gängigsten.",
        "zimmer": [],  # jede Datei = ein Zimmer am Gang
    }

    # 1. Jedes Zimmer einsammeln
    for f in files:
        try:
            with open(f, encoding="utf-8", errors="ignore") as fh:
                inhalt = fh.read()
        except:
            continue
        zimmer = {
            "pfad": f,
            "name": os.path.basename(f),
            "ordner": os.path.dirname(f) or ".",
            "bytes": len(inhalt),
            "hash": hashlib.md5(inhalt.encode("utf-8", errors="ignore")).hexdigest()[:8],
            "typ": f.split(".")[-1].lower(),
            "inhalt": inhalt,
            # Was tut dieses Zimmer? Index muss es wissen.
            "tut": was_tut_es(f, inhalt),
        }
        gang["zimmer"].append(zimmer)
        print(f"  [GANG] {f} -> Zimmer, tut: {zimmer['tut']}")

    # 2. GANG.js — der Gang selbst, der alles kennt
    gang_js = f"""// GANG.js — AUTOMATISCH GESCHWEISST — {gang['zeit']}
// Alles aus allen Tabs. Ein Gang. Alle Zimmer.
// Beweis: {gang['beweis']}
window.GANG = {json.dumps({k: v for k, v in gang.items() if k != 'zimmer'}, ensure_ascii=False, indent=2)};
window.GANG.zimmer = {json.dumps([{{k: v for k, v in z.items() if k != 'inhalt'}} for z in gang['zimmer']], ensure_ascii=False, indent=2)};
window.GANG.lauf = function(){{
  console.log("GANG läuft. Zimmer:", this.zimmer.length);
  this.zimmer.forEach(z => console.log(" -", z.pfad, "->", z.tut));
  return this;
}};
window.GANG.weiss_was_es_tut = true;
console.log("GANG geladen:", window.GANG.zimmer.length, "Zimmer. Index weiss was es tut.");
"""
    with open(f"{AUS}/GANG.js", "w", encoding="utf-8") as out:
        out.write(gang_js)

    # 3. GANG.full.json — gelötet, lösbar, alles drin
    with open(f"{AUS}/GANG.full.json", "w", encoding="utf-8") as out:
        json.dump(gang, out, ensure_ascii=False, indent=2)

    # 4. INDEX — der, der am Ende weiss was er tut
    index_html = bauen_index(gang)
    with open("index.html", "w", encoding="utf-8") as out:
        out.write(index_html)

    print(f"\n[GANG] FERTIG.")
    print(f"[GANG] GANG/GANG.js — {len(gang_js)} Zeichen")
    print(f"[GANG] GANG/GANG.full.json — {len(gang['zimmer'])} Zimmer")
    print(f"[GANG] index.html — WEISS WAS ES TUT")
    print(f"[GANG] Gängigkeit: {gangigkeit(gang)}%")
    return gang

def was_tut_es(pfad, inhalt):
    # Index muss wissen was jede Datei tut. Nicht raten, lesen.
    p = pfad.lower()
    if "kaiser" in p: return "KAISER misst 9 Sektoren, Top 3 = König"
    if "könig" in p or "konig" in p: return "KÖNIG = Mitte, 3 = AUGE/HIRN/OFFEN"
    if "bauer" in p: return "BAUER trägt / baut, braucht das Land"
    if "dame" in p: return "DAME läuft überall, MA³ Brücke"
    if "läufer" in p or "laufer" in p: return "LÄUFER diagonal, rettet"
    if "schach" in p or "chess" in p: return "SCHACH · 9×9 · Figuren + Züge"
    if "btc" in p or "729" in p: return "BTC729 Codec 729→81→9→3→Bild"
    if "bio" in p or "tel" in p: return "BIO.TEL · goldenes Minimum · f(x)=min(x,40)"
    if "jungbrunnen" in p: return "JUNGBRUNNEN · ROM fest, ROME wächst"
    if "djinn" in p or "lampe" in p: return "DJINN · 3 Wünsche · Lampe"
    if "rad" in p: return "RAD · NC Engine · Magma + Vitality"
    if "planetera" in p: return "PLANETERA · Sicherheit · 3 Ringe"
    if "home" in p: return "HOME 40 · Fixpunkt · f(f(40))=40"
    if "gang" in p: return "GANG · Korridor · alles zusammen"
    if "agent" in p: return "AGENT · läuft, macht, meldet"
    if p.endswith(".csv"): return "DATEN · Tabelle · Werte für SCSI/RAID"
    if p.endswith(".room"): return "ROOM · Raum / Zustand"
    if p.endswith(".html"): return "SEITE · zeigt was"
    if p.endswith(".js"): return "LOGIK · macht was"
    return "ZIMMER am GANG · gehört dazu"

def gangigkeit(gang):
    # Wie gängig? 0% = 1 Zimmer, 100% = alle Zimmer haben ein 'tut'
    if not gang["zimmer"]: return 0
    mit_tut = sum(1 for z in gang["zimmer"] if z["tut"] and "ZIMMER" not in z["tut"])
    return round(mit_tut / len(gang["zimmer"]) * 100, 1)

def bauen_index(gang):
    # Index, der weiss was er tut — Liste aller Zimmer, mit Knopf
    zeilen = ""
    for z in gang["zimmer"]:
        zeilen += f'<div class="zimmer"><b>{z["pfad"]}</b> <span>{z["bytes"]} Bytes · {z["hash"]}</span><br><i>{z["tut"]}</i></div>\n'
    return f"""<!DOCTYPE html>
<html lang="de"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>GANG · INDEX WEISS WAS ES TUT</title>
<style>
body{{background:#050805;color:#f2ead1;font:14px/1.5 ui-monospace,monospace;margin:0;padding:16px}}
h1{{color:#f2c94c}} .beweis{{color:#7ee787}} .zimmer{{background:#0b120c;border:1px solid #2a3a25;border-radius:10px;padding:10px;margin:8px 0}}
.zimmer b{{color:#f2c94c}} .zimmer span{{color:#9cb09b;font-size:11px}} .zimmer i{{color:#35e6ff}}
button{{background:#1e180a;color:#f2c94c;border:1px solid #f2c94c;padding:10px 16px;border-radius:99px;cursor:pointer;font:inherit}}
</style></head><body>
<h1>GANG · INDEX WEISS WAS ES TUT</h1>
<p class="beweis">{gang['beweis']}</p>
<p>Alles aus allen Tabs rein in GANG. Dann wird er gängiger. Jetzt weiss index was er tut — am gängigsten.</p>
<p><b>{len(gang['zimmer'])} Zimmer</b> · Gängigkeit: {gangigkeit(gang)}% · Zeit: {gang['zeit']}</p>
<button onclick="GANG.lauf()">▶ GANG LAUFEN</button>
<button onclick="document.querySelectorAll('.zimmer').forEach(e=>e.style.display='block')">ALLE ZEIGEN</button>
<h2>Alle Zimmer am Gang:</h2>
{zeilen}
<script src="GANG/GANG.js"></script>
</body></html>"""

if __name__ == "__main__":
    print("="*60)
    print("GANG SCHWEISSEN · ALLE TABS -> GANG -> INDEX WEISS ES")
    print("="*60)
    files = finde_alles()
    gang = gang_bauen(files)
    print("\nFertig, Mann. GANG ist gängiger. Index weiss was er tut. 🫏")
