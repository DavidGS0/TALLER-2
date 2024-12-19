# 06. Escribe un programa que solicite al usuario un número entero positivo y luego imprima la suma de los cuadrados de todos los números desde 1 hasta ese número utilizando un bucle while

n = int(input("Introduce un número entero positivo: "))

suma_cuadrados = 0
i = 1

print(f"Los cuadrados de los números desde 1 hasta {n} son:")
while i <= n:
    cuadrado = i ** 2
    print(cuadrado)
    suma_cuadrados += cuadrado
    i += 1 

print(f"\nLa suma de los cuadrados de los números desde 1 hasta {n} es: {suma_cuadrados}")