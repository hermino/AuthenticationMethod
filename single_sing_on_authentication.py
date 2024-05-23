from requests_oauthlib import OAuth2Session


def get_google_provider_cfg():
    """_summary_
    """
    return requests.get("https://accounts.google.com/.well-known/openid-configuration").json()


def authenticate_google(client_id, client_secret, redirect_uri):
    """_summary_

    :param client_id: _description_
    :param client_secret: _description_
    :param redirect_uri: _description_
    """
    google_cfg = get_google_provider_cfg()
    authenticate_endpoint = google_cfg.get("authorization_endpoint")
    token_endpoint = google_cfg.get("token_endpoint")
    
    google = OAuth2Session(client_id, redirect_uri, scope=["openid", "email", "profile"])
    authorization_url, state = google.authorization_url(authenticate_endpoint)
    
    print(f"Autorize access in {authorization_url}")
    
    authorization_response = input("Enter the full callback URL: ")
    token = google.fetch_token(token_endpoint, authorization_response, client_secret)
    
    return token

client_id = ""
client_secret = ""
redirect_uri = ""
token = authenticate_google(client_id, client_secret, redirect_uri)