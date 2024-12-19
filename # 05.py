# 05. Escribe un programa que solicite al usuario un número entero positivo y luego imprima todos los números primos menores o iguales a ese número utilizando un bucle while.

def es_primo(num):
    if num <= 1:
        return False
    i = 2
    while i * i <= num:
        if num % i == 0:
            return False
        i += 1
    return True

n = int(input("Introduce un número entero positivo: "))

i = 2

while i <= n:
    if es_primo(i):
        print(i)
    i += 1