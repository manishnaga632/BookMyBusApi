from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routes import auth, users, categories, products, address, carts, reviews, orders
from api.database.connection import engine
from api.database.base import Base

# Create database tables if they don't exist
Base.metadata.create_all(bind=engine)

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

# Include authentication-related routes
app.include_router(auth.router, prefix="/auth", tags=["Auth"])

# Include user-related routes
app.include_router(users.router, prefix="/users", tags=["Users"])

app.include_router(categories.router, prefix="/categories", tags=["Categories"])

app.include_router(products.router, prefix="/products", tags=["Products"])

app.include_router(address.router, prefix="/address", tags=["Address"])

app.include_router(carts.router, prefix="/cart", tags=["Cart"])

app.include_router(reviews.router, prefix="/reviews", tags=["Reviews"])

app.include_router(orders.router, prefix="/orders", tags=["Orders"])
