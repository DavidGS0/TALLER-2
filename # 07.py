# 07. Escribe un programa que solicite al usuario un número entero positivo y luego imprima la suma de los primeros n números pares utilizando un bucle while.

cantidad = int(input("Introduce la cantidad de números pares a sumar: "))

suma_pares = 0
i = 1
contador_pares = 0

while contador_pares < cantidad:
    if i % 2 == 0:
        suma_pares += i
        contador_pares += 1
    i += 1

print(f"La suma de los primeros {cantidad} números pares es: {suma_pares}")