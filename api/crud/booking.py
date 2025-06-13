from fastapi import HTTPException  
from sqlalchemy.orm import Session
from api.database.models.booking import Booking
from api.database.models.travels import Travels
from api.database.schemas.booking import BookingCreate
from datetime import datetime

def create_booking(db: Session, booking: BookingCreate, user_id: int):
    # Find the travel entry
    travel = db.query(Travels).filter(
        Travels.id == booking.travel_id
    ).first()

    if not travel:
        raise HTTPException(status_code=404, detail="Travel not found for booking")

    if travel.available_seats < booking.book_seats:
        raise HTTPException(status_code=400, detail="Not enough seats available")

    # Reduce available seats
    travel.available_seats -= booking.book_seats
    db.add(travel)

    # Ensure price is correctly fetched (remove trailing comma)
    price_per_seat = travel.price_per_seat
    total_price = booking.book_seats * price_per_seat

    # Create the booking
    new_booking = Booking(
        user_id=user_id,
        travel_id=booking.travel_id,
        bus_image=travel.bus_image,
        from_location=travel.from_location,
        to_location=travel.to_location,
        time=travel.time,
        book_seats=booking.book_seats,
        price_per_seat=price_per_seat,
        total_price=total_price,
        created_at=datetime.now(),
        updated_at=datetime.now()
    )

    db.add(new_booking)
    db.commit()
    db.refresh(new_booking)
    return new_booking



def get_all_bookings(db: Session):
    return db.query(Booking).all()

def get_booking_by_id(db: Session, booking_id: int):
    return db.query(Booking).filter(Booking.id == booking_id).first()

def update_booking(db: Session, booking_id: int, updated_seats: int):
    booking = get_booking_by_id(db, booking_id)
    if not booking:
        return None

    travel = db.query(Travels).filter(
        Travels.from_location == booking.from_location,
        Travels.to_location == booking.to_location,
        Travels.time == booking.time
    ).first()

    if not travel:
        return None

    seat_diff = updated_seats - booking.book_seats

    if seat_diff > 0:
        if travel.available_seats < seat_diff:
            raise Exception("Not enough additional seats available")
        travel.available_seats -= seat_diff
    else:
        travel.available_seats += abs(seat_diff)

    booking.book_seats = updated_seats
    booking.total_price = updated_seats * booking.price_per_seat

    db.add(booking)
    db.add(travel)
    db.commit()
    db.refresh(booking)
    return booking

def cancel_booking(db: Session, booking_id: int):
    booking = get_booking_by_id(db, booking_id)
    if not booking:
        return None

    travel = db.query(Travels).filter(
        Travels.from_location == booking.from_location,
        Travels.to_location == booking.to_location,
        Travels.time == booking.time
    ).first()

    if travel:
        travel.available_seats += booking.book_seats
        db.add(travel)

    db.delete(booking)
    db.commit()
    return True
