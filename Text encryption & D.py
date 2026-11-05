
import os
from cryptography.fernet import Fernet

# Generate or load secret key
if os.path.exists("key.key"):
    key = open("key.key", "rb").read()
else:
    key = Fernet.generate_key()
    with open("key.key", "wb") as file:
        file.write(key)

f = Fernet(key)

# Caesar Cipher
def caesar(text, shift):
    result = ""
    for c in text:
        if 'A' <= c <= 'Z':
            result += chr((ord(c)-65+shift) % 26+65)
        elif 'a' <= c <= 'z':
            result += chr((ord(c)-97+shift) % 26+97)
        else:
            result += c
    return result

print("\nTEXT ENCRYPTION & DECRYPTION TOOL")
print("1. Caesar Cipher")
print("2. Fernet Encryption")

choice = input("Choose method: ")
msg = input("Enter text: ")

if choice == "1":
    shift = int(input("Enter shift (0-25): "))
    if 0 <= shift <= 25:
        enc = caesar(msg, shift)
        print("Encrypted:", enc)
        print("Decrypted:", caesar(enc, -shift))
    else:
        print("Invalid shift!")

elif choice == "2":
    enc = f.encrypt(msg.encode())
    print("Encrypted:", enc.decode())
    print("Decrypted:", f.decrypt(enc).decode())

    with open("encrypted.txt", "w") as file:
        file.write(enc.decode())

    print("Saved in encrypted.txt")

else:
    print("Invalid choice!")
