from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from api.database.connection import get_db
from api.database.schemas.booking import BookingCreate, BookingResponse
from api.crud.booking import create_booking, get_all_bookings, get_booking_by_id, update_booking, cancel_booking,get_bookings_by_user_id

router = APIRouter()

@router.post("/create", response_model=BookingResponse)
def create_new_booking(booking: BookingCreate, db: Session = Depends(get_db)):
    return create_booking(db, booking, booking.user_id)


@router.get("/all", response_model=list[BookingResponse])
def get_bookings(db: Session = Depends(get_db)):
    return get_all_bookings(db)

# routes/booking.py

from api.crud.booking import get_bookings_by_user_id

@router.get("/user/{user_id}", response_model=list[BookingResponse])
def get_user_bookings(user_id: int, db: Session = Depends(get_db)):
    bookings = get_bookings_by_user_id(db, user_id)
    if not bookings:
        raise HTTPException(status_code=404, detail="No bookings found for this user")
    return bookings


@router.get("/{booking_id}", response_model=BookingResponse)
def get_booking(booking_id: int, db: Session = Depends(get_db)):
    booking = get_booking_by_id(db, booking_id)
    if not booking:
        raise HTTPException(status_code=404, detail="Booking not found")
    return booking

@router.put("/update/{booking_id}", response_model=BookingResponse)
def update_booking_seats(booking_id: int, updated_seats: int = Query(..., description="Updated number of seats"), db: Session = Depends(get_db)):
    booking = update_booking(db, booking_id, updated_seats)
    if not booking:
        raise HTTPException(status_code=404, detail="Booking not found")
    return booking

@router.delete("/cancel/{booking_id}")
def cancel_user_booking(booking_id: int, db: Session = Depends(get_db)):
    success = cancel_booking(db, booking_id)
    if not success:
        raise HTTPException(status_code=404, detail="Booking not found")
    return {"message": "Booking cancelled successfully"}
