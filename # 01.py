# 01. Escribe un programa que solicite al usuario un número entero positivo y luego imprima todos los números entre 1 y ese número que sean múltiplos de 5 utilizando un bucle while.

n = int(input("Introduce un número entero positivo: "))

i = 1

while i <= n:
    if i % 5 == 0:
        print(i)
    i += 1  