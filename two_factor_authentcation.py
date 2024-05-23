import pyotp


def generate_otp_secret() -> str:
    """_summary_

    :return: _description_
    """
    return pyotp.random_base32()

def get_otp(secret: str) -> str:
    """_summary_

    :param secret: _description_
    """
    totp = pyotp.TOTP(secret)
    return totp.now()


def verify_otp(secret: str, otp: str) -> bool:
    """_summary_

    :param secret: _description_
    :param otp: _description_
    :return: _description_
    """
    totp = pyotp.TOTP(secret)
    return totp.verify(otp)

secret = generate_otp_secret()
otp = get_otp(secret)
print(verify_otp(secret, otp))