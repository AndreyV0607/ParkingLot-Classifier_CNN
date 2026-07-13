# Crear dataset desde las carpetas con imagenes

from pathlib import Path
import csv
import random


BASE_DIR = Path(__file__).resolve().parent

# Carpetas
carpeta_libres = BASE_DIR / "dataset" / "0_Parqueo"
carpeta_ocupados = BASE_DIR / "dataset" / "1_Parqueo"

# Extensiones aceptadas
extensiones = ["*.jpg", "*.jpeg", "*.png", "*.webp"]

datos = []

for extension in extensiones:
    for imagen in carpeta_libres.glob(extension):
        datos.append({
            "ruta_imagen": str(imagen.relative_to(BASE_DIR)),
            "label": 0
        })

for extension in extensiones:
    for imagen in carpeta_ocupados.glob(extension):
        datos.append({
            "ruta_imagen": str(imagen.relative_to(BASE_DIR)),
            "label": 1
        })

if not datos:
    raise RuntimeError("No se encontraron imagenes para crear el dataset.")

random.seed(42)
random.shuffle(datos)

# Guardar el dataset en un archivo CSV
ruta_salida = BASE_DIR / "dataset" / "dataset.csv"
ruta_salida.parent.mkdir(parents=True, exist_ok=True)

with ruta_salida.open("w", newline="", encoding="utf-8") as archivo:
    writer = csv.DictWriter(archivo, fieldnames=["ruta_imagen", "label"])
    writer.writeheader()
    writer.writerows(datos)

print("Dataset creado correctamente en:")
print(ruta_salida, "\n")

print("Cantidad de imagenes:", len(datos))
print("Libres:", sum(1 for fila in datos if fila["label"] == 0))
print("Ocupados:", sum(1 for fila in datos if fila["label"] == 1))
