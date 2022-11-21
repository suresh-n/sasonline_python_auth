client_id = 'SAS-CLIENT'
client_secret = ''  # copy the code sahred by sas online customer support here.
scope = 'orders holdings'
redirect_uri = 'http://127.0.0.1'

from authlib.integrations.requests_client import OAuth2Session
client = OAuth2Session(client_id, client_secret, scope=scope)

from authlib.integrations.httpx_client import AsyncOAuth2Client

client = AsyncOAuth2Client(client_id, client_secret, scope=scope)

authorization_endpoint = 'https://alphaapi.sasonline.in/oauth2/auth'

uri, state = client.create_authorization_url(authorization_endpoint)

print(uri)
