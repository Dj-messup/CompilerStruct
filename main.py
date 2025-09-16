# Driver for the float FSM

import argparse
import fsm_float as f

def run_one(s, ints_ok, trail_ok):
    ok = f.parse_float(s, accept_integers=ints_ok, accept_trailing_dot=trail_ok)
    print(f"{s!r} -> {'ACCEPT' if ok else 'REJECT'}")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("strings", nargs="*")
    ap.add_argument("--no-integers", action="store_true")
    ap.add_argument("--allow-trailing-dot", action="store_true")
    ap.add_argument("--repl", action="store_true")
    ap.add_argument("--debug", action="store_true")
    a = ap.parse_args()

    if a.debug:
        f.DEBUG_ON = True

    if a.repl:
        print("FSM REPL  Ctrl-D to exit")
        try:
            while True:
                s = input("> ")
                run_one(s, not a.no_integers, a.allow_trailing_dot)
        except EOFError:
            print()
        return

    if not a.strings:
        # quick demo set like in class
        demo = ["0", "+0", "-12", ".5", "5.", "12.34", "12.", "12.0",
                "12e3", "12E+3", "12.3e-4", "e10", ".e10", "--1", "3.14.15"]
        for s in demo:
            run_one(s, not a.no_integers, a.allow_trailing_dot)
    else:
        for s in a.strings:
            run_one(s, not a.no_integers, a.allow_trailing_dot)

if __name__ == "__main__":
    main()
