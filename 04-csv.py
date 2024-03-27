import csv
import os

with open("/home/flamax75/arcivo.csv", "w") as arcivo:
    writer = csv.writer(arcivo)
    writer.writerow(["nombre", "apellido", "mascota", "nombre mascota"])
    writer.writerow(["flaviu", "maxim", "perro", "tango"])
    writer.writerow(["laura", "cozac", "gato", "michi"])
    writer.writerow(["poche", "revo", "soparla", "balaur"])


with open("/home/flamax75/arcivo.csv", "r") as arcivo:
    reader = csv.reader(arcivo)
    print(list(reader))
    arcivo.seek(0)
    for linea in reader:
        print(linea)


with open("/home/flamax75/arcivo.csv") as r, open("/home/flamax75/archivo_temp.csv", "w") as w:
    reader = csv.reader(r)
    writer = csv.writer(w)
    for linea in reader:
        if linea[0] == "poche":
            writer.writerow(["poche", "revo", "crocodil", "guzac"])
        else:
            writer.writerow(linea)

    os.remove("/home/flamax75/arcivo.csv")
    os.rename("/home/flamax75/archivo_temp.csv", "/home/flamax75/arcivo.csv")
