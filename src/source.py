
letters = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19, 'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25}

numbers = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J', 10: 'K', 11: 'L', 12: 'M', 13: 'N', 14: 'O', 15: 'P', 16: 'Q', 17: 'R', 18: 'S', 19: 'T', 20: 'U', 21: 'V', 22: 'W', 23: 'X', 24: 'Y', 25: 'Z'}

def encrypt(word, shift=3):
    final = ""
    for letter in word:
        if letter == " ":
            final += " "
            continue
        
        encrypted_index = (letters[letter.upper()] + shift) % 26
        encrypted_letter = numbers[encrypted_index]
        
        if letter.islower():
            final += encrypted_letter.lower()
        else:
            final += encrypted_letter 
    
    return final.strip()
def decrypt(word, shift=3):
    final = ""
    for letter in word:
        if letter == " ":
            final += " "
            continue
        
        decrypted_index = (letters[letter.upper()] - shift) % 26
        decrypted_letter = numbers[decrypted_index]
        
        if letter.islower():
            final += decrypted_letter.lower()
        else:
            final += decrypted_letter
    
    return final.strip()


encrypted_message = encrypt("Hello my name is ismail")
decrypted_message = decrypt(encrypted_message)


