from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import csv

app = FastAPI()

class ContactoCreate(BaseModel):
    nombre: str
    email: str

@app.get(
    "/",
    response_class=JSONResponse,
    description="Endpoint raíz de la API Contactos",
    summary="Endpoint Raíz"
)
async def root():
    return {"Hello": "World"}

@app.get("/v1/contactos", response_class=JSONResponse)
async def get_contactos():
    datos = []
    with open('contactos.csv', 'r', newline='') as file:
        fieldnames = ('nombre', 'email')
        reader = csv.DictReader(file, fieldnames)
        for row in reader:
            datos.append(row)
    return datos

@app.post("/v1/contactos", response_class=JSONResponse)
async def crear_contacto(contacto: ContactoCreate):
    nuevo_contacto = {
        "nombre": contacto.nombre,
        "email": contacto.email
    }
    
    # Guardar el nuevo contacto en el archivo CSV
    with open('contactos.csv', 'a', newline='') as file:
        fieldnames = ['nombre', 'email']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writerow(nuevo_contacto)
    
    return {"mensaje": "Contacto creado con éxito", "contacto": nuevo_contacto}
