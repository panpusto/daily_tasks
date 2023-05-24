# Step 1: Create a function called encode() to replace all the lowercase vowels
# in a given string with numbers according to the following pattern:

# a -> 1
# e -> 2
# i -> 3
# o -> 4
# u -> 5

# For example, encode("hello") would return "h2ll4". There is no need to
# worry about uppercase vowels in this kata.

# Step 2: Now create a function called decode() to turn the numbers back into
# vowels according to the same pattern shown above.

# For example, decode("h3 th2r2") would return "hi there".

# For the sake of simplicity, you can assume that any numbers passed into the
# function will correspond to vowels.


# solution_1
def encode_loop(st: str) -> str:
    vowels = {
        'a': '1',
        'e': '2',
        'i': '3',
        'o': '4',
        'u': '5'
    }
    encoded_text = ''
    for char in st:
        if char in vowels.keys():
            encoded_text += vowels[char]
        else:
            encoded_text += char

    return encoded_text

def decode_loop(st: str) -> str:
    numbers = {
        '1': 'a',
        '2': 'e',
        '3': 'i',
        '4': 'o',
        '5': 'u'
    }
    decoded_text = ''
    for char in st:
        if char in numbers.keys():
            decoded_text += numbers[char]
        else:
            decoded_text += char

    return decoded_text


# solution_2
CIPHER = '12345', 'aeiou'

def encode(st: str) -> str:
    encode_cipher = str.maketrans(CIPHER[1], CIPHER[0])
    return st.translate(encode_cipher)

def decode(st: str) -> str:
    decode_cipher = str.maketrans(CIPHER[0], CIPHER[1])
    return st.translate(decode_cipher)


# tests
import unittest

class VowelCodeBasicTests(unittest.TestCase):
    def test_encode_loop(self):
        self.assertEqual(encode_loop('hello'), 'h2ll4')
        self.assertEqual(encode_loop('How are you today?'), 'H4w 1r2 y45 t4d1y?')
        self.assertEqual(encode_loop('This is an encoding test.'), 'Th3s 3s 1n 2nc4d3ng t2st.')
    
    def test_decode_loop(self):
        self.assertEqual(decode_loop('h2ll4'), 'hello')
        self.assertEqual(decode_loop('H4w 1r2 y45 t4d1y?'), 'How are you today?')
        self.assertEqual(decode_loop('Th3s 3s 1n 2nc4d3ng t2st.'), 'This is an encoding test.')
    
    def test_encode(self):
        self.assertEqual(encode('hello'), 'h2ll4')
        self.assertEqual(encode('How are you today?'), 'H4w 1r2 y45 t4d1y?')
        self.assertEqual(encode('This is an encoding test.'), 'Th3s 3s 1n 2nc4d3ng t2st.')
    
    def test_decode(self):
        self.assertEqual(decode('h2ll4'), 'hello')
        self.assertEqual(decode('H4w 1r2 y45 t4d1y?'), 'How are you today?')
        self.assertEqual(decode('Th3s 3s 1n 2nc4d3ng t2st.'), 'This is an encoding test.')


if __name__ == '__main__':
    unittest.main()
