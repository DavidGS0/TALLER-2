# 09. Escribe un programa que solicite al usuario un número entero positivo y luego imprima todos los números entre 1 y ese número en orden inverso utilizando un bucle while.

n = int(input("Introduce un número entero positivo: "))

i = n

while i >= 1:
    print(i)
    i -= 1