from io import open

texto = """"Well, I woke up this morning and I got myself a beer
Well, I woke up this morning and I got myself a beer
The future's uncertain and the end is always near"""


arcivo = open("/home/flamax75/refren.txt", "w")

arcivo.write(texto)
arcivo.close()

arcivo = open("/home/flamax75/refren.txt", "r")
texto = arcivo.readlines()
arcivo.close()
print(texto)


with open("/home/flamax75/refren.txt", "r") as arcivo:
    print(arcivo.readlines())
    arcivo.seek(0)
    for linea in arcivo:
        print(linea)
