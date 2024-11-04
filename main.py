from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal, engine, Base
from app.models import ItemDB
from app.schemas import Market

# Создание всех таблиц в базе данных
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Получение сессии базы данных
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Маршрут для создания нового item и сохранения его в базу данных
@app.post("/items/")
def create_item(item: Market, db: Session = Depends(get_db)):
    db_item = ItemDB(name_item=item.name_item, description_item=item.description_item, price_item=item.price_item)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

# Маршрут для получения всех товаров
@app.get("/items/")
def get_all_items(db: Session = Depends(get_db)):
    items = db.query(ItemDB).all()
    return items

# Маршрут для получения товара по его ID
@app.get("/items/{item_id}")
def get_item_by_id(item_id: int, db: Session = Depends(get_db)):
    item = db.query(ItemDB).filter(ItemDB.id == item_id).first()
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item
