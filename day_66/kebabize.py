# Modify the kebabize function so that it converts a camel case string into a
# kebab case.

# "camelsHaveThreeHumps"  -->  "camels-have-three-humps"
# "camelsHave3Humps"  -->  "camels-have-humps"
# "CAMEL"  -->  "c-a-m-e-l"

# Notes:
# the returned string should only contain lowercase letters

###############################################################################

# solution
def kebabize(text: str) -> str:
    result = ''

    for char in text:
        if char.isupper():
            result += f"-{char.lower()}"
        elif char.islower():
            result += char
        else:
            result += ''
    
    return result.strip('-')


# tests
import unittest

class KebabizeTextTests(unittest.TestCase):
    test_cases = [
        ('myCamelCasedString', 'my-camel-cased-string'),
        ('myCamelHas3Humps', 'my-camel-has-humps'),
        ('SOS', 's-o-s'),
        ('42', ''),
        ('CodeWars', 'code-wars'),
    ]

    def test_kebabize_text(self):
        for tested, expected in self.test_cases:
            self.assertEqual(kebabize(tested), expected)


if __name__ == '__main__':
    unittest.main()
