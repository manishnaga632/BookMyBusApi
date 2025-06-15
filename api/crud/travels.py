from sqlalchemy.orm import Session
from sqlalchemy import and_, func
from fastapi import HTTPException
from api.database.models.travels import Travels
from api.database.schemas.travels import TravelCreate, TravelUpdate


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
    travel = db.query(Travels).filter(Travels.id == travel_id).first()
    if not travel:
        raise HTTPException(status_code=404, detail="Travel not found")
    return travel


def search_travels(db: Session, from_location: str, to_location: str, skip: int = 0, limit: int = 10):
    return db.query(Travels).filter(
        and_(
            func.lower(Travels.from_location).like(f"%{from_location.lower()}%"),
            func.lower(Travels.to_location).like(f"%{to_location.lower()}%")
        )
    ).offset(skip).limit(limit).all()


def update_travel_by_id(db: Session, travel_id: int, travel_data: TravelUpdate):
    travel = db.query(Travels).filter(Travels.id == travel_id).first()
    if not travel:
        raise HTTPException(status_code=404, detail="Travel not found")

    for field, value in travel_data.dict(exclude_unset=True).items():
        setattr(travel, field, value)

    db.commit()
    db.refresh(travel)
    return travel


def delete_travel_by_id(db: Session, travel_id: int):
    travel = db.query(Travels).filter(Travels.id == travel_id).first()
    if not travel:
        raise HTTPException(status_code=404, detail="Travel not found")

    db.delete(travel)
    db.commit()
    return travel
