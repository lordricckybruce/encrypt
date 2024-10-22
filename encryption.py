
#using advanced AES 
#!/usr/bin/env python3
#symmetric encryption needs only one key
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes  #cipher,algorithms, modes used for configuring the AES cipher
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC #used to derive a cryptographic key
from cryptography.hazmat.backends import default_backend #for cryptographic operations
from cryptography.hazmat.primitives import hashes #used to specify hash algorithms
from cryptography.hazmat.primitives import padding #adding and removing padding to ensure data fits
import os #used to generate random data
import base64 #used to encode binary data into text for transmission and storage

class SymmetricEncryption:  #customs python class for symmetric encrypt and decrypt
    def __init__(self, password):   #a consturctor which runs when obj are created
        # Deriving a key from the password
        self.backend = default_backend()   #specifies backend use
        self.salt = os.urandom(16)  # A random salt, salt is a random 16byte added to the password during key derivation to make it more secure and resistant to brute_force attack
        self.iterations = 100000  # Iterations for key derivation to slow down brute_forc e attack
        self.key = self.derive_key(password) #method to derive encryption key from password and salt
    
    def derive_key(self, password):
        # Key derivation using PBKDF2 HMAC with SHA256
        kdf = PBKDF2HMAC(  #produces the cryptographic key
            algorithm=hashes.SHA256(), #an hashing algorithms during key derivation
            length=32,  # AES key size: 32 bytes for AES-256
            salt=self.salt, #salt ensures two users use the same password
            iterations=self.iterations,  #more iteration amke it harder to brute force
            backend=self.backend   #specifies which backend to use
        )
        return kdf.derive(password.encode())  # Returns the derived key

    def encrypt(self, plaintext):
        iv = os.urandom(16)  # Random IV (Initialization Vector)
        cipher = Cipher(algorithms.AES(self.key), modes.CBC(iv), backend=self.backend)
        encryptor = cipher.encryptor()

        # Padding plaintext to match block size
        padder = padding.PKCS7(algorithms.AES.block_size).padder()
        padded_data = padder.update(plaintext.encode()) + padder.finalize()

        ciphertext = encryptor.update(padded_data) + encryptor.finalize()

        # Encode the ciphertext and IV to be stored/transmitted easily
        return base64.b64encode(iv + ciphertext).decode('utf-8')

    def decrypt(self, ciphertext):
        # Decode the base64 encoded ciphertext
        data = base64.b64decode(ciphertext)
        iv = data[:16]  # Extract IV
        actual_ciphertext = data[16:]  # Extract the actual ciphertext

        cipher = Cipher(algorithms.AES(self.key), modes.CBC(iv), backend=self.backend)
        decryptor = cipher.decryptor()

        # Decrypt and unpad the plaintext
        padded_plaintext = decryptor.update(actual_ciphertext) + decryptor.finalize()

        unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
        plaintext = unpadder.update(padded_plaintext) + unpadder.finalize()

        return plaintext.decode('utf-8')

# Example Usage
password = 'strongpassword'
encryption_obj = SymmetricEncryption(password)

# Encrypt a message
plaintext = 'This is a secret message'
ciphertext = encryption_obj.encrypt(plaintext)
print(f'Ciphertext: {ciphertext}')

# Decrypt the message
decrypted_message = encryption_obj.decrypt(ciphertext)
print(f'Decrypted Message: {decrypted_message}')

