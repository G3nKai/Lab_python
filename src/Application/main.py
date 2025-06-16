from typing import Union
from pydantic import BaseModel
from fastapi import FastAPI

from Infrastructure.database import engine, sessionLocal
from Domain.Models.person import Person

def test_db():
    db = sessionLocal()
    try:
        persons = db.query(Person).all()
        print(persons)
    finally:
        db.close()

if __name__ == "__main__":
    test_db()


app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}