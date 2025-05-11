# # Ejercicio 1
# for i in range(101):
#     print(i)
# # Ejercicio 2
# numero = input("Ingrese un número entero: ")
# print("Cantidad de dígitos:", len(numero))

# # Ejercicio 3
# a = int(input("Ingrese el primer número: "))
# b = int(input("Ingrese el segundo número: "))
# suma = 0
# for i in range(min(a, b) + 1, max(a, b)):
#     suma += i
# print("Suma:", suma)

# # Ejercicio 4
# total = 0
# num = int(input("Ingrese un número (0 para terminar): "))  # Primera lectura fuera del bucle
# while num != 0:
#     total += num
#     num = int(input("Ingrese otro número (0 para terminar): "))  # Actualización dentro del bucle
# print("Total acumulado:", total)

# # Ejercicio 5
# import random

# numero_secreto = random.randint(0, 9)
# intentos = 0
# intento = -1  # Inicializamos con un valor que nunca coincidirá (ej. -1)

# while intento != numero_secreto:
#     intento = int(input("Adivina el número (0-9): "))
#     intentos += 1

# print(f"¡Correcto! Intentos: {intentos}")

# #ejercicio 6
# for i in range(100, -1, -2):
#     print(i)

# #ejercicio 7
# n = int(input("Ingrese un número positivo: "))
# suma = 0
# for i in range(n + 1):
#     suma += i
# print("Suma total:", suma)

# #ejercicio 8
# pares = impares = positivos = negativos = 0
# for _ in range(100):
#     num = int(input("Ingrese un número: "))
#     if num % 2 == 0:
#         pares += 1
#     else:
#         impares += 1
#     if num > 0:
#         positivos += 1
#     elif num < 0:
#         negativos += 1
# print(f"Pares: {pares}, Impares: {impares}, Positivos: {positivos}, Negativos: {negativos}")

# #ejercicio 9
# suma = 0
# for _ in range(100):
#     num = int(input("Ingrese un número: "))
#     suma += num
# print("Media:", suma / 100)

# #ejercicio 10
# numero = input("Ingrese un número: ")
# print("Número invertido:", numero[::-1])

def main ():
    nums = [1,2,3,4,5]
    result = 1
    for num in nums:
        result *= num
        if result > 10:
            break
    print(result)

main()