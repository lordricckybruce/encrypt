#!/bin/python3
from cryptography.fernet import Fernet
#Fernet is used for general encryption tasks and provides authenticated encryption
# Generate a key
key = Fernet.generate_key()  #generates a secure key for encryption and decryption
cipher_suite = Fernet(key)   #for creating a cipher object that encrypt and decrypt

# Encrypt a message
plaintext = b"This is a secret message"
ciphertext = cipher_suite.encrypt(plaintext)   #produces ciphertext
print(f"Ciphertext: {ciphertext}")

# Decrypt the message
decrypted_message = cipher_suite.decrypt(ciphertext)   #for decrypting
print(f"Decrypted Message: {decrypted_message}")


from cryptography.fernet import Fernet    
key = Fernet.generate_key()
cipher_suite = Fernet(key)
plaintext = b'Learning this !!!'
ciphertext = cipher_suite.encrypt(plaintext)
print(f'Encrypt: {ciphertext}')
decrypted_code = cipher_suite.decrypt(ciphertext)
print(f'Decrypt: {decrypted_code}')
