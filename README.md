# CompilerStruct

## Grammar Specification

This project implements a parser for **floating point numbers** based on the FSM diagram from class.  
The language supports:

- Optional leading sign (`+` or `-`)
- Digits before and/or after a decimal point
- Optional exponent part (`e` or `E` followed by optional sign and digits)

### Accepting Rules
- Integers may be accepted if enabled (e.g., `42`).
- A trailing dot (e.g., `5.`) may be accepted if enabled.
- Exponent requires digits after `e` or `E`.

---

### BNF Grammar
<Float> ::= <Sign> <Digits> <Fraction> <Exponent>
<Sign> ::= "+" | "-" | ε
<Digits> ::= <Digit> <Digits> | <Digit>
<Fraction> ::= "." <Digits> | ε
<Exponent> ::= ("E" | "e") <SignedDigits> | ε
<SignedDigits> ::= <Sign> <Digits>
<Digit> ::= "0" | "1" | "2" | "3" | "4"
| "5" | "6" | "7" | "8" | "9"


---

### Examples

Accepts:
- `0`
- `+0`
- `-12`
- `.5`
- `12.34`
- `12e3`
- `12.3e-4`

Rejects:
- `e10` (missing digits before exponent)
- `.e10` (missing digits between `.` and `e`)
- `--1` (double sign not allowed)
- `3.14.15` (multiple decimal points)
