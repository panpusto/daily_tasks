# Given a variable n,
# If n is an integer, Return a string with dash'-'marks before and after each 
# odd integer, but do not begin or end the string with a dash mark. If n is
# negative, then the negative sign should be removed.

# If n is not an integer, return the string "None".

# Ex:
# dashatize(274) -> '2-7-4'
# dashatize(6815) -> '68-1-5'

# solution
def dashatize(n):
    if type(n) is not int:
        return 'None'

    nums = list(str(abs(n)))
    result = []

    for num in nums:
        if int(num) % 2 == 0:
            result.append(num)
        else:
            if result and result[-1] != '-':
                result.append('-')
            result.append(num)
            result.append('-')

    if result and result[-1] == '-':
        result.pop()

    return ''.join(result) 
       
# solution 2
def dashatize_oneliner(n):
    try:
        return ''.join([i if int(i) % 2 == 0 else f'-{i}-' for i in list(str(abs(n)))]) \
            .replace('--', '-').strip('-')

    except:
        return 'None'

# tests
import unittest

class DashatizeBasicTests(unittest.TestCase):
    def test_dashatize_func(self):
        self.assertEqual(dashatize(274),"2-7-4")
        self.assertEqual(dashatize(5311),"5-3-1-1")
        self.assertEqual(dashatize(86320),"86-3-20")
        self.assertEqual(dashatize(974302),"9-7-4-3-02")
    
    def test_dashatize_oneliner(self):
        self.assertEqual(dashatize_oneliner(274),"2-7-4")
        self.assertEqual(dashatize_oneliner(5311),"5-3-1-1")
        self.assertEqual(dashatize_oneliner(86320),"86-3-20")
        self.assertEqual(dashatize_oneliner(974302),"9-7-4-3-02")


if __name__ == '__main__':
    unittest.main()
