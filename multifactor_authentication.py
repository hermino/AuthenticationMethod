from password_autentication import hash_password, authenticate_password
from two_factor_authentcation import generate_otp_secret, get_otp, verify_otp


def autheticate_mfa(stored_password_hash: str, provided_password: str, secret: str, otp: str) -> True:
    """_summary_

    :param stored_password_hash: _description_
    :param provided: _description_
    :param secret: _description_
    :param otp: _description_
    :return: _description_
    """
    return authenticate_password(stored_password_hash, provided_password) and verify_otp(secret, otp)


stored_password_hash = hash_password("password")
secret = generate_otp_secret()
otp = get_otp(secret)

print(autheticate_mfa(stored_password_hash, "password", secret, otp))