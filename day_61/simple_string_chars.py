# In this Kata, you will be given a string and your task will be to return a
# list of ints detailing the count of uppercase letters, lowercase, numbers
# and special characters, as follows.

# Solve("*'&ABCDabcde12345") = [4,5,5,3]. 
# --the order is: uppercase letters, lowercase, numbers and special characters.

# solution
from string import ascii_uppercase, ascii_lowercase, digits, punctuation

def count_chars(s: str) -> list[int]:
    upp_ltrs, low_ltrs, nums, special_chars = 0, 0, 0, 0

    for char in s:
        if char in ascii_uppercase:
            upp_ltrs += 1
        elif char in ascii_lowercase:
            low_ltrs += 1
        elif char in digits:
            nums += 1
        elif char in punctuation:
            special_chars += 1
    
    return [upp_ltrs, low_ltrs, nums, special_chars]


# tests
import unittest

class SimpleStringCharsTests(unittest.TestCase):
    test_cases = [
        ("Codewars@codewars123.com",[1,18,3,2]),
        ("bgA5<1d-tOwUZTS8yQ",[7,6,3,2]),
        ("P*K4%>mQUDaG$h=cx2?.Czt7!Zn16p@5H",[9,9,6,9]),
        ("RYT'>s&gO-.CM9AKeH?,5317tWGpS<*x2ukXZD",[15,8,6,9]),
        ("$Cnl)Sr<7bBW-&qLHI!mY41ODe", [10,7,3,6]),
        ("@mw>0=QD-iAx!rp9TaG?o&M%l$34L.nbft", [7,13,4,10]),
    ]

    def test_count_type_of_chars(self):
        for tested, expected in self.test_cases:
            self.assertEqual(count_chars(tested), expected)


if __name__ == '__main__':
    unittest.main()
