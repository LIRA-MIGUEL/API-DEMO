from fastapi import FastAPI
import csv
from fastapi import FastAPI, status

app = FastAPI()

@app.get(
    "/",
    status_code=201,
    description="Endpoint raiz de la API Contactos",
    summary="Endpoint Raiz"
    )
async def root():
    """
    #Endpoint Raiz 
    ##1-Status codes
    *289-codigo de muestra 
    *334-otro estatus de prueba 
    """
    return {"Hello": "World"}

@app.get("/v1/contactos")
def get_contactos():
    datos = []
    with open('contactos.csv', 'r', newline='') as file:
        fieldnames = ('nombre', 'email')
        reader = csv.DictReader(file, fieldnames)
        for row in reader:
            datos.append(row)
    return datos
