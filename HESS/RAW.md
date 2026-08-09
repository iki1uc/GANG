# RAW · UNLINEAR CHESS · AIRCHESS · HESS  
## Tensor‑Geometrie · 9×9 · 12D · Slide³ · Speed³ · Ebenen‑Traversal

Dieses Dokument beschreibt die vollständige geometrische Rohstruktur (RAW)
des UNLINEAR‑CHESS‑Systems. Alle Berechnungen basieren auf Tensoren,
die in 9×9‑Feldern, 12‑Dimensionen und 6 Ebenen organisiert sind.

---

# 1 · 12D AIR‑TENSOR

Der zentrale Tensor des Systems ist der 12‑dimensionale AIR‑Tensor:

┌──────────────────────────────────────────────┐
│                12D AIR‑TENSOR                │
├───────────────┬───────────────┬─────────────┤
│ 6D CLASSIC     │ 6E EXTENDED   │ META        │
├───────────────┼───────────────┼─────────────┤
│ pos_x          │ lage_value    │ Slide_tri   │
│ pos_y          │ tiefe_value   │ Speed³      │
│ piece_type     │ momentum_value│ Bonus       │
│ color          │ slide_value   │ ΔTime       │
│ vector_dir     │ speed3_value  │ ΔDepth      │
│ carry_effect   │ bonus_value   │ ΔMomentum   │
└───────────────┴───────────────┴─────────────┘

Jede Zeile ist eine **Dimension**, jeder Block eine **Ebene**.

---

# 2 · 9×9 BOARD‑TENSOR

Das Spielfeld ist ein 9×9‑Tensor:

┌──────────────────────────────────────────────┐
│                9×9 BOARD‑TENSOR              │
├──────────────────────────────────────────────┤
│ d1 d2 d3 d4 d5 d6 d7 d8 d9                   │
│ e1 e2 e3 e4 e5 e6 e7 e8 e9                   │
│ i1 i2 i3 i4 i5 i6 i7 i8 i9                   │
│ n1 n2 n3 n4 n5 n6 n7 n8 n9                   │
│ o1 o2 o3 o4 o5 o6 o7 o8 o9                   │
│ r1 r2 r3 r4 r5 r6 r7 r8 r9                   │
│ s1 s2 s3 s4 s5 s6 s7 s8 s9                   │
│ u1 u2 u3 u4 u5 u6 u7 u8 u9                   │
│ w1 w2 w3 w4 w5 w6 w7 w8 w9                   │
└──────────────────────────────────────────────┘

Jede Zelle ist ein **Knoten**, der den 12D‑AIR‑Tensor trägt.

---

# 3 · SLIDE‑TRIUMPHTENSOR

Der Slide‑Tensor ist ein dreieckiger Zeit‑Tensor:

        t3³
       ╱
      ╱
     t2²
    ╱
   ╱
  t1

Formel:

Slide_tri = (t1 × 1) + (t2 × 2)² + (t3 × 3)³

Dieser Tensor ist **triangular‑exponentiell**, nicht linear.

---

# 4 · SPEED³‑TENSOR

Der Speed³‑Tensor ist ein Impuls‑Tensor:

┌───────────────┐
│ SPEED³‑TENSOR │
├───────────────┤
│ 3 × 3³ = 81    │
└───────────────┘

Er wird nur ausgelöst, wenn **3 Züge in 2 Sekunden** auftreten.

---

# 5 · EBENEN‑TRAVERSAL‑TENSOR

UNLINEAR CHESS springt durch 6 Ebenen:

┌──────────────────────────────┐
│      EBENEN‑TRAVERSAL        │
├───────────────┬──────────────┤
│ E1 Board       │ 9×9          │
│ E2 Vector      │ 12D          │
│ E3 Slide       │ Triangular   │
│ E4 Speed       │ X4 / X8      │
│ E5 Bonus       │ Kill‑Boost   │
│ E6 HESS        │ Battle‑Mode  │
└───────────────┴──────────────┘

Traversal:

E1 → E2 → E3 → E4 → E5 → E6 → E1 → …

Jeder Zug ist ein **Ebenen‑Sprung**, kein linearer Verlauf.

---

# 6 · WIRKUNGSGRAD‑TENSOR

Der Wirkungsgrad eines Zuges ist ein Summen‑Tensor:

┌──────────────────────────────┐
│      WIRKUNGSGRAD‑TENSOR     │
├──────────────────────────────┤
│ W = AXIOM + PUZZLE + Slide   │
│ Slide = L + T + M + Tri + S³ │
└──────────────────────────────┘

---

# 7 · UNLINEAR‑TENSOR

Die vollständige Transformation eines Zuges lautet:

UNLINEAR(Zug) = Σ(12D) × Ebenen(6) × Slide³ × Speed³

Dies ist die **geometrische Signatur** eines UNLINEAR‑Zuges.

---

# 8 · RAW‑Ziel

Dieses Dokument definiert die **Roh‑Geometrie** des Systems:

- Tensoren  
- Ebenen  
- Dimensionen  
- Zeit‑Triumph  
- Geschwindigkeit  
- Bonus  
- Wirkungsgrad  

Es bildet die Grundlage für:

- AIRchess  
- HESS  
- UNLINEAR Engine  
- 6D / 12D Traversal  
- Slide³ / Speed³ Mechanik

