from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str | None = None  # Optional field
    price: float
    tax: float | None = None

@app.post("/items/")
def create_item(item: Item):
    # 'item' is now a fully validated Pydantic object!
    total_price = item.price + (item.tax if item.tax else 0)
    return {"name": item.name, "total": total_price}
@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int,user_id: int = None):  
    return {"item_id": item_id,"user_id":user_id}