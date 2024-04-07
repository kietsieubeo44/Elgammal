from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.backends import default_backend

def generate_keys():
    parameters = dh.generate_parameters(generator=2, key_size=512, backend=default_backend())
    private_key = parameters.generate_private_key()
    public_key = private_key.public_key()
    return public_key, private_key

def encrypt(message, public_key):
    shared_key = public_key.generate_private_key().exchange(public_key)
    return shared_key

def decrypt(encrypted_message, private_key):
    shared_key = private_key.exchange(encrypted_message)
    return shared_key
