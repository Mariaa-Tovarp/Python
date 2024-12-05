estudiantes = {}

n= int(input("Ingrese el numero de estudiantes: "))

for i in range (n):
    nombre = input (f"Ingrese el nombre del estudiante {i + 1}: ")
    promedio = input (f"Ingrese el promedio de {nombre}: ")
    estudiantes[nombre] = promedio

print ("Diccionario de estudaintes y sus promedios: ")
for nombre, promedio in estudiantes.items():
    print(f"Estudiante: {nombre}, Promedio: {promedio}")

mejor_estudiante = max(estudiantes, key= estudiantes.get)
print(f"El estudiante con el promedio mas alto es {mejor_estudiante} con un promedio de {estudiantes} ")

while True:
    print ("---Actualizacion de datos---")
    nombre = input("Infrese el nombre delestudiantes (o 'Salirr' para terminar): ")
    if nombre.lower() == "Salirr":
        break
    promedio =float(input(f"Ingrese el nuevo promedio de {nombre}"))
    if nombre in estudiantes:
        print(f"Actualizando promedio de {nombre}...")
    else:
        print(f"Añadiendo nuevo registro para {nombre}")
    estudiantes[nombre] = promedio

    print ("Diccionario actualizando de estudiantes y sus promedios: ")
    for nombre, promedio in estudiantes.items():
        print(f"Estudiantes: {nombre}, Promedio: {promedio}")