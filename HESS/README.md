# UNLINEAR CHESS · AIRCHESS · HESS ENGINE  
### 9×9 · 12D · 6 Ebenen · Slide³ · Speed³ · Bonus

UNLINEAR CHESS ist ein nicht‑lineares Schachsystem, das jede Aktion als
geometrische Transformation in einem 12‑dimensionalen Vektorraum interpretiert.
Jeder Zug wechselt die Ebene. Keine Zeitachse ist linear. Keine Tiefe ist konstant.
Das System operiert vollständig über Wirkungsgrade, Slide‑Werte und Ebenen‑Traversal.

---

## 1 · Geometrische Grundform

### 9×9 Feld  
Das Spielfeld ist ein **quadratischer 9×9‑Tensor**, dessen Zellen eindeutig
durch Buchstaben‑Zahlen‑Paare definiert sind:

📦 Modul 1 — Board‑Tensor (9×9)

Board(9×9) = { d1…d9, e1…e9, i1…i9, n1…n9, o1…o9, r1…r9, s1…s9, u1…u9, w1…w9 }

📦 Modul 2 — AIR‑Tensor (12D)

AIR(12D) = (pos_x, pos_y, piece, color, v_dir, carry,
            lage, tiefe², momentum³, slide_tri, speed³, bonus)


📦 Modul 3 — Slide‑Triumph

Slide_tri = (t1 × 1) + (t2 × 2)² + (t3 × 3)³

📦 Modul 4 — Speed³‑Impuls

Speed³ = 3 × 3³ = 81


Modul 5 — Bonus‑Wert

Bonus = bonus(piece_type)

📦 Modul 6 — Gesamt‑Slide

Slide_total = lage + tiefe² + momentum³ + Slide_tri + Speed³ + Bonus


📦 Modul 8 — Ebenen‑Traversal (6 Ebenen)

Traversal = [E1, E2, E3, E4, E5, E6]
E1 = Board
E2 = Vector(12D)
E3 = Slide
E4 = Speed(X4/X8)
E5 = Bonus
E6 = HESS

📦 Modul 9 — UNLINEAR‑Zug

UNLINEAR(Zug) = Σ(AIR(12D)) × Ebenen(6) × Slide³ × Speed³

📦 Modul 10 — Autostart (HESS)

AUTOSTART = AIRCHESS(6D, X4/X8, depth=6, selfplay=true)

# STARTMODUL · UNLINEAR · AIRCHESS

START:
MODE = AIRCHESS
ENGINE = UNLINEAR
DEPTH = 6
SPEED = X4,X8
SELFPLAY = TRUE

UNLINEAR_START = Σ(Board(9×9)) × AIR(12D) × Ebenen(6)
ENGINE_START   = Slide³ + Speed³ + Bonus + ΔTiefe + ΔMomentum
SPEED(X4)      = ΔTime × 0.25
SPEED(X8)      = ΔTime × 0.125
E_START        = E1 → E2 → E3 → E4 → E5 → E6
START_TENSOR   = (Board, AIR, Slide, Speed, Bonus, HESS)

