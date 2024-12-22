def caesar_cipher(text, key, decrypt=False):
    # Adjusting the key to decide if you want to decrypt or encrypt
    if decrypt:
        key = -key

    result = []
    for char in text:
        if char.isalpha():  # Checking if the key entered is a letter
            shift = 65 if char.isupper() else 97  # Making sure the letter that was entered is either lower/upper case
            # Shifting the input to ecnrypt or decrypt
            new_char = chr((ord(char) - shift + key) % 26 + shift)
            result.append(new_char)
        else:
            result.append(char)

    return ''.join(result)

#Enter the word you want to decipher or encrypt
word = input("Enter the word of your choice: ")

key = int(input("Enter the key (integer): "))

action = input("Would you like to encrypt or decrypt? (e/d): ").lower()

# Decide if you want to encrypt or decrypt the word of your choice
if action == 'e':
    print(f"Encrypted word: {caesar_cipher(word, key)}")

elif action == 'd':
    print(f"Decrypted word: {caesar_cipher(word, key, decrypt=True)}")

else:
    print("ERROR! Please enter 'e' for Encryption or 'd' for Decryption.")
