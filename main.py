from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

# INSTANCIAMOS LA CLASE
app = FastAPI()
# 'http://127.0.0.1:8000/' 

# BASEMODEL VALIDACION DE DATOS
class Libro(BaseModel):
    title: str
    authon: str
    pages: int
    year: Optional[int]

# El @ es un decorador para registrar la función e INDICAMOS LA RUTA, EN ESTE CASO ES LA RAIZ
@app.get('/')
def index():
    return {"Funcion": "principal"}

@app.get('/libros/{id}')
def mostrar_libros(id: int):
    return {'data': id}

@app.post('/libros')
def insertar_libro(libro: Libro):
    return {'message': f'el libro {libro.title} ha sido insertado'}
