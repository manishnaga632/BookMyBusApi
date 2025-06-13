from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routes import auth, users,travels,booking,contact
from api.database.connection import engine
from api.database.base import Base
# engine: Database se connect hone ke liye.

# Base: Saare models ka base class (SQLAlchemy ORM ka structure).


# Create database tables if they don't exist
Base.metadata.create_all(bind=engine)


# Ye line kehti hai: agar koi table nahi bana hai to automatically bana do SQLAlchemy models ke basis par.

# Ye runtime migration jaisa kaam karta hai. Production me Alembic use hota hai, but ye development ke liye sahi hai.

# Initialize FastAPI app
app = FastAPI()

# ✅ Add CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow frontend domain
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)


# Jab frontend (React/Next.js) aur backend (FastAPI) alag ports par hote hain (like 3000 & 8000), to browser security policy ke wajah se request block ho jati hai.

# CORS middleware ye allow karta hai ki frontend backend se safely baat kar sake.

# Include authentication-related routes
app.include_router(auth.router, prefix="/auth", tags=["Authentication"])

# Iska matlab: /auth ke under auth.py ke routes available honge.
# Tags UI documentation (/docs) me grouping ke liye hote hain.

# Include user-related routes
app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(travels.router, prefix="/Travels", tags=["Travels"])
app.include_router(booking.router, prefix="/Booking", tags=["Booking"])
app.include_router(contact.router, prefix="/Contact", tags=["Contact"])
















