def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            encrypted_text += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted_text += char
    
    return encrypted_text

def decrypt(text, shift):
    decrypt_text = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            decrypt_text += chr((ord(char) - shift_base - shift) % 26 + shift_base)  # Fixed decryption logic
        else:
            decrypt_text += char
    return decrypt_text

def caesar_cipher_choice():
    message = input("Enter the message: ")
    shift = int(input("Enter the shift value: "))
    choice = input("If you want to encrypt the message, press 'y'. Otherwise, press 'n' to decrypt the message. (y/n): ").lower()

    if choice == 'y':
        encrypted_message = encrypt(message, shift)
        print(f"Encrypted message: {encrypted_message}")
    elif choice == 'n':
        decrypted_message = decrypt(message, shift)
        print(f"Decrypted message: {decrypted_message}")
    else:
        print("Invalid choice! Please enter 'y' for encryption and 'n' for decryption of a message.")

if __name__ == "__main__":
    caesar_cipher_choice()
