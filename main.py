from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Описываем структуру данных, которую ждем от пользователя
class Item(id: int, name: str, price: float): # Обычный класс или Pydantic BaseModel
    pass

# Исправим по стандартам Pydantic:
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    price: float

@app.get("/")
def read_root():
    return {"message": "Привет от Docker и CI/CD!"}

@app.get("/health")
def health_check():
    return {"status": "ok"}

# Новый POST-эндпоинт для создания товара
@app.post("/items/")
def create_item(item: Item):
    if item.price < 0:
        raise HTTPException(status_code=400, detail="Цена не может быть отрицательной")
    return {"status": "success", "item": item}