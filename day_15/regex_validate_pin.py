# ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything
# but exactly 4 digits or exactly 6 digits.
# If the function is passed a valid PIN string, return true, else return false.
#
# Examples (Input --> Output)
#
# "1234"   -->  true
# "12345"  -->  false
# "a234"   -->  false

# solution 1
# import re
# def validate_pin(pin):
#     if len(pin) in (4, 6):
#         return True if re.match('^(\d{6}|\d{4})$', pin) else False
#     return False

# solution 2
def validate_pin(pin):
    return len(pin) in (4, 6) and pin.isdigit()
# tests
import unittest

class ValidatePinBasicTests(unittest.TestCase):
    def test_invalid_pin(self):
        self.assertEqual(validate_pin("1"), False)
        self.assertEqual(validate_pin("12"), False)
        self.assertEqual(validate_pin("123"), False)
        self.assertEqual(validate_pin("12345"), False)
        self.assertEqual(validate_pin("1234567"), False)
        self.assertEqual(validate_pin("-1234"), False)
        self.assertEqual(validate_pin("-12345"), False)
        self.assertEqual(validate_pin("1.234"), False)
        self.assertEqual(validate_pin("00000000"), False)

    def test_valid_pin(self):
        self.assertEqual(validate_pin("1234"), True)
        self.assertEqual(validate_pin("0000"), True)
        self.assertEqual(validate_pin("1111"), True)
        self.assertEqual(validate_pin("123456"), True)
        self.assertEqual(validate_pin("098765"), True)
        self.assertEqual(validate_pin("000000"), True)
        self.assertEqual(validate_pin("123456"), True)
        self.assertEqual(validate_pin("090909"), True)

    def test_pin_with_non_digit_value(self):
        self.assertEqual(validate_pin("a234"), False)
        self.assertEqual(validate_pin(".234"), False)


if __name__ == '__main__':
    unittest.main()
