from typing import Union
from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/suma")
def get_suma(numero1 : float, numero2 : float):
    suma = numero1 + numero2
    return {"Rsultado": suma}
    /suma?numero1=5&numero2=10