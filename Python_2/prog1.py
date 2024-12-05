num_empleados = int(input("Ingrese la cantidad de empleados: "))

salarios = []
num_empleados_bajo = 0
num_empleados_alto = 0
total_salarios = 0
i = 0

while i < num_empleados:
    salario = float(input(f"Ingrese el salario del empleado {i+1}: "))
    salarios.append(salario) 
    total_salarios += salario  

    if 1000000 <= salario <= 3000000:
        num_empleados_bajo += 1
    elif salario > 3000000:
        num_empleados_alto += 1

    i += 1

print(f"Lista de sueldos capturados: {salarios}")
print(f"Cantidad de empleados con salario entre $1,000,000 y $3,000,000: {num_empleados_bajo}")
print(f"Cantidad de empleados con salario mayor a $3,000,000: {num_empleados_alto}")
print(f"Total de salarios pagados por la empresa: ${total_salarios:.2f}")
