
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
