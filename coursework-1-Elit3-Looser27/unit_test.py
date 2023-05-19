import unittest
import encrypt
import decrypt
class TestMyCode():
    def test_mycode_enc(self):
        self.assertEqual(encrypt.encrypt("Hell0 w0rld :)", "!TWp\ "),"iZd}-Al($i&t2:", "it is not correct")

    def test_mycode_dec(self):
        self.assertEqual(decrypt.decrypt("iZd}-Al($i&t2:", "!TWp\ "),"Hell0 w0rld :)", "it is not correct")

if __name__ == "__main__":
    unittest.main()
