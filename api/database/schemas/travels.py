from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class TravelCreate(BaseModel):
    bus_image:str
    from_location: str
    to_location: str
    time: str
    available_seats: int
    price_per_seat: float



    
class TravelUpdate(BaseModel):
    bus_image: Optional[str] = None
    from_location: Optional[str] = None
    to_location: Optional[str] = None
    time: Optional[str] = None
    available_seats: Optional[int] = None
    price_per_seat: Optional[float] = None

class TravelResponse(BaseModel):
    id: int
    bus_image:str
    from_location: str
    to_location: str
    time: str
    available_seats: int
    price_per_seat: float
    created_at: datetime

    class Config:
        from_attributes = True
