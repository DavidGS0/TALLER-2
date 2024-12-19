# 15. Escribe un programa que solicite al usuario un número entero positivo y luego imprima el promedio de todos los números desde 1 hasta ese número utilizando un bucle while

n = int(input("Introduce un número entero positivo: "))

suma = 0
i = 1

while i <= n:
    suma += i
    i += 1 
promedio = suma / n

print(f"La suma de los números desde 1 hasta {n} es: {suma}")
print(f"El promedio de los números desde 1 hasta {n} es: {promedio}")