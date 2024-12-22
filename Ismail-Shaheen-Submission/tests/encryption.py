
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from source import encrypt


def test_encrypt_lowercase():
    result = encrypt("hello")
    print(f"Encrypt 'hello' -> {result}")
    assert result == "khoor", f"Expected 'khoor', but got {result}"

def test_encrypt_uppercase():
    result = encrypt("HELLO")
    print(f"Encrypt 'HELLO' -> {result}")
    assert result == "KHOOR", f"Expected 'KHOOR', but got {result}"

def test_encrypt_mixed_case():
    result = encrypt("Hello")
    print(f"Encrypt 'Hello' -> {result}")
    assert result == "Khoor", f"Expected 'Khoor', but got {result}"

def test_encrypt_with_shift():
    result = encrypt("hello", shift=5)
    print(f"Encrypt 'hello' with shift 5 -> {result}")
    assert result == "mjqqt", f"Expected 'mjqqt', but got {result}"

def test_encrypt_with_space():
    result = encrypt("hello world")
    print(f"Encrypt 'hello world' -> {result}")
    assert result == "khoor zruog", f"Expected 'khoor zruog', but got {result}"

if __name__ == "__main__":
    test_encrypt_lowercase()
    test_encrypt_uppercase()
    test_encrypt_mixed_case()
    test_encrypt_with_shift()
    test_encrypt_with_space()
