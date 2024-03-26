from io import open

texto = """"Well, I woke up this morning and I got myself a beer
Well, I woke up this morning and I got myself a beer
The future's uncertain and the end is always near"""


archivo = open("/home/flamax75/refren.txt", "w")

archivo.write(texto)
archivo.close()

archivo = open("/home/flamax75/refren.txt", "r")
texto = archivo.readlines()
archivo.close()
print(texto)


with open("/home/flamax75/refren.txt", "r") as archivo:
    print(archivo.readlines())
    archivo.seek(0)
    for linea in archivo:
        print(linea)
