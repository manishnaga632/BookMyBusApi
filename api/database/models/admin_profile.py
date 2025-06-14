
    

from sqlalchemy import Column, Integer, String
from api.database.connection import Base  

class AdminProfile(Base):
    __tablename__ = "admin_profiles"

    id = Column(Integer, primary_key=True, index=True)
    address = Column(String, nullable=False)
    mobile_number = Column(String, nullable=False)
    email = Column(String, nullable=False)
    since = Column(Integer, nullable=False)
    destinations_covered = Column(Integer, nullable=False)
    travel_partners = Column(Integer, nullable=False)
    happy_travelers = Column(Integer, nullable=False)

