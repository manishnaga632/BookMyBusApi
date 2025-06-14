from pydantic import BaseModel,EmailStr,ConfigDict
from typing import Optional

class AdminProfileBase(BaseModel):
    address: str
    mobile_number: str
    email:EmailStr
    since: int
    happy_travelers : int
    destinations_covered: int
    travel_partners: int

class AdminProfileCreate(AdminProfileBase):
    pass

class AdminProfileUpdate(AdminProfileBase):
    pass

class AdminProfileOut(AdminProfileBase):
    id: int


    model_config = ConfigDict(from_attributes=True)


