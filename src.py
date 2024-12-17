def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isupper():  # Uppercase letters
            result += chr((ord(char) - 65 + shift) % 26 + 65)
        elif char.islower():  # Lowercase letters
            result += chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            result += char  # Leave non-alphabetic characters unchanged
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)  # Use the same function for decryption

# Example usage
message = input("Enter your message: ")
shift = int(input("Enter shift value (number): "))

encrypted = encrypt(message, shift)
print("Encrypted Message:", encrypted)

decrypted = decrypt(encrypted, shift)
print("Decrypted Message:", decrypted)
