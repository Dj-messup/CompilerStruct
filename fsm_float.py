# Floating number FSM (table-driven)
# Form: [sign]? ( digits ('.' digits?)? | '.' digits ) ([eE] [sign]? digits)?

from enum import Enum, auto

DEBUG_ON = False
def DEBUG(msg, v=""):
    if DEBUG_ON:
        print(f"{msg}{v}")

class S(Enum):
    START = auto(); SIGN = auto(); WHOLE = auto()
    DOT = auto(); DOT_NO_WHOLE = auto(); FRAC = auto()
    EXP_MARK = auto(); EXP_SIGN = auto(); EXP = auto()

class C(Enum):           # input classes
    DIGIT = auto(); SIGN = auto(); DOT = auto(); E = auto(); OTHER = auto()

def cls(ch: str) -> C:
    if ch.isdigit(): return C.DIGIT
    if ch in "+-":   return C.SIGN
    if ch == ".":    return C.DOT
    if ch in "eE":   return C.E
    return C.OTHER

# transition[state][class] = next_state
T = {
    S.START:        {C.SIGN: S.SIGN, C.DIGIT: S.WHOLE, C.DOT: S.DOT_NO_WHOLE},
    S.SIGN:         {C.DIGIT: S.WHOLE, C.DOT: S.DOT_NO_WHOLE},
    S.WHOLE:        {C.DIGIT: S.WHOLE, C.DOT: S.DOT, C.E: S.EXP_MARK},
    S.DOT_NO_WHOLE: {C.DIGIT: S.FRAC},
    S.DOT:          {C.DIGIT: S.FRAC},
    S.FRAC:         {C.DIGIT: S.FRAC, C.E: S.EXP_MARK},
    S.EXP_MARK:     {C.SIGN: S.EXP_SIGN, C.DIGIT: S.EXP},
    S.EXP_SIGN:     {C.DIGIT: S.EXP},
    S.EXP:          {C.DIGIT: S.EXP},
}

def parse_float(s: str, accept_integers: bool = True, accept_trailing_dot: bool = False) -> bool:
    s = s.strip()
    if not s: return False
    st = S.START
    for ch in s:
        DEBUG("S=", st.name); DEBUG(" ch=", ch)
        st = T.get(st, {}).get(cls(ch))
        if st is None:
            return False
    # Accept sets match the circled finals
    accept = {S.FRAC, S.EXP}
    if accept_integers:     accept.add(S.WHOLE)
    if accept_trailing_dot: accept.add(S.DOT)
    return st in accept
