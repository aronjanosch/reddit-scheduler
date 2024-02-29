from fastapi import Depends, HTTPException, status, Request
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from firebase_admin import auth
from app import models, crud
from app.db import get_database

oauth2_scheme = HTTPBearer()

def get_current_user(request: Request, credentials: HTTPAuthorizationCredentials = Depends(oauth2_scheme)):
    token = credentials.credentials
    db = get_database()
    try:
        decoded_token = auth.verify_id_token(token)
        request.state.user = decoded_token  # Optionally add the user info to the request state
        current_user = crud.get_user_by_firebase_uid(db, decoded_token["uid"])
        return current_user
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
def get_current_active_superuser(current_user: dict = Depends(get_current_user)) -> models.User:
    if not crud.is_superuser(current_user):
        raise HTTPException(status_code=400, detail="The user doesn't have enough privileges")
    return current_user
