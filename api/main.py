from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routes import auth, users,travels,booking,contact,admin_profile
from api.database.connection import engine
from api.database.base import Base

Base.metadata.create_all(bind=engine)
app = FastAPI()
# ✅ Add CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)
app.include_router(auth.router, prefix="/auth", tags=["Authentication"])
app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(travels.router, prefix="/Travels", tags=["Travels"])
app.include_router(booking.router, prefix="/Booking", tags=["Booking"])
app.include_router(contact.router, prefix="/Contact", tags=["Contact"])
app.include_router(admin_profile.router, prefix="/Admin_Profile", tags=["Admin_Profile"])
















