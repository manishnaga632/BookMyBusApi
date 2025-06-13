from pydantic import BaseModel
from datetime import datetime

class TravelCreate(BaseModel):
    bus_image:str
    from_location: str
    to_location: str
    time: str
    available_seats: int
    price_per_seat: float

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
