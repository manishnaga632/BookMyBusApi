from sqlalchemy import Column, Integer, String, Float, ForeignKey,DateTime, func
from sqlalchemy.orm import relationship
from api.database.connection import Base

class Booking(Base):
    __tablename__ = 'bookings'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), index=True)
    travel_id=Column(Integer, ForeignKey("travels.id"), index=True)
    bus_image = Column(String(255), nullable=False)
    from_location = Column(String(100), nullable=False)
    to_location = Column(String(100), nullable=False)
    time = Column(String(50), nullable=False)
    book_seats = Column(Integer, nullable=False)
    price_per_seat = Column(Float, nullable=False)
    total_price = Column(Float, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())  # ✅ FIXED
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())  # ✅ FIXED

    user = relationship("User", back_populates="bookings")
    travel = relationship("Travels", back_populates="bookings")






