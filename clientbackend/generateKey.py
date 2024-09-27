from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

# Function to generate RSA key pair
def generate_rsa_key_pair():
    # Generate private key
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )

    # Generate private key in PEM format
    private_key_pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.NoEncryption()
    )

    # Generate public key
    public_key = private_key.public_key()

    # Generate public key in PEM format
    public_key_pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )

    return private_key_pem, public_key_pem


# Save the keys to files
def save_key_to_file(key, filename):
    with open(filename, 'wb') as key_file:
        key_file.write(key)

def generate_keys():
    private_key_pem, public_key_pem = generate_rsa_key_pair()

    # Save the private and public keys to files
    save_key_to_file(private_key_pem, "private_key.pem")
    save_key_to_file(public_key_pem, "public_key.pem")

    print("RSA key pair generated and saved to 'private_key.pem' and 'public_key.pem'.")

export = {generate_keys}