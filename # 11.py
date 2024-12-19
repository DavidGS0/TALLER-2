# 11. Escribe un programa que solicite al usuario un número entero positivo y luego calcule la cantidad de dígitos del número utilizando un bucle while.

numero = int(input("Introduce un número entero positivo: "))

cantidad_digitos = 0

while numero > 0:
    numero //= 10
    cantidad_digitos += 1

print(f"La cantidad de dígitos del número es: {cantidad_digitos}")