# Given an array (arr) as an argument complete the function countSmileys that should return the total number of smiling faces.

# Rules for a smiling face:
# Each smiley face must contain a valid pair of eyes. Eyes can be marked as : or ;
# A smiley face can have a nose but it does not have to. Valid characters for a nose are - or ~
# Every smiling face must have a smiling mouth that should be marked with either ) or D
# No additional characters are allowed except for those mentioned.

# Valid smiley face examples: :) :D ;-D :~)
# Invalid smiley faces:  ;( :> :} :]

# Example

# countSmileys([':)', ';(', ';}', ':-D']);       // should return 2;
# countSmileys([';D', ':-(', ':-)', ';~)']);     // should return 3;
# countSmileys([';]', ':[', ';*', ':$', ';-D']); // should return 1;
# Note

# In case of an empty array return 0. You will not be tested with invalid input (input will always be an array).
# Order of the face (eyes, nose, mouth) elements will always be the same.

# solution
import unittest

def count_smileys(arr):
    if not arr:
        return 0
    count = 0
    for smile in arr:
        if len(smile) == 2 and smile[0] in [':', ';'] and smile[1] in [')', 'D']:
            count += 1
        elif len(smile) == 3 and smile[0] in [':', ';'] and smile[1] in ['-', '~'] and smile[2] in [')', 'D']:
            count += 1
    return count


# tests
class TestPrime(unittest.TestCase):
   def test_case_1(self):
       self.assertEqual(count_smileys([]), 0)

   def test_case_2(self):
       self.assertTrue(count_smileys([':D',':~)',';~D',':)']), 4)

   def test_case_3(self):
       self.assertTrue(count_smileys([':)',':(',':D',':O',':;']), 2)

   def test_case_4(self):
       self.assertTrue(count_smileys([';]', ':[', ';*', ':$', ';-D']), 1)


if __name__ == '__main__':
    unittest.main()