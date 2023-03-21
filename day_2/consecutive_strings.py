# You are given an array(list) strarr of strings and an integer k. Your task is to return
# the first longest string consisting of k consecutive strings taken in the array.
# Examples:

# strarr = ["tree", "foling", "trashy", "blue", "abcdef", "uvwxyz"], k = 2

# Concatenate the consecutive strings of strarr by 2, we get:

# treefoling   (length 10)  concatenation of strarr[0] and strarr[1]
# folingtrashy ("      12)  concatenation of strarr[1] and strarr[2]
# trashyblue   ("      10)  concatenation of strarr[2] and strarr[3]
# blueabcdef   ("      10)  concatenation of strarr[3] and strarr[4]
# abcdefuvwxyz ("      12)  concatenation of strarr[4] and strarr[5]

# Two strings are the longest: "folingtrashy" and "abcdefuvwxyz".
# The first that came is "folingtrashy" so 
# longest_consec(strarr, 2) should return "folingtrashy".

# In the same way:
# longest_consec(["zone", "abigail", "theta", "form", "libe", "zas", "theta", "abigail"], 2) --> "abigailtheta"
# n being the length of the string array, if n = 0 or k > n or k <= 0 return "" (return Nothing in Elm, "nothing" in Erlang).

# Note
# consecutive strings : follow one after another without an interruption


# solution
import unittest

def longest_consec(strarr, k):
    n = len(strarr)
    if n == 0 or k > n or k <= 0:
        return ''
    
    result = ''
    for i in range(n - k + 1):
        s = ''.join(strarr[i: i + k])
        if len(s) > len(result):
            result = s
    return result        


# tests
class TestLongestConsec(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], 2), "abigailtheta")
    
    def test_case_2(self):
        self.assertEqual(longest_consec(["ejjjjmmtthh", "zxxuueeg", "aanlljrrrxx", "dqqqaaabbb", "oocccffuucccjjjkkkjyyyeehh"], 1), "oocccffuucccjjjkkkjyyyeehh")
    
    def test_case_3(self):
        self.assertEqual(longest_consec([], 3), "")
    
    def test_case_4(self):
        self.assertEqual(longest_consec(["itvayloxrp","wkppqsztdkmvcuwvereiupccauycnjutlv","vweqilsfytihvrzlaodfixoyxvyuyvgpck"], 2), "wkppqsztdkmvcuwvereiupccauycnjutlvvweqilsfytihvrzlaodfixoyxvyuyvgpck")
    
    def test_case_5(self):
        self.assertEqual(longest_consec(["wlwsasphmxx","owiaxujylentrklctozmymu","wpgozvxxiu"], 2), "wlwsasphmxxowiaxujylentrklctozmymu")
    
    def test_case_6(self):
        self.assertEqual(longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], -2), "")
    
    def test_case_7(self):
        self.assertEqual(longest_consec(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 3), "ixoyx3452zzzzzzzzzzzz")
    
    def test_case_8(self):
        self.assertEqual(longest_consec(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 15), "")
    
    def test_case_9(self):
        self.assertEqual(longest_consec(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 0), "")
    

if __name__ == '__main__':
    unittest.main()
