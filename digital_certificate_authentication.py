from OpenSSL import crypto


def verify_certificate(cert_file: str, trusted_cert_file: str) -> bool:
    """_summary_

    :param cert_file: _description_
    :param trusted_cert_file: _description_
    :return: _description_
    """
    cert = crypto.load_certificate(crypto.FILETYPE_PEM, open(cert_file).read())
    trusted_cert = crypto.load_certificate(crypto.FILETYPE_PEM, open(trusted_cert).read())
    
    store - crypto.X509Store()
    store.add_cert(trusted_cert)
    store_context = crypto.X509StoreContext(store, cert)
    
    try:
        store_context.verify_certificate()
        return True
    except crypto.X509StoreContextError:
        return False
    
print(verify_certificate('user_cert.pem', 'trusted_cert.pem'))