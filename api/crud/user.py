from sqlalchemy.orm import Session
from api.database.models.user import User
from api.database.schemas.user import UserCreate
from api.security import hash_password
from datetime import datetime

# Create new user
def create_user(db: Session, user: UserCreate):
    db_user = User(
        name=user.name,
        email=user.email,
        password=hash_password(user.password),  # 🔥 Hash password
        mob_number=user.mob_number,
        role="customer",
        created_at=datetime.now(),
        updated_at=datetime.now()
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Get user by email
def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

# Get user by mobile
def get_user_by_mobile(db: Session, mob_number: str):
    return db.query(User).filter(User.mob_number == mob_number).first()

# Update user
def update_user_profile(db: Session, user_id: int, update_data: dict):
    db.query(User).filter(User.id == user_id).update(update_data)
    db.commit()
    return db.query(User).filter(User.id == user_id).first()

# Get all users
def get_all_users(db: Session):
    return db.query(User).all()

# Delete user
def delete_user(db: Session, user_id: int):
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        db.delete(user)
        db.commit()
        return True
    return False





