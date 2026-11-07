import pathlib

# 1. Alle deine Tabs sammeln
ordner = pathlib.Path(".")  # Ordner wo deine Tabs liegen
tabs = list(ordner.rglob("*.html")) + list(ordner.rglob("*.js")) + list(ordner.rglob("*.csv"))
print(f"Gefunden: {len(tabs)} Tabs")

# 2. GANG bauen — jeder Tab wird 1 Station im Gang
gang = []
gang.append("<!-- GANG.root — alle Tabs -> 1 Gang | HOME 40 | f(f(x))=f(x) -->")
gang.append("<script>window.GANG = { tabs: [], lvl: 0, home: 40 }; </script>")

for i, tab in enumerate(tabs):
    name = tab.name
    # Nur Name + Pfad reinschweissen, nicht den ganzen Inhalt — sonst Hölle
    gang.append(f'<!-- GANG-STATION {i+1}: {name} | Pfad: {tab} -->')
    gang.append(f'<script>window.GANG.tabs.push("{name}");</script>')

gang.append("""
<script>
  // INDEX weiss was er tut — das ist der Kopf
  window.GANG.weiss = function(){
    console.log("GANG:", window.GANG.tabs.length, "Stationen");
    console.log("Reihenfolge: Axiom -> HESS -> C -> Q -> Z -> HOME 40");
    console.log("HOME 40 = 4*9+4 = 40 | f(40)=40 | FIXPOINT");
    window.GANG.lvl = 5;
    return window.GANG;
  };
</script>
""")

pathlib.Path("GANG_GESCHWEISST.html").write_text("\\n".join(gang), encoding="utf-8")
print("Fertig: GANG_GESCHWEISST.html")
print("Regel: INDEX weiss -> GANG ist gängig")
