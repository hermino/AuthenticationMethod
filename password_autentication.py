import hashlib


def hash_password(password: str):
    """Hash password

    :param password: password to generate hash
    :return: password hashble
    """
    return hashlib.sha256(password.encode()).hexdigest()

def authenticate_password(stored_password_hash: str, provided_password: str):
    """Authenticate password

    :param stored_password_hash: _description_
    :param provided_password: _description_
    """
    return stored_password_hash == hash_password(provided_password)


stored_password_hash = hash_password("password")
print(authenticate_password(stored_password_hash, "password"))