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

