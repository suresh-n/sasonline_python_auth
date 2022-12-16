import config

from authlib.integrations.requests_client import OAuth2Session
client = OAuth2Session(config.client_id, config.client_secret, scope=config.scope)

authorization_response = 'copy your URL here'
token_endpoint = 'https://alphaapi.sasonline.in/oauth2/token'
token = client.fetch_token(token_endpoint, authorization_response=authorization_response)
print(token)
