from sqlalchemy import Column, Float, Integer, String
from app.database import Base


class ItemDB(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name_item = Column(String, index=True)
    description_item = Column(String, index=True)
    price_item = Column(Float)
