#vigenere cipher
def vigenere_cipher(text, key_stream, encrypting):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if encrypting:
            result += chr((ord(char) - 97 + ord(key_stream[i]) - 97) % 26 + 97)
        else:
            result += chr((ord(char) - ord(key_stream[i]) + 26) % 26 + 97)
    return result


if __name__ == "__main__":
    key = input("Enter Key: ").replace(" ", "").lower()
    plaintext = input("Enter Plaintext: ").replace(" ", "").lower()

    key_stream = "".join(key[i % len(key)] for i in range(len(plaintext)))

    ciphertext = vigenere_cipher(plaintext, key_stream, True)
    print("Ciphertext: ", ciphertext)

    decrypted_text = vigenere_cipher(ciphertext, key_stream, False)
    print("Decrypted Text: ", decrypted_text)
