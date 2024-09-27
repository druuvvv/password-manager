import os
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend

# Function to check if a PEM file contains a private key and return it
def check_private_key(pem_file):
    try:
        with open(pem_file, "rb") as key_file:
            key_data = key_file.read()

            # Attempt to load the private key
            private_key = serialization.load_pem_private_key(
                key_data,
                password=None,
                backend=default_backend()
            )
            return private_key  # Return the private key object
    except ValueError:
        return None  # Return None if not a private key
    except Exception as e:
        raise Exception(f"Error reading private key from file '{pem_file}': {e}")

# Function to check if a PEM file contains a public key and return it
def check_public_key(pem_file):
    try:
        with open(pem_file, "rb") as key_file:
            key_data = key_file.read()

            # Attempt to load the public key
            public_key = serialization.load_pem_public_key(
                key_data,
                backend=default_backend()
            )
            return public_key  # Return the public key object
    except ValueError:
        return None  # Return None if not a public key
    except Exception as e:
        raise Exception(f"Error reading public key from file '{pem_file}': {e}")

# Function to get all .pem files in the directory
def find_pem_files(directory):
    return [f for f in os.listdir(directory) if f.endswith('.pem')]

# Function to load keys from the directory and ensure there is exactly one private and one public key
def load_keys(directory):
    pem_files = find_pem_files(directory)
    private_key = None
    public_key = None

    for pem_file in pem_files:
        full_path = os.path.join(directory, pem_file)

        # Check if the file contains a private key
        if check_private_key(full_path):
            if private_key is not None:
                raise Exception(f"Multiple private keys found! Already found in another file before '{pem_file}'")
            private_key = check_private_key(full_path)

        # Check if the file contains a public key
        if check_public_key(full_path):
            if public_key is not None:
                raise Exception(f"Multiple public keys found! Already found in another file before '{pem_file}'")
            public_key = check_public_key(full_path)

    # Raise errors if no keys or multiple keys are found
    if private_key is None:
        raise Exception("No private key found in the directory.")
    if public_key is None:
        raise Exception("No public key found in the directory.")

    return private_key, public_key

def findKeys():
    try:
        directory = "."  # Current directory or specify the path
        private_key, public_key = load_keys(directory)
        print("Private key and public key successfully loaded.")
    except Exception as e:
        print(f"Error: {e}")

findKeys()