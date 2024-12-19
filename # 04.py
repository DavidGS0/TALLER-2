# 04. Escribe un programa que solicite al usuario un número entero positivo y luego imprima si el número es un número de Armstrong utilizando un bucle while.

num = int(input("Introduce un número entero positivo: "))

num_digitos = len(str(num))

suma = 0
temp = num

while temp > 0:
    digito = temp % 10
    suma += digito ** num_digitos
    temp //= 10

if num == suma:
    print(f"{num} es un número de Armstrong.")
else:
    print(f"{num} no es un número de Armstrong.")