from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class BookingBase(BaseModel):
    user_id:Optional[int]
    travel_id:int
    from_location: str
    to_location: str
    time: str
    book_seats: int
class BookingCreate(BookingBase):
    pass
class BookingUpdate(BaseModel):
    book_seats: int
class BookingResponse(BookingBase):
    id: int
    user_id: int
    travel_id:int
    bus_image: str
    price_per_seat: float
    total_price: float
    created_at: datetime
    updated_at:datetime

    class Config:
        from_attributes = True
