import json
from pathlib import Path


productos = [
    {"id": 1, "nombre": "coche"},
    {"id": 2, "nombre": "vivienda"},
    {"id": 3, "nombre": "mascota"},
    {"id": 3, "nombre": "motocicleta"},
]

data = json.dumps(productos)
Path("/home/flamax75/productos.json").write_text(data)

data = Path("/home/flamax75/productos.json").read_text(encoding="utf-8")
productos = json.loads(data)


productos[1]["nombre"] = "Castillo"
productos[0]["nombre"] = "audi"
productos[0]["id"] = 23

Path("/home/flamax75/productos.json").write_text(json.dumps(productos))
print(productos)
