import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from source import decrypt

def test_decrypt_lowercase():
    result = decrypt("khoor")
    print(f"Decrypt 'khoor' -> {result}")
    assert result == "hello", f"Expected 'hello', but got {result}"

def test_decrypt_uppercase():
    result = decrypt("KHOOR")
    print(f"Decrypt 'KHOOR' -> {result}")
    assert result == "HELLO", f"Expected 'HELLO', but got {result}"

def test_decrypt_mixed_case():
    result = decrypt("Khoor")
    print(f"Decrypt 'Khoor' -> {result}")
    assert result == "Hello", f"Expected 'Hello', but got {result}"

def test_decrypt_with_shift():
    result = decrypt("mjqqt", shift=5)
    print(f"Decrypt 'mjqqt' with shift 5 -> {result}")
    assert result == "hello", f"Expected 'hello', but got {result}"

def test_decrypt_with_space():
    result = decrypt("khoor zruog")
    print(f"Decrypt 'khoor zruog' -> {result}")
    assert result == "hello world", f"Expected 'hello world', but got {result}"

if __name__ == "__main__":
    test_decrypt_lowercase()
    test_decrypt_uppercase()
    test_decrypt_mixed_case()
    test_decrypt_with_shift()
    test_decrypt_with_space()
