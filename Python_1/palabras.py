# Leer las dos palabras
palabra1 = input("Ingresa la primera palabra: ")
palabra2 = input("Ingresa la segunda palabra: ")

# Verificar si palabra1 es sufijo de palabra2
if palabra1.endswith(palabra2):
    print(f'"{palabra2}" es sufijo de "{palabra1}".')
else:
    print(f'"{palabra2}" no es sufijo de "{palabra1}".')


# Verificar si palabra1 es sufijo de palabra2
if palabra1.endswith(palabra2):
    print((palabra2)+" es sufijo de "+(palabra1))
else:
    print((palabra2)+" no es sufijo de "+(palabra1))
