import os
from dotenv import load_dotenv
from kinde_sdk.kinde_api_client import GrantType

load_dotenv()

SITE_HOST = os.getenv("SITE_HOST", "localhost")
SITE_PORT = os.getenv("SITE_PORT", "8888")

# Quickstart copy/paste overwrite section
SITE_URL = f"http://{SITE_HOST}:{SITE_PORT}"
LOGOUT_REDIRECT_URL = f"http://{SITE_HOST}:{SITE_PORT}/api/auth/logout"
KINDE_CALLBACK_URL = f"http://{SITE_HOST}:{SITE_PORT}/api/auth/kinde_callback"
CLIENT_ID = os.getenv("KINDE_CLIENT_ID")
CLIENT_SECRET = os.getenv("KINDE_CLIENT_SECRET")
# Quickstart copy/paste overwrite section

KINDE_ISSUER_URL = os.getenv("KINDE_ISSUER_URL")
GRANT_TYPE = GrantType.AUTHORIZATION_CODE_WITH_PKCE
CODE_VERIFIER = os.getenv("SESSION_CODE_VERIFIER")
TEMPLATES_AUTO_RELOAD = True
SESSION_TYPE = "filesystem"
SESSION_PERMANENT = False
SECRET_KEY = os.getenv("SESSION_SECRET_KEY")
