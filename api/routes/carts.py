

# from fastapi import APIRouter, Depends
# from sqlalchemy.orm import Session
# from api.database.connection import get_db
# from api.database.schemas.carts import CartsCreate, CartsResponse
# from api.crud.carts import create_cart, delete_cart, get_all_carts
# from typing import List
# from fastapi.security import OAuth2PasswordBearer
# from api.token import get_current_user
# from api.database.models.user import User

# # Create an OAuth2PasswordBearer instance for JWT token
# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# # Create API Router
# router = APIRouter()

# # Add to cart (requires user_id from token)
# @router.post("/add", response_model=CartsResponse)
# def add_cart(cart: CartsCreate, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
#     # Access user.id instead of user['id']
#     return create_cart(db, cart, user.id)  # Pass user ID to create_cart function






# # Delete cart (requires user_id from token)
# @router.delete("/delete/{cart_id}", response_model=dict)
# def delete(cart_id: int, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
#     # Access user.id instead of user['id']
#     return delete_cart(db, cart_id, user.id)  # Pass user ID to delete_cart function

# # List all carts for the logged-in user
# @router.get("/all_carts", response_model=List[CartsResponse])
# def list_carts(db: Session = Depends(get_db), user: User = Depends(get_current_user)):
#     # Access user.id instead of user['id']
#     return get_all_carts(db, user.id)  # Pass user ID to get_all_carts function
