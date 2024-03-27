from pathlib import Path

ruta_archivo = "/home/flamax75/arcivo.txt"
nuevo_texto = """Ah, keep your eyes on the road, your hand upon the wheel
Keep your eyes on the road, your hand upon the wheel
Yeah, we're going to the roadhouse, gonna have a real, a good-time

Yeah, the back of the roadhouse, they got some bungalows
Yeah, the back of the roadhouse, they got some bungalows
And that's for the people who like to go down slow

Let it roll, baby, roll, let it roll, baby, roll
Let it roll, baby, roll, let it roll
All night long

Do it, Robby, do it!

You gotta roll, roll, roll
You gotta thrill my soul, all right
Roll, roll, roll, roll
Thrill my soul
You gotta beep a gunk a chucha
Honk konk konk
You gotta each you puna
Each ya bop a luba
Each y'all bump a kechonk
Ease sum konk
Ya, ride

Ashen lady
Ashen lady
Give up your vows
Give up your vows
Save our city
Save our city
Ah, right now

Well, I woke up this morning and I got myself a beer
Well, I woke up this morning and I got myself a beer
The future's uncertain and the end is always near

Let it roll, baby, roll, let it roll, baby, roll
Let it roll, baby, roll, let it roll
All night long

Agregar a la playlist
Tamaño
A
A
Cifrado
Imprimir
Corregir
Enviar la traducción


"""


try:
    with open(ruta_archivo, "w") as file:
        file.write(nuevo_texto)

    print("contenido reemplazado con exito")
    with open(ruta_archivo, "r") as file:
        contenido_reemplazado = file.read()
    print("\nTHE DOORS\nROADHOUSE BLUES")
    print(contenido_reemplazado)

except Exception as e:
    print(f"error en reemplazar el contenido del arcivo {e}")

archivo_original = Path("/home/flamax75/arcivo.txt")
nuevo_nombre_archivo = "letras_rooadhouse_TheDoors.txt"
# arcivo.write_text("\n".join(texto), "utf
archivo_original.rename(archivo_original.with_name(nuevo_nombre_archivo))
