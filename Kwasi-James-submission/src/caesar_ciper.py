alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x','y', 'z']

# Function Encrypt text
def encryption(plain_text, shift):
    cipher_text = ""
    for char in plain_text:
        if char in alphabet:
            position = alphabet.index(char)  
            new_position = (position + shift) % 26
            cipher_text += alphabet[new_position]
        else:
            cipher_text += char
    print(f"Encrypted text = {cipher_text}")

# Function Decrypt text
def decryption(cipher_text, shift):
    plain_text = ""
    for char in cipher_text:
        if char in alphabet:
            #print(char)
            position = alphabet.index(char)   # store the index of the character 
            new_position = (position - shift) % 26
            plain_text += alphabet[new_position]
        else:
            plain_text += char
    print(f"Decrypted text = {plain_text}")

# Run the program until user prompt to exit

exit_program = False

while not exit_program:
    usr_choice = input("Type 'encrypt' to encrypt a message and 'decrypt' to decrypt a message: ").lower()
    text = input("Type your message: \n").lower()
    shift = int(input("Enter secreat shift key: \n"))
    if usr_choice == "encrypt":
        encryption(plain_text=text, shift=shift)
    elif usr_choice == "decrypt":
        decryption(cipher_text=text, shift=shift)
    play_again = input("Type 'yes' to continue or 'no' to exit: \n").lower()
    if play_again == 'no':
        exit_program = True
        print("Program terminated. Thank you...")
