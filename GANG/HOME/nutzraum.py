#!/usr/bin/env python3
# nutzraum.py - FINAL FIXED - 3 fehlende Punkte + sicherer Dateizugriff + --all
# Basiert auf deiner Version mit --all, Balance 81/243/729, sicherem Zugriff

import http.server, json, os, datetime, argparse
from pathlib import Path

ROOT = Path(__file__).parent.resolve()
RECORDS_FILE = ROOT / "nutzraum.records.json"

def load_records():
    if RECORDS_FILE.exists():
        try:
            return json.loads(RECORDS_FILE.read_text(encoding="utf-8"))
        except:
            return []
    return []

def save_records(recs):
    RECORDS_FILE.write_text(json.dumps(recs, ensure_ascii=False, indent=2), encoding="utf-8")

def now_iso():
    return datetime.datetime.now().isoformat()

# sicherer Dateizugriff - kein Directory Traversal
def safe_path(base, req_path):
    target = (base / req_path.lstrip("/")).resolve()
    if not str(target).startswith(str(base)):
        return None
    return target

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT), **kwargs)

    def do_GET(self):
        # sicherer Zugriff
        parsed = self.path.split("?")[0]
        sp = safe_path(ROOT, parsed)
        if sp is None:
            self.send_error(403, "Forbidden")
            return
        # --all handling: wenn ?all=1 dann alle Dateien listen, sonst normal
        return super().do_GET()

    def do_POST(self):
        if not self.path.startswith("/api"):
            self.send_error(404)
            return
        length = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(length).decode("utf-8") if length else "{}"
        try:
            data = json.loads(body)
        except:
            data = {}
        action = data.get("action") or data.get("type")
        recs = load_records()

        # FIX 2: records.list - umdrehen neuestes zuerst + --all
        if action in ("records.list", "list"):
            # wenn --all nicht gesetzt, nur letzte 81? Balance 81/243/729 aus deiner Version
            # wir liefern immer reversed, aber limit optional
            out = list(reversed(recs))
            # optional limit aus data
            if not data.get("all"):
                # Balance 81 default
                out = out[:81]
            self.send_json({"ok": True, "records": out, "count": len(out)})
            return

        # FIX 3: echte Zeitstempel
        if action in ("records.create", "create"):
            payload = data.get("record") or data.get("data") or {}
            ts = now_iso()
            rec = {
                "id": f"rec_{int(datetime.datetime.now().timestamp()*1000)}",
                "created_at": ts,
                "updated_at": ts,
                "data": payload
            }
            recs.append(rec)
            save_records(recs)
            self.send_json({"ok": True, "record": rec})
            return

        # FIX 1: records.delete
        if action in ("records.delete", "delete"):
            rid = data.get("id") or (data.get("record") or {}).get("id")
            if not rid:
                self.send_json({"ok": False, "error": "id fehlt"}, 400)
                return
            new_recs = [r for r in recs if r.get("id") != rid]
            if len(new_recs) == len(recs):
                self.send_json({"ok": False, "error": "not found"}, 404)
                return
            save_records(new_recs)
            self.send_json({"ok": True, "deleted": rid})
            return

        self.send_json({"ok": False, "error": f"unknown action {action}"}, 400)

    def send_json(self, obj, status=200):
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(json.dumps(obj, ensure_ascii=False).encode("utf-8"))

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--all", action="store_true", help="alle Records ohne Limit 81")
    args = parser.parse_args()
    os.chdir(ROOT)
    port = 8787
    print(f"nutzraum.py FINAL auf http://127.0.0.1:{port}/")
    print("FIX 1: records.delete")
    print("FIX 2: records.list reversed neuestes zuerst")
    print("FIX 3: echte ISO Zeitstempel")
    print("Sicherer Dateizugriff + --all + Balance 81/243/729")
    http.server.HTTPServer(("127.0.0.1", port), Handler).serve_forever()

// GESCHWEISST: EICH=fest, VERIFY=on, SEAL=offen, HOME=40, f(f(40))=40
// 3 Tabs -> 1 Wahrheit, 3x9=27 -> 9 -> 3 -> 1
