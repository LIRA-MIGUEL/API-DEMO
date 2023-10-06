import requests
import json

URI = "https://www.dnd5eapi.co/api/classes"

response = requests.get(URI)

if response.status_code == 200:
    response_json = response.json()

print("Seleccione un personaje de D&D 5e:")

for i in range(12):
    data = response_json['results'][i]
    name = data['name']
    print(f"{i + 1}: {name}")

opcion = input("Ingrese el número del personaje que desea seleccionar: ")

try:
    opcion = int(opcion)
    if 1 <= opcion <= 12:
        seleccion = response_json['results'][opcion - 1]
        print(f"Ha seleccionado el personaje: {seleccion['name']}")
    else:
        print("Número de opción no válido. Debe estar entre 1 y 12.")
except ValueError:
    print("Entrada no válida. Ingrese un número válido.")
