try :
    import authlib
except (ImportError, ModuleNotFoundError):
    __import__("os").system(
        f"{__import__('sys').executable} -m pip install -U authlib requests httpx"
    ) 
import config,requests,webbrowser

from authlib.integrations.httpx_client import AsyncOAuth2Client

client = AsyncOAuth2Client(config.client_id, config.client_secret, scope=config.scope)

authorization_endpoint = 'https://alphaapi.sasonline.in/oauth2/auth'

uri, state = client.create_authorization_url(authorization_endpoint)


webbrowser.open_new(uri)
