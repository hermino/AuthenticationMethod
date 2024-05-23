from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa, padding


def generate_keys():
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    public_key = private_key.public_key()
    
    return private_key, public_key


def authenticate_device(puplic_key, challenge, signature):
    try:
        puplic_key.verify(signature, challenge, padding.PKCS1v15(), hashes.SHA256())
        return True
    except:
        return False


private_key, public_key = generate_keys()
challenge = b"Authentication"
signature = private_key.sign(challenge, padding.PKCS1v15(), hashes.SHA256())
print(authenticate_device(public_key, challenge, signature))
    