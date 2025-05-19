# Ejercicio 1
def imprimir_hola_mundo() -> None:
    
    print("Hola Mundo!")

# Ejercicio 2
def saludar_usuario(nombre: str) -> str:
    
    return f"Hola {nombre}!"

# Ejercicio 3
def informacion_personal(nombre: str, apellido: str, edad: int, residencia: str) -> None:
    
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

# Ejercicio 4
import math

def calcular_area_circulo(radio: float) -> float:
    
    return math.pi * radio ** 2

def calcular_perimetro_circulo(radio: float) -> float:
    
    return 2 * math.pi * radio

# Ejercicio 5
def segundos_a_horas(segundos: float) -> float:
    
    return segundos / 3600

# Ejercicio 6
def tabla_multiplicar(numero: int) -> None:
   
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

# Ejercicio 7
def operaciones_basicas(a: float, b: float) -> tuple[float, float, float, float]:
    
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else float('nan')  # Manejo de división por cero
    return (suma, resta, multiplicacion, division)

# Ejercicio 8
def calcular_imc(peso: float, altura: float) -> float:
    
    return round(peso / (altura ** 2), 2)

# Ejercicio 9
def celsius_a_fahrenheit(celsius: float) -> float:
    
    return (celsius * 9/5) + 32

# Ejercicio 10
def calcular_promedio(a: float, b: float, c: float) -> float:
    
    return (a + b + c) / 3

# Programa principal
if __name__ == "__main__":
    print("=== Ejercicio 1 ===")
    imprimir_hola_mundo()
    
    print("\n=== Ejercicio 2 ===")
    nombre = input("Por favor ingrese su nombre: ")
    print(saludar_usuario(nombre))
    
    print("\n=== Ejercicio 3 ===")
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    edad = int(input("Edad: "))
    residencia = input("Residencia: ")
    informacion_personal(nombre, apellido, edad, residencia)
    
    print("\n=== Ejercicio 4 ===")
    radio = float(input("Ingrese el radio del círculo: "))
    print(f"Área: {calcular_area_circulo(radio):.2f}")
    print(f"Perímetro: {calcular_perimetro_circulo(radio):.2f}")
    
    print("\n=== Ejercicio 5 ===")
    segundos = float(input("Ingrese la cantidad de segundos: "))
    print(f"Equivale a {segundos_a_horas(segundos):.2f} horas")
    
    print("\n=== Ejercicio 6 ===")
    numero = int(input("Ingrese un número para ver su tabla de multiplicar: "))
    tabla_multiplicar(numero)
    
    print("\n=== Ejercicio 7 ===")
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    resultados = operaciones_basicas(num1, num2)
    print(f"Suma: {resultados[0]}")
    print(f"Resta: {resultados[1]}")
    print(f"Multiplicación: {resultados[2]}")
    print(f"División: {resultados[3]}")
    
    print("\n=== Ejercicio 8 ===")
    peso = float(input("Ingrese su peso en kg: "))
    altura = float(input("Ingrese su altura en metros: "))
    print(f"Su IMC es: {calcular_imc(peso, altura)}")
    
    print("\n=== Ejercicio 9 ===")
    celsius = float(input("Ingrese la temperatura en Celsius: "))
    print(f"Equivale a {celsius_a_fahrenheit(celsius):.2f}° Fahrenheit")
    
    print("\n=== Ejercicio 10 ===")
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    num3 = float(input("Ingrese el tercer número: "))
    print(f"El promedio es: {calcular_promedio(num1, num2, num3):.2f}")