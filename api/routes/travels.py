from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from api.database.connection import get_db
from api.database.schemas.travels import TravelCreate, TravelResponse, TravelUpdate
from api.crud.travels import (
    create_travel,
    get_all_travels,
    get_travel_by_id,
    delete_travel_by_id,
    update_travel_by_id as update_travel_crud,
    search_travels
)

router = APIRouter()

@router.post("/create", response_model=TravelResponse)
def create_new_travel(travel: TravelCreate, db: Session = Depends(get_db)):
    return create_travel(db, travel)

@router.get("/all", response_model=list[TravelResponse])
def get_travels(db: Session = Depends(get_db)):
    return get_all_travels(db)

@router.get("/search", response_model=list[TravelResponse])
def search_travel(
    from_location: str = Query(..., description="Source location"),
    to_location: str = Query(..., description="Destination location"),
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db)
):
    travels = search_travels(db, from_location, to_location, skip=skip, limit=limit)
    if not travels:
        raise HTTPException(status_code=404, detail="No Travels found")
    return travels

@router.get("/{travel_id}", response_model=TravelResponse)
def get_travel(travel_id: int, db: Session = Depends(get_db)):
    travel = get_travel_by_id(db, travel_id)
    if not travel:
        raise HTTPException(status_code=404, detail="Travel not found")
    return travel

@router.put("/update/{travel_id}", response_model=TravelResponse)
def update_travel_route(travel_id: int, travel_data: TravelUpdate, db: Session = Depends(get_db)):
    updated = update_travel_crud(db, travel_id, travel_data)
    if not updated:
        raise HTTPException(status_code=404, detail="Travel not found")
    return updated

@router.delete("/delete/{travel_id}", response_model=TravelResponse)
def delete_travel_route(travel_id: int, db: Session = Depends(get_db)):
    deleted = delete_travel_by_id(db, travel_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Travel not found")
    return deleted
