from pydantic import BaseModel

class Market(BaseModel):
    name_item: str
    description_item: str = None
    price_item: float

    class Config:
        orm_mode = True
