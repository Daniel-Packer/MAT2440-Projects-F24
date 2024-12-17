# Caesar Cipher

## Description 
This is a generalized version of the Caesar Cipher, that uses the following ***f(p) = (p + k) mod 26*** to encrypt a message and ***f(p) = (p - k) mod 26*** to decrypt a message.

## Features
- **Encryption:** Encode plain text message by shifting letters based on a shift key.
- **Decryption:** Decode ciphertext by reversing the shift using the same shift key.
- **Shift:** User defined shift key for encoding and decoding.
- **The program only supports Upper and lower case letters, non-alphabetic characters (i.e. numbers, spaces and special characters) are handled by adding them back to the text unchanged.**
- **All outputs are presented as lowercase versions of its original text.**

## Example Code (Python)
Example Snippet of the Caesar Cipher in Python:
'''python
def encryption(plain_text, shift):
    cipher_text = ""
    for char in plain_text:
        if char in alphabet:
            position = alphabet.index(char)   # store the index of the character 
            new_position = (position + shift) % 26
            cipher_text += alphabet[new_position]
        else:
            cipher_text += char
    print(f"Encrypted text = {cipher_text}")

def decryption(cipher_text, shift):
    plain_text = ""
    for char in cipher_text:
        if char in alphabet:
            #print(char)
            position = alphabet.index(char)  
            new_position = (position - shift) % 26
            plain_text += alphabet[new_position]
        else:
            plain_text += char
    print(f"Decrypted text = {plain_text}")

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
'''

## Sample test script
'''python
def test_caesar_cipher():
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x','y', 'z']
    
    def encryption(plain_text, shift):
        plain_text = plain_text.lower()
        cipher_text = ""
        for char in plain_text:
            if char in alphabet:
                position = alphabet.index(char)  
                new_position = (position + shift) % 26
                cipher_text += alphabet[new_position]
            else:
                cipher_text += char
        
        return cipher_text

    def decryption(cipher_text, shift):
        plain_text = ""
        for char in cipher_text:
            if char in alphabet:
                position = alphabet.index(char)   # store the index of the character 
                new_position = (position - shift) % 26
                plain_text += alphabet[new_position]
            else:
                plain_text += char
        
        return plain_text
    
    # Test Cases
    assert encryption("Hello", 3) == "khoor"
    assert decryption("khoor", 3) == "hello"
    assert encryption("Hello Kwasi!", 4) == "lipps oaewm!"
    assert decryption("lipps oaewm!", 4) == "hello kwasi!"
    assert encryption("kw@si1234", 9) == "tf@br1234"
    assert decryption("tf@br1234", 9) == "kw@si1234"
    print("All test passed!!!")
    
# Run test
test_caesar_cipher()
'''


## Usage
###1. Clone Github Repo
'''bash
git clone https://github.com/Daniel-Packer/MAT2440-Projects-F24/Kwasi-James-submission
cd src
'''
###2. Run Program
'''bash
python caesar_cipher.py
'''
###3. Input and Output
When prompted:
1. Enter a message to encrypt or decrypt.
2. Enter a shift key (integer)
3. The program will output the encrypted or decrypted text.
4. Enter 'yes' continue running program or 'no' to exit program.

###4. Run Test Script
'''bash
cd tests
python test_caesar_cipher.py
'''

***Example Encryption**
'''
Input: Hello Kwasi!
Shift: 3
Output: khoor nzdvl!
'''
***Example Decryption**
'''
Input: khoor nzdvl!
Shift: 3
Output: hello kwasi!
'''

## Author
Kwasi James
Github: https://github.com/kwasijames



