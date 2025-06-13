from sqlalchemy.orm import Session
from sqlalchemy import and_, or_
from sqlalchemy.sql import func
from api.database.models.travels import Travels
from api.database.schemas.travels import TravelCreate

def create_travel(db: Session, travel: TravelCreate):
    new_travel = Travels(
        bus_image=travel.bus_image,
        from_location=travel.from_location,
        to_location=travel.to_location,
        time=travel.time,
        available_seats=travel.available_seats,
        price_per_seat=travel.price_per_seat
        
    )
    db.add(new_travel)
    db.commit()
    db.refresh(new_travel)
    return new_travel

def get_all_travels(db: Session):
    return db.query(Travels).all()

def get_travel_by_id(db: Session, travel_id: int):
    return db.query(Travels).filter(Travels.id == travel_id).first()

def search_travels(db: Session, from_location: str, to_location: str, skip: int = 0, limit: int = 10):
    return db.query(Travels).filter(
        and_(
            func.lower(Travels.from_location).like(f"%{from_location.lower()}%"),
            func.lower(Travels.to_location).like(f"%{to_location.lower()}%")
        )
    ).offset(skip).limit(limit).all()
