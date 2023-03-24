# Write two functions that convert a roman numeral to and from an integer value.
# Multiple roman numeral values will be tested for each function.

# Modern Roman numerals are written by expressing each digit separately starting with the left most digit
# and skipping any digit with a value of zero. 
# In Roman numerals 1990 is rendered: 1000=M, 900=CM, 90=XC; resulting in MCMXC. 
# 2008 is written as 2000=MM, 8=VIII; or MMVIII. 1666 uses each Roman symbol in descending order: MDCLXVI.

# Input range : 1 <= n < 4000

# In this kata 4 should be represented as IV, NOT as IIII (the "watchmaker's four").

# Examples

# to roman:
# 2000 -> "MM"
# 1666 -> "MDCLXVI"
# 1000 -> "M"
#  400 -> "CD"
#   90 -> "XC"
#   40 -> "XL"
#    1 -> "I"

# from roman:
# "MM"      -> 2000
# "MDCLXVI" -> 1666
# "M"       -> 1000
# "CD"      -> 400
# "XC"      -> 90
# "XL"      -> 40
# "I"       -> 1


#  solution
import unittest


class RomanNumerals:
    roman_numeral_map = {
        'M': 1000, 'CM': 900, 'D': 500, 'CD': 400, 
        'C': 100, 'XC': 90, 'L': 50, 'XL': 40, 
        'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'I': 1
    }
    
    @staticmethod
    def to_roman(arabic_num):
        roman_numeral = ''
        while arabic_num > 0:
            for r, n in RomanNumerals.roman_numeral_map.items():
                while arabic_num >= n:
                    roman_numeral += r
                    arabic_num -= n

        return roman_numeral

    @staticmethod
    def from_roman(roman_num):
        arabic_number = 0
        i = 0
        while i < len(roman_num):
            if i + 1 < len(roman_num) and roman_num[i:i+2] in RomanNumerals.roman_numeral_map:
                arabic_number += RomanNumerals.roman_numeral_map[roman_num[i:i+2]]
                i += 2
            else:
                arabic_number += RomanNumerals.roman_numeral_map[roman_num[i]]
                i += 1
        return arabic_number
    

#  tests
class RomanNumeralsTest(unittest.TestCase):
    def test_to_roman_funt(self):
        self.assertEqual(RomanNumerals.to_roman(1000), 'M')
        self.assertEqual(RomanNumerals.to_roman(4), 'IV')
        self.assertEqual(RomanNumerals.to_roman(1), 'I')
        self.assertEqual(RomanNumerals.to_roman(1990), 'MCMXC')
        self.assertEqual(RomanNumerals.to_roman(2008), 'MMVIII')
    def test_from_roman(self):
        self.assertEqual(RomanNumerals.from_roman('XXI'), 21)
        self.assertEqual(RomanNumerals.from_roman('I'), 1)
        self.assertEqual(RomanNumerals.from_roman('IV'), 4)
        self.assertEqual(RomanNumerals.from_roman('MMVIII'), 2008)
        self.assertEqual(RomanNumerals.from_roman('MDCLXVI'), 1666)

if __name__ == '__main__':
    unittest.main()