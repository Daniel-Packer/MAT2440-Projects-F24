#include <iostream>
#include <string>
#include <cctype>  


const char alphabet_upper[] = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
const char alphabet_lower[] = "abcdefghijklmnopqrstuvwxyz";


std::string encrypt(const std::string& word, int shift = 3) {
    std::string final = "";

    for (char letter : word) {
        if (letter == ' ') {
            final += ' ';
            continue;
        }

        bool is_lower = std::islower(letter);

       
        char base_letter = is_lower ? std::tolower(letter) : letter;

      
        int index = base_letter - (is_lower ? 'a' : 'A');

       
        int encrypted_index = (index + shift) % 26;

      
        char encrypted_letter = (is_lower ? alphabet_lower : alphabet_upper)[encrypted_index];

        final += encrypted_letter;
    }

    return final;
}


std::string decrypt(const std::string& word, int shift = 3) {
    std::string final = "";

    for (char letter : word) {
        if (letter == ' ') {
            final += ' ';
            continue;
        }

        bool is_lower = std::islower(letter);

       
        char base_letter = is_lower ? std::tolower(letter) : letter;

       
        int index = base_letter - (is_lower ? 'a' : 'A');

        
        int decrypted_index = (index - shift + 26) % 26;

       
        char decrypted_letter = (is_lower ? alphabet_lower : alphabet_upper)[decrypted_index];

        final += decrypted_letter;
    }

    return final;
}

int main() {
    std::string original_message = "Hello my name is Yousif";

   
    std::string encrypted_message = encrypt(original_message);

   
    std::string decrypted_message = decrypt(encrypted_message);

  
    std::cout << "Encrypted: " << encrypted_message << std::endl;
    std::cout << "Decrypted: " << decrypted_message << std::endl;

    return 0;
}