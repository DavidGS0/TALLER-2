# 13. Escribe un programa que solicite al usuario dos números enteros positivos y luego imprima la tabla de multiplicar del primer número hasta el segundo número utilizando un bucle while.

num_base = int(input("Introduce el número base de la tabla de multiplicar: "))
num_limite = int(input("Introduce el número hasta el cual multiplicar: "))

i = 1

print(f"Tabla de multiplicar del {num_base} hasta {num_limite}:")
while i <= num_limite:
    print(f"{num_base} x {i} = {num_base * i}")
    i += 1