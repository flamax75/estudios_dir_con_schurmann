from pathlib import Path


path = Path("/home/flamax75/mia.txt")


with path.open(mode="w") as file:
    file.write("hola esta es una prueba de crear archivos")


print(path.is_file())
print(path.is_dir())
print(path.exists())
print(path.absolute())
print(path.name,
      path.stem,
      path.suffix,
      path.parent)


new_path = path.with_suffix(".bat")
path.rename(new_path)


new_path2 = new_path.with_stem("nicolas")
new_path.rename(new_path2)
