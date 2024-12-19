# 02. Escribe un programa que solicite al usuario dos números enteros positivos y luego imprima todos los números entre ellos (inclusive) utilizando un bucle while.

num1 = int(input("Introduce el primer número entero positivo: "))
num2 = int(input("Introduce el segundo número entero positivo: "))

if num1 > num2:
    num1, num2 = num2, num1 

i = num1

while i <= num2:
    print(i)
    i += 1