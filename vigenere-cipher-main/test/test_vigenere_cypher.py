import unittest
from cypher import vigenere_cipher

class TestVigenereCipher(unittest.TestCase):
    def test_basic_encryption(self):
        text = "hello"
        key_stream = "abcde"
        result = vigenere_cipher(text, key_stream, encrypting=True)
        self.assertEqual(result, "hfnos")

    def test_basic_decryption(self):
        ciphertext = "hfnos"
        key_stream = "abcde"
        result = vigenere_cipher(ciphertext, key_stream, encrypting=False)
        self.assertEqual(result, "hello")

    def test_empty_input(self):
        text = ""
        key_stream = ""
        result = vigenere_cipher(text, key_stream, encrypting=True)
        self.assertEqual(result, "")

    def test_repeated_key(self):
        text = "helloworld"
        key = "abc"
        key_stream = "".join(key[i % len(key)] for i in range(len(text)))
        result = vigenere_cipher(text, key_stream, encrypting=True)
        decrypted = vigenere_cipher(result, key_stream, encrypting=False)
        self.assertEqual(decrypted, text)

    def test_case_insensitivity(self):
        text = "HeLLo"
        key_stream = "abcde"
        result = vigenere_cipher(text.lower(), key_stream, encrypting=True)
        self.assertEqual(result, "hfnos")

if __name__ == "__main__":
    unittest.main()

