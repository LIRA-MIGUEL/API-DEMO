from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import csv  # Importa el módulo csv

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
    """
    # Endpoint Raíz
    ## 1-Status codes
    * 201 - Código de muestra
    * 334 - Otro estatus de prueba

    Este es el endpoint raíz de la API de Contactos.
    """
    return {"Hello": "World"}

@app.get("/v1/contactos", response_class=JSONResponse)
async def get_contactos():
    """
    # Obtener Contactos

    Obtiene la lista de contactos desde un archivo CSV.

    Returns:
        List[dict]: Lista de contactos en formato JSON.
    """
    datos = []
    with open('contactos.csv', 'r', newline='') as file:
        fieldnames = ('nombre', 'email')
        reader = csv.DictReader(file, fieldnames)
        for row in reader:
            datos.append(row)
    return datos

# Agregar la operación POST sin modificar las rutas y funciones existentes
@app.post("/v1/contactos", response_class=JSONResponse)
async def crear_contacto(contacto: ContactoCreate):
    nuevo_contacto = {
        "nombre": contacto.nombre,
        "email": contacto.email
    }
    # Aquí puedes agregar el código para guardar el nuevo contacto en tu archivo CSV o en tu base de datos.
    return {"mensaje": "Contacto creado con éxito", "contacto": nuevo_contacto}
