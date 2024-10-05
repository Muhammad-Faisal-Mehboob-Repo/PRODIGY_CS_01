# Caesar Cipher Program

Welcome to the **Caesar Cipher Program**! This Python project implements a simple yet powerful encryption and decryption algorithm using the Caesar Cipher technique.

## About the Program

The **Caesar Cipher** is one of the most well-known encryption techniques. It shifts each letter of the message by a specified number of positions in the alphabet. This project allows you to both encrypt and decrypt messages using a user-defined shift value.

### Features:
- Encrypts any text message by shifting its characters.
- Decrypts any text that was previously encrypted with a Caesar Cipher.
- Handles both uppercase and lowercase letters.
- Non-alphabetic characters (like punctuation, numbers, etc.) remain unchanged.

## How It Works

1. **Encryption**: The program takes a message and a shift value as input. It then shifts each letter in the message by the shift value and returns the encrypted text.

2. **Decryption**: You can also decrypt an encrypted message by using the same shift value used during encryption. The program will reverse the shift to give you the original message back.

## How to Use

1. **Clone the repository** to your local machine:

    ```bash
    git clone https://github.com/your-username/caesar-cipher-program.git
    ```

2. **Run the Program**:

    Open your terminal or command prompt and run the program using Python:

    ```bash
    python caesar_cipher.py
    ```

3. **Follow the prompts**:

    - Enter the message you want to encrypt or decrypt.
    - Provide a shift value (any integer).
    - Choose whether you want to encrypt or decrypt the message by pressing `y` for encryption or `n` for decryption.

4. **Example**:

    ```bash
    Enter the message: Hello World!
    Enter the shift value: 3
    If you want to encrypt the message, press 'y'. Otherwise, press 'n' to decrypt the message. (y/n): y
    Encrypted message: Khoor Zruog!
    ```

## Code Breakdown

- **encrypt(text, shift)**: This function encrypts the given text by shifting each letter by the shift value.
  
- **decrypt(text, shift)**: This function reverses the shift, effectively decrypting the encrypted text.
  
- **caesar_cipher_choice()**: This function handles the user input and provides the choice between encryption and decryption.

## Improvements

This project is just a basic implementation of the Caesar Cipher. You can improve or extend it in several ways:
- Add support for encrypting/decrypting files.
- Allow for custom handling of numbers and symbols.
- Implement additional cipher techniques (e.g., Vigenère cipher, substitution cipher).

## Contributing

Feel free to contribute to this project by submitting issues or making pull requests. Let’s improve this together!

## License

This project is licensed under the MIT License.

---

Happy Encrypting!
