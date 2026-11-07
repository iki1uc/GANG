import hashlib

def schweissen(tabs):
    # tabs = Liste mit 3 Datei-Inhalten
    clean = [t.split("// STATE:")[0] for t in tabs]
    hashes = set(hashlib.sha256(c.encode()).hexdigest() for c in clean)
    print("Quelle identisch?", len(hashes)==1)  # True = 0 Bytes Unterschied
    # Löten: stärkster STATE gewinnt
    welded = clean[0] + "\n// GESCHWEISST: EICH=fest, VERIFY=on, HOME=40\n"
    return welded

def loeten(a, b):
    # Löten = 2 Teile mit Zinn verbinden, nicht schmelzen
    # Schweißen = 2 Teile verschmelzen zu 1
    return a + "\n// LOT: " + b
