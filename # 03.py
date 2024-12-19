# 03. Escribe un programa que solicite al usuario un número entero positivo y luego calcule la suma de todos los números divisibles por 3 desde 1 hasta ese número utilizando un bucle while.

n = int(input("Introduce un número entero positivo: "))

suma = 0
i = 1

while i <= n:
    if i % 3 == 0:
        suma += i
    i += 1

print(f"La suma de todos los números divisibles por 3 desde 1 hasta {n} es: {suma}")