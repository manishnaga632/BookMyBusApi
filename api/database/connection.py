from sqlalchemy import create_engine

# ✅ from sqlalchemy import create_engine
# Ye SQLAlchemy ka function hai jo database se connection banata hai.

# Example: PostgreSQL, MySQL, SQLite, etc.


from sqlalchemy.ext.declarative import declarative_base

# Ye function ek Base class return karta hai.

# Is Base se hum apne models banaate hain (jaise User, Product), jisse SQLAlchemy samajh sake ki ye database ke table hain.

from sqlalchemy.orm import sessionmaker

# sessionmaker() ek function hai jo session banata hai —
#  session ka matlab hai ek "connection" jiske through aap database me read/write karte ho.
from api.config import DATABASE_URL
# Ye line config.py file se DATABASE_URL (database ka connection string) import karti hai.



engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False} if "sqlite" in DATABASE_URL else {})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Ye ek function banata hai jisse hum har request ke liye naya session (connection) le sakte hain.

# autocommit=False → SQL queries tab tak commit nahi hoti jab tak manually commit() na karo.

# autoflush=False → Performance ke liye. Auto data refresh off rakhta hai.

# bind=engine → Ye session kis database ke engine se connected hoga, ye set karta hai.

Base = declarative_base()

# Ye ek base class banata hai jisse hum apne database models (tables) banaate hain.

# Har model class (jaise User, Cart, etc.) is Base ko inherit karta hai.


# engine ek main object hai jo actual DB ke saath connection banata hai.

# Agar tum SQLite use kar rahe ho, 
# toh uske sath ek special setting check_same_thread=False dena padta hai (multi-threading issues avoid karne ke liye).

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# 🔹 Kaam kya karta hai?

# Ye ek FastAPI-compatible dependency function hai.

# Jab bhi API route me DB chahiye hota hai, hum Depends(get_db) use karte hain.

# Is function se ek db session milega:

# db = SessionLocal() → ek naya session ban gaya.

# yield db → FastAPI ko session de diya temporarily.

# finally db.close() → kaam khatam hone ke baad DB session band ho gaya (safe coding practice).