from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes

def load_public_key(pem_path):
    with open(pem_path, "rb") as key_file:
        public_key = serialization.load_pem_public_key(
            key_file.read(),
            backend=default_backend()
        )
    return public_key

# Function to load private key from PEM file
def load_private_key(pem_path):
    with open(pem_path, "rb") as key_file:
        private_key = serialization.load_pem_private_key(
            key_file.read(),
            password=None,
            backend=default_backend()
        )
    return private_key

# Function to encrypt a message using the public key
def encrypt_message(public_key, message):
    encrypted = public_key.encrypt(
        message.encode(),  # Convert message to bytes
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return encrypted

# Function to decrypt a message using the private key
def decrypt_message(private_key, encrypted_message):
    decrypted = private_key.decrypt(
        encrypted_message,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return decrypted.decode()  # Convert bytes back to string

# Save the keys to files
def save_key_to_file(key, filename):
    with open(filename, 'wb') as key_file:
        key_file.write(key)

if __name__ == "__main__":
    public_key = load_public_key("public_key.pem")
    private_key = load_private_key("private_key.pem")

    # Message to be encrypted
    original_message = "This is a secret message!"

    # Encrypt the message using the public key
    encrypted_message = encrypt_message(public_key, original_message)
    print("Encrypted message:", encrypted_message)

    # Decrypt the message using the private key
    decrypted_message = decrypt_message(private_key, encrypted_message)
    print("Decrypted message:", decrypted_message)