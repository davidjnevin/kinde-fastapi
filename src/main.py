from typing import Union
from fastapi import FastAPI, Depends, HTTPException, status, Request
from starlette.middleware.sessions import SessionMiddleware
from kinde_sdk.kinde_api_client import KindeApiClient

import src.config as config


app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=config.SECRET_KEY)

# user clients dictionary to store Kinde clients for each user
user_clients = {}

# Dependency to get the current user's KindeApiClient instance
def get_kinde_client(request: Request) -> KindeApiClient:
    user_id = request.session.get("user_id")
    if user_id is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Not authenticated")

    if user_id not in user_clients:
        # If the client does not exist, create a new instance with parameters
        user_clients[user_id] = KindeApiClient()

    kinde_client = user_clients[user_id]
    # Ensure the client is authenticated
    if not kinde_client.is_authenticated():
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Not authenticated")

    return kinde_client


@app.get("/")
def read_root(kinde_client: KindeApiClient = Depends(get_kinde_client)):
    return {"Hello": "David"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None, kinde_client: KindeApiClient = Depends(get_kinde_client)):
    return {"item_id": item_id, "q": q}
