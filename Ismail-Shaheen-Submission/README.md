Caesar Encryption & Decryption Project
This project uses basic Caesar encryption and decryption functions in Python. It provides a way to encrypt and decrypt messages by shifting the letters of the alphabet by a given number of positions. The main goal of this project is to show the use of simple encryption/decryption algorithms and organize the code into modular files.

Project structure
The project is organized into two main directories:
src/: This folder contains the core implementation of the cipher. Specifically:
source.py: Has the encrypt and decrypt functions which implement the Caesar algorithm.
tests/: This folder contains the test cases to verify the correctness of the encrypt and decrypt functions.

encryption.py: This has the test cases for testing the encryption functionality.
decryption.py: This has the test cases for testing the decryption functionality.
How the Cipher Works
Encryption
The encrypt() function shifts each letter of the input message by a specified number of positions in the alphabet. By default, it uses a shift of 3. For example, the letter 'A' becomes 'D', and 'B' becomes 'E'. Non-letter characters are not allowed except for space

Decryption
The decrypt() function reverses the encryption process by shifting each letter in the opposite direction. If you encrypted a message with a shift of 3, you can decrypt it by shifting each letter back by 3 positions.

How to run the files
1. Running the Tests:
The tests are written to verify the correctness of the encryption and decryption functions. They are located in the tests/ folder.

Running the encryption test:
To test the encryption function, run the following command from the project root:

python tests/encryption.py
Running the Decryption Test:
To test the decryption function, run the following command from the project root:

python tests/decryption.py
2. Understanding the Test Files:
Test Encryption:
encryption.py runs tests to verify that the encryption function behaves as expected for various test cases, including different letter cases and shift values.
Test Decryption:
decryption.py runs tests to verify that the decryption function correctly reverses the encryption process for different inputs.
3. Code Execution Flow:
Both test files import the respective functions (encrypt or decrypt) from the source.py file in the src/ folder.
Each test case checks the output of the encryption or decryption function against the expected result. If the output doesn't match, the test will fail and display an error message.
Organization of Submission
This submission is organized into two main components:

Source Code (src/ folder):

The core cipher logic is implemented here.
The source.py file contains two functions: encrypt() and decrypt(). These functions are responsible for encrypting and decrypting text using a Caesar cipher algorithm.
Test Files (tests/ folder):

The encryption.py and decryption.py files contain test cases to validate the functionality of the cipher functions.
Tests check for various conditions, such as:
Different letter cases (upper, lower, mixed).
Handling of spaces in the message.
Correct decryption of previously encrypted text.
Example
1. Encryption Example:
For a simple message like hello, calling the encrypt() function will result in the following encrypted output:

encrypt("hello")
Output: "khoor"
2. Decryption Example:
Decrypting the previously encrypted message "khoor" using the decrypt() function will give:

decrypt("khoor")
Output: "hello"
Additional Notes
The default shift value for both encryption and decryption is 3. This can be adjusted by passing a shift argument to the functions.
Spaces are preserved in the output, ensuring the structure of the input message is maintained.