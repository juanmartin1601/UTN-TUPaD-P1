# TRABAJO PRÁCTICO DE RECURSIVIDAD - TECNICATURA EN PROGRAMACIÓN

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def mostrar_factoriales():
    num = int(input("\nIngrese un número entero positivo para calcular factoriales: "))
    print("\nFactoriales:")
    for i in range(1, num + 1):
        print(f"{i}! = {factorial(i)}")

def fibonacci(pos):
    if pos == 0:
        return 0
    elif pos == 1:
        return 1
    return fibonacci(pos - 1) + fibonacci(pos - 2)

def mostrar_serie_fibonacci():
    posicion = int(input("\nIngrese la posición hasta la que desea ver la serie Fibonacci: "))
    print("\nSerie de Fibonacci:")
    for i in range(posicion + 1):
        print(fibonacci(i), end=" ")
    print()

def potencia(base, exponente):
    if exponente == 0:
        return 1
    return base * potencia(base, exponente - 1)

def calcular_potencia():
    base = int(input("\nIngrese la base: "))
    exponente = int(input("Ingrese el exponente: "))
    print(f"\nResultado: {base}^{exponente} = {potencia(base, exponente)}")

def decimal_a_binario(n):
    if n == 0:
        return ""
    return decimal_a_binario(n // 2) + str(n % 2)

def convertir_a_binario():
    numero = int(input("\nIngrese un número decimal positivo: "))
    binario = decimal_a_binario(numero) if numero != 0 else "0"
    print(f"\nEl número {numero} en binario es: {binario}")

def es_palindrome(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindrome(palabra[1:-1])

def verificar_palindromo():
    cadena = input("\nIngrese una palabra (sin espacios ni tildes): ").lower()
    if es_palindrome(cadena):
        print(f"\n'{cadena}' ES un palíndromo")
    else:
        print(f"\n'{cadena}' NO es un palíndromo")

def suma_digitos(n):
    if n < 10:
        return n
    return n % 10 + suma_digitos(n // 10)

def calcular_suma_digitos():
    numero = int(input("\nIngrese un número entero positivo: "))
    print(f"\nSuma de dígitos: {suma_digitos(numero)}")

def contar_bloques(n):
    if n == 1:
        return 1
    return n + contar_bloques(n - 1)

def calcular_bloques_piramide():
    niveles = int(input("\nIngrese bloques en el nivel base: "))
    print(f"\nTotal de bloques necesarios: {contar_bloques(niveles)}")

def contar_digito(numero, digito):
    if numero == 0:
        return 0
    ultimo_digito = numero % 10
    conteo = 1 if ultimo_digito == digito else 0
    return conteo + contar_digito(numero // 10, digito)

def contar_digitos_numero():
    num = int(input("\nIngrese un número entero positivo: "))
    d = int(input("Ingrese un dígito a buscar (0-9): "))
    resultado = contar_digito(num, d) if num != 0 else (1 if d == 0 else 0)
    print(f"\nEl dígito {d} aparece {resultado} veces en {num}")

def mostrar_menu():
    print("\n" + "="*50)
    print("TRABAJO PRÁCTICO DE RECURSIVIDAD".center(50))
    print("="*50)
    print("1. Calcular factoriales (Ejercicio 1)")
    print("2. Mostrar serie Fibonacci (Ejercicio 2)")
    print("3. Calcular potencia (Ejercicio 3)")
    print("4. Convertir decimal a binario (Ejercicio 4)")
    print("5. Verificar palíndromo (Ejercicio 5)")
    print("6. Sumar dígitos de un número (Ejercicio 6)")
    print("7. Calcular bloques de pirámide (Ejercicio 7)")
    print("8. Contar dígitos en un número (Ejercicio 8)")
    print("0. Salir")
    print("="*50)

def main():
    """Función principal que maneja el menú interactivo"""
    while True:
        mostrar_menu()
        opcion = input("\nSeleccione un ejercicio (0-8): ")
        
        if opcion == "0":
            print("\n¡Gracias por usar el programa!")
            break
        elif opcion == "1":
            mostrar_factoriales()
        elif opcion == "2":
            mostrar_serie_fibonacci()
        elif opcion == "3":
            calcular_potencia()
        elif opcion == "4":
            convertir_a_binario()
        elif opcion == "5":
            verificar_palindromo()
        elif opcion == "6":
            calcular_suma_digitos()
        elif opcion == "7":
            calcular_bloques_piramide()
        elif opcion == "8":
            contar_digitos_numero()
        else:
            print("\nOpción no válida. Intente nuevamente.")
        
        input("\nPresione Enter para continuar...")

if __name__ == "__main__":
    main()