import unittest
from fsm_float import parse_float

class T(unittest.TestCase):
    def test_defaults(self):
        self.assertTrue(parse_float("0"))
        self.assertTrue(parse_float(".5"))
        self.assertFalse(parse_float("5."))
        self.assertTrue(parse_float("12.34"))
        self.assertTrue(parse_float("12e3"))
        self.assertTrue(parse_float("12.3e-4"))
        self.assertFalse(parse_float("e10"))
        self.assertFalse(parse_float("3.14.15"))

    def test_flags(self):
        self.assertTrue(parse_float("5.", accept_trailing_dot=True))
        self.assertFalse(parse_float("123", accept_integers=False))

if __name__ == "__main__":
    unittest.main()
