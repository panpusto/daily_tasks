# Happy Holidays fellow Code Warriors!

# Santa's senior gift organizer Elf developed a way to represent up to 26 
# gifts by assigning a unique alphabetical character to each gift.
# After each gift was assigned a character, the gift organizer
# Elf then joined the characters to form the gift ordering code.

# Santa asked his organizer to order the characters in alphabetical order,
# but the Elf fell asleep from consuming too much hot chocolate and candy
# canes! Can you help him out?

# Sort the Gift Code

# Write a function called sortGiftCode/sort_gift_code/SortGiftCode
# that accepts a string containing up to 26 unique alphabetical characters,
# and returns a string containing the same characters in alphabetical order.

# Examples (Input -- => Output):

# "abcdef"                      -- => "abcdef"
# "pqksuvy"                     -- => "kpqsuvy"
# "zyxwvutsrqponmlkjihgfedcba"  -- => "abcdefghijklmnopqrstuvwxyz"

# solution_1
def sort_gift_code(code):
    return ''.join(sorted(code))


# solution_2
import string
import itertools

def sort_code(code):
    alphabet = string.ascii_lowercase
    code = [char for char in code]

    for i, j in itertools.combinations(range(len(code)), 2):
        if alphabet.index(code[i]) > alphabet.index(code[j]):
            code[i], code[j] = code[j], code[i]
    
    return ''.join(code)


# tests
import unittest

class SortGiftBasicTests(unittest.TestCase):
    def test_sort_gift_code(self):
        self.assertEqual(sort_gift_code('abcdef'), 'abcdef');
        self.assertEqual(sort_gift_code('pqksuvy'), 'kpqsuvy');
        self.assertEqual(
            sort_gift_code('zyxwvutsrqponmlkjihgfedcba'),
              'abcdefghijklmnopqrstuvwxyz');

    def test_sort_code(self):
        self.assertEqual(sort_code('abcdef'), 'abcdef');
        self.assertEqual(sort_code('pqksuvy'), 'kpqsuvy');
        self.assertEqual(
            sort_code('zyxwvutsrqponmlkjihgfedcba'),
              'abcdefghijklmnopqrstuvwxyz');

if __name__ == '__main__':
    unittest.main()
