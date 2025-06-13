from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer
from api.database.connection import get_db
from api.database.schemas.user import UserCreate, UserLogin, UserResponse
from api.crud.user import create_user, get_user_by_email, get_user_by_mobile
from api.security import verify_password
from api.token import create_access_token

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")

@router.post("/register", response_model=UserResponse)
def register(user: UserCreate, db: Session = Depends(get_db)):
    if get_user_by_email(db, user.email):
        raise HTTPException(status_code=400, detail="Email already registered")
    if get_user_by_mobile(db, user.mob_number):
        raise HTTPException(status_code=400, detail="Mobile number already registered")
    return create_user(db, user)

@router.post("/login")
def login(user_login: UserLogin, db: Session = Depends(get_db)):
    db_user = get_user_by_email(db, user_login.email)

    if not db_user or not verify_password(user_login.password, db_user.password):
        raise HTTPException(status_code=400, detail="Invalid credentials")

    access_token = create_access_token(user={"sub": db_user.email, "user_id": db_user.id})

    return {"access_token": access_token, "token_type": "bearer"}
