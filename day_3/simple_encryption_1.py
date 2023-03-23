# Implement a pseudo-encryption algorithm which given a string S and an integer N concatenates 
# all the odd-indexed characters of S with all the even-indexed characters of S, 
# this process should be repeated N times.

# Examples:
# encrypt("012345", 1)  =>  "135024"
# encrypt("012345", 2)  =>  "135024"  ->  "304152"
# encrypt("012345", 3)  =>  "135024"  ->  "304152"  ->  "012345"

# encrypt("01234", 1)  =>  "13024"
# encrypt("01234", 2)  =>  "13024"  ->  "32104"
# encrypt("01234", 3)  =>  "13024"  ->  "32104"  ->  "20314"
# Together with the encryption function, you should also implement a decryption function which reverses the process.

# If the string S is an empty value or the integer N is not positive, return the first argument without changes.


# solution
import unittest

def decrypt(encrypted_text, n):
    if n <= 0:
        return encrypted_text
    splitted_text = list(encrypted_text)
    length = len(splitted_text)
    if length % 2 == 0:
        split_idx = length // 2
    else:
        split_idx = (length - 1) // 2
    text_1 = splitted_text[0:split_idx]
    text_2 = splitted_text[split_idx:]
    result = ''.join([text_2[i//2] if i % 2 == 0 else text_1[(i - 1) // 2] for i in range(length)])
    return decrypt(result, n - 1)


def encrypt(text, n):
    if not text or n <= 0:
        return text
    encrypted_text = text[1::2] + text[::2]
    result = ''.join(encrypted_text)
    return encrypt(result, n - 1)


# tests
class TestSimpleEncryption(unittest.TestCase):
    def test_encrypt_func(self):
        self.assertEqual(encrypt("This is a test!", 0), "This is a test!")
        self.assertEqual(encrypt("This is a test!", 1), "hsi  etTi sats!")
        self.assertEqual(encrypt("This is a test!", 2), "s eT ashi tist!")
        self.assertEqual(encrypt("This is a test!", 3), " Tah itse sits!")
        self.assertEqual(encrypt("This is a test!", 4), "This is a test!")
        self.assertEqual(encrypt("This is a test!", -1), "This is a test!")
        self.assertEqual(encrypt("This kata is very interesting!", 1), "hskt svr neetn!Ti aai eyitrsig")
        self.assertEqual(encrypt("", 0), "")
        self.assertEqual(encrypt(None, 0), None)
    
    def test_decrypt_func(self):
        self.assertEqual(decrypt("This is a test!", 0), "This is a test!")
        self.assertEqual(decrypt("hsi  etTi sats!", 1), "This is a test!")
        self.assertEqual(decrypt("s eT ashi tist!", 2), "This is a test!")
        self.assertEqual(decrypt(" Tah itse sits!", 3), "This is a test!")
        self.assertEqual(decrypt("This is a test!", 4), "This is a test!")
        self.assertEqual(decrypt("This is a test!", -1), "This is a test!")
        self.assertEqual(decrypt("hskt svr neetn!Ti aai eyitrsig", 1), "This kata is very interesting!")
        self.assertEqual(decrypt("", 0), "")
        self.assertEqual(decrypt(None, 0), None)


if __name__ == '__main__':
    unittest.main()