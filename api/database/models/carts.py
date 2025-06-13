

# from sqlalchemy import Column, Integer, DateTime, ForeignKey, func
# from sqlalchemy.orm import relationship
# from api.database.connection import Base
# from api.database.models.products import Products  # Import the Products model
# from api.database.models.user import User  # Assuming you have a Users model


# class Carts(Base):
#     __tablename__ = "cart"

#     id = Column(Integer, primary_key=True, index=True)
#     user_id = Column(Integer, ForeignKey("users.id"), index=True)  # Linking to Users table
#     product_id = Column(Integer, ForeignKey("products.id"), index=True)  # Linking to Products table
#     quantity = Column(Integer, default=1)
#     created_at = Column(DateTime, default=func.now())

#     # Relationships
#     product = relationship("Products", back_populates="carts")  # Linking to Products model
#     user = relationship("User", back_populates="carts")



