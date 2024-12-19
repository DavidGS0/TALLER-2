# 14. Escribe un programa que solicite al usuario un número entero positivo y luego imprima la suma de los números de Fibonacci hasta ese número utilizando un bucle while.

n = int(input("Introduce un número entero positivo: "))

a, b = 0, 1
suma_fibonacci = 0

print(f"Números de Fibonacci hasta {n}:")
while a <= n:
    print(a)
    suma_fibonacci += a
    a, b = b, a + b
print(f"\nLa suma de los números de Fibonacci hasta {n} es: {suma_fibonacci}")