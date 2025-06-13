from pydantic import BaseModel, EmailStr, validator
from typing import Optional
from datetime import datetime

# For user registration
class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str
    mob_number: str

# For normal user update
class UserUpdate(BaseModel):
    mob_number: Optional[str] = None
    new_password: Optional[str] = None
    confirm_password: Optional[str] = None

    @validator("confirm_password")
    def passwords_match(cls, confirm_password, values):
        if values.get('new_password') and confirm_password != values['new_password']:
            raise ValueError("New password and confirm password do not match")
        return confirm_password

# For admin-level update
class AdminUserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None
    mob_number: Optional[str] = None

# For API response
class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    mob_number: str
    role: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

# For login
class UserLogin(BaseModel):
    email: EmailStr
    password: str
