import os
from dotenv import load_dotenv
from kinde_sdk.kinde_api_client import GrantType

load_dotenv()

SITE_HOST = "localhost"
SITE_PORT = "8000"

# Quickstart copy/paste overwrite section
SITE_URL = f"http://{SITE_HOST}:{SITE_PORT}"
LOGOUT_REDIRECT_URL = f"http://{SITE_HOST}:{SITE_PORT}/api/auth/logout"
KINDE_CALLBACK_URL = f"http://{SITE_HOST}:{SITE_PORT}/api/auth/kinde_callback"
CLIENT_ID = os.getenv("KINDE_CLIENT_ID")
CLIENT_SECRET = os.getenv("KINDE_SOME_SECRET")
# Quickstart copy/paste overwrite section

KINDE_ISSUER_URL = os.getenv("KINDE_ISSUER_URL")
GRANT_TYPE = GrantType.AUTHORIZATION_CODE_WITH_PKCE
CODE_VERIFIER = "joasd923nsad09823noaguesr9u3qtewrnaio90eutgersgdsfg" # A suitably long string > 43 chars
TEMPLATES_AUTO_RELOAD = True
SESSION_TYPE = "filesystem"
SESSION_PERMANENT = False
SECRET_KEY = "joasd923nsad09823noaguesr9u3qtewrnaio90eutgersgdsfgs" # Secret used for session management
