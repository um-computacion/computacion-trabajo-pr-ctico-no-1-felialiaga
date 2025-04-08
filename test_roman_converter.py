import unittest
from roman_converter import decimal_to_roman

class TestDecimalARomano(unittest.TestCase):
    
    def test_basic(self):
        self.assertEqual(decimal_to_roman(1), "I")
        self.assertEqual(decimal_to_roman(5), "V")
        self.assertEqual(decimal_to_roman(10), "X")
        self.assertEqual(decimal_to_roman(50), "L")
        self.assertEqual(decimal_to_roman(100), "C")
        self.assertEqual(decimal_to_roman(500), "D")
        self.assertEqual(decimal_to_roman(1000), "M")
        
    def test_substraction(self):
        self.assertEqual(decimal_to_roman(4), "IV")
        self.assertEqual(decimal_to_roman(9), "IX")
        self.assertEqual(decimal_to_roman(40), "XL")
        self.assertEqual(decimal_to_roman(90), "XC")
        self.assertEqual(decimal_to_roman(400), "CD")
        self.assertEqual(decimal_to_roman(900), "CM")

    def test_complex(self):
        self.assertEqual(decimal_to_roman(44), "XLIV")
        self.assertEqual(decimal_to_roman(99), "XCIX")
        self.assertEqual(decimal_to_roman(444), "CDXLIV")
        self.assertEqual(decimal_to_roman(999), "CMXCIX")
        self.assertEqual(decimal_to_roman(1987), "MCMLXXXVII")

if __name__ == "__main__":
    unittest.main()