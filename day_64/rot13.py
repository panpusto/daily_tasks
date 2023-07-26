# ROT13 is a simple letter substitution cipher that replaces a letter with
# the letter 13 letters after it in the alphabet. ROT13 is an example of
# the Caesar cipher.

# Create a function that takes a string and returns the string ciphered
# with Rot13. If there are numbers or special characters included in the
# string, they should be returned as they are. Only letters from the
# latin/english alphabet should be shifted, like in the original Rot13 
# "implementation".

# Please note that using encode is considered cheating.

###############################################################################

# solution
import string

def rot13_cipher(message: str) -> str:
    alphabet_low = string.ascii_lowercase
    alphabet_up = string.ascii_uppercase
    encoded_text = ''

    for char in message:
        if char.isalpha():
            if char.isupper():
                encoded_text += alphabet_up[(alphabet_up.index(char) + 13) % 26]
            else:
                encoded_text += alphabet_low[(alphabet_low.index(char) + 13) % 26]
        else:
            encoded_text += char

    return encoded_text


# tests
import unittest

class EncodeMessageTests(unittest.TestCase):
    def test_rot13_cipher_fixed_strings_simple(self):
        self.assertEqual(rot13_cipher('test'), 'grfg')
        self.assertEqual(rot13_cipher('Test'), 'Grfg')
        self.assertEqual(rot13_cipher('Codewars'), 'Pbqrjnef')
        self.assertEqual(rot13_cipher('Avoid success at all costs!'), 'Nibvq fhpprff ng nyy pbfgf!')
        self.assertEqual(rot13_cipher('10+2 is twelve.'), '10+2 vf gjryir.')
        self.assertEqual(rot13_cipher('abcdefghijklmnopqrstuvwxyz'), 'nopqrstuvwxyzabcdefghijklm')
        
    def test_rot13_cipher_fixed_strings_edge_cases(self):
        self.assertEqual(rot13_cipher(''), '')
        self.assertEqual(rot13_cipher('ZZZZZZZZZzzzzzzzzz'), 'MMMMMMMMMmmmmmmmmm')
        self.assertEqual(rot13_cipher('1     3     abzzq  &!  2   z'), '1     3     nommd  &!  2   m')
        self.assertEqual(rot13_cipher('aA bB zZ 1234 *!?%'), 'nN oO mM 1234 *!?%')
        self.assertEqual(rot13_cipher('!@#$%^&*+?~()_-+=:;'), '!@#$%^&*+?~()_-+=:;')
        
    def test_rot13_cipher_fixed_strings_twice_return_original(self):
        self.assertEqual(rot13_cipher(rot13_cipher('do i return to original ?!')), 'do i return to original ?!')
        self.assertEqual(rot13_cipher(rot13_cipher('DO I RETURN TO ORIGINAL ?!')), 'DO I RETURN TO ORIGINAL ?!')
        self.assertEqual(rot13_cipher(rot13_cipher('123456 !@#$%^&*+?~()_-+=:;')), '123456 !@#$%^&*+?~()_-+=:;')
        self.assertEqual(rot13_cipher(rot13_cipher('abcdEFGH1234 *>>>!!~~ ggg JJ7z')), 'abcdEFGH1234 *>>>!!~~ ggg JJ7z')


if __name__ == '__main__':
    unittest.main()
