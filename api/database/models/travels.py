from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.sql import func
from api.database.connection import Base
from sqlalchemy.orm import relationship


class Travels(Base):
    __tablename__ = "travels"

    id = Column(Integer, primary_key=True, index=True)
    bus_image=Column(String(255), nullable=False)
    from_location = Column(String(100), nullable=False)
    to_location = Column(String(100), nullable=False)
    time = Column(String(50), nullable=False)
    available_seats = Column(Integer, nullable=False)
    price_per_seat = Column(Float, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    bookings = relationship("Booking", back_populates="travel")



