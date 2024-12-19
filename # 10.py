# 10. Escribe un programa que solicite al usuario dos números enteros positivos y luego imprima la suma de todos los números entre ellos (inclusive) utilizando un bucle while.

num1 = int(input("Introduce el primer número entero positivo: "))
num2 = int(input("Introduce el segundo número entero positivo: "))


if num1 > num2:
    num1, num2 = num2, num1

i = num1
suma = 0

print(f"Los números entre {num1} y {num2} son:")
while i <= num2:
    print(i)
    suma += i
    i += 1

print(f"La suma de todos los números entre {num1} y {num2} es: {suma}")