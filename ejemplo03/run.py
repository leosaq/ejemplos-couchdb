import requests
import json
from config import url_base

# Cargar datos desde archivo
with open('datos.json', 'r') as f:
    # pasar los datos a estructuras de Python
    data = json.load(f)

lista_datos = []

for d in data['docs']:
    if d['nombre'][0] in ["A", "B", "L"]:
        lista_datos.append(d)

base_datos = "personas003"
# Configurar el acceso a la base de datos
url = f"{url_base}/{base_datos}/_bulk_docs"
headers = {'Content-Type': 'application/json'}

# Enviar datos
datos_finales = {'docs': lista_datos}
response = requests.post(url, headers=headers, json=datos_finales)

# Mostrar respuesta
print(response.status_code)
print(response.json())
