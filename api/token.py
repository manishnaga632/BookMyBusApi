from datetime import datetime, timedelta
from jose import JWTError, jwt
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from api.config import SECRET_KEY, ALGORITHM
from api.crud.user import get_user_by_email
from api.database.connection import get_db
from sqlalchemy.orm import Session

# Define the OAuth2 scheme for token authentication
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Function to create a JWT access token
def create_access_token(user: dict, expires_delta: timedelta = timedelta(minutes=60 * 12)):
    """
    Generates a JWT access token with an expiration time.
    """
    to_encode = {
        "sub": user["sub"],    # 'sub' = email
        "user_id": user["user_id"],    # user_id added in token
        "exp": datetime.utcnow() + expires_delta
    }
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# Function to retrieve the currently authenticated user from the JWT token
def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    """
    Decodes the JWT token to extract user information and validate authentication.
    """
    credentials_exception = HTTPException(status_code=401, detail="Could not validate credentials")

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        user_id: int = payload.get("user_id")
        
        if email is None or user_id is None:
            raise credentials_exception

    except JWTError:
        raise credentials_exception

    # Fetch the user from the database using the email
    user = get_user_by_email(db, email)
    if user is None or user.id != user_id:
        raise credentials_exception

    return user  # Return the authenticated user
