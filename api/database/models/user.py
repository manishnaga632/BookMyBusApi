from sqlalchemy import Column, Integer, String, DateTime, func
from api.database.connection import Base
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(255), unique=True, index=True, nullable=False)
    password = Column(String(255), nullable=False)
    mob_number = Column(String(15), unique=True, nullable=False)
    role = Column(String(50), default="customer", nullable=False)  # ✅ Default role added
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    bookings = relationship("Booking", back_populates="user")
