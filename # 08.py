# 08. Escribe un programa que solicite al usuario un número entero positivo y luego imprima los primeros n números impares utilizando un bucle while.

n = int(input("Introduce un número entero positivo: "))

i = 1
contador_impares = 0

while contador_impares < n:
    if i % 2 != 0:
        print(i)
        contador_impares += 1
    i += 1