import random
from statistics import mode, median, mean
def ejercicio1():
    
    edad = int(input("Ingrese su edad: "))
    if edad > 18:
        print("Es mayor de edad")
    else:
        print("No es mayor de edad")


def ejercicio2():
    
    nota = float(input("Ingrese su nota: "))
    if nota >= 6:
        print("Aprobado")
    else:
        print("Desaprobado")


def ejercicio3():
    
    num = int(input("Ingrese un número: "))
    if num % 2 == 0:
        print("Ha ingresado un número par")
    else:
        print("Por favor, ingrese un número par")


def ejercicio4():
    
    edad = int(input("Ingrese su edad: "))
    if edad < 12:
        print("Niño/a")
    elif edad < 18:
        print("Adolescente")
    elif edad < 30:
        print("Adulto/a joven")
    else:
        print("Adulto/a")


def ejercicio5():
    
    password = input("Ingrese una contraseña: ")
    if 8 <= len(password) <= 14:
        print("Ha ingresado una contraseña correcta")
    else:
        print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")


def ejercicio6():
    
    

    numeros_aleatorios = [random.randint(1, 100) for _ in range(50)]
    
    mod = mode(numeros_aleatorios)
    med = median(numeros_aleatorios)
    avg = mean(numeros_aleatorios)
    
    print("Lista de números:", numeros_aleatorios)
    print("Media:", avg)
    print("Mediana:", med)
    print("Moda:", mod)
    
    if mod is None:
        print("No se pudo determinar una moda única.")
    else:
        if avg > med and med > mod:
            print("Sesgo positivo o a la derecha")
        elif avg < med and med < mod:
            print("Sesgo negativo o a la izquierda")
        elif avg == med == mod:
            print("Sin sesgo")
        else:
            print("No se cumple ningún criterio de sesgo")


def ejercicio7():
    
    frase = input("Ingrese una frase o palabra: ")
    if frase and frase[-1].lower() in "aeiou":
        print(frase + "!")
    else:
        print(frase)


def ejercicio8():
    
    nombre = input("Ingrese su nombre: ")
    opcion = input("Ingrese 1 para mayúsculas, 2 para minúsculas, 3 para la primera letra en mayúscula: ")
    if opcion == "1":
        print(nombre.upper())
    elif opcion == "2":
        print(nombre.lower())
    elif opcion == "3":
        print(nombre.title())
    else:
        print("Opción no válida")


def ejercicio9():
   
    magnitud = float(input("Ingrese la magnitud del terremoto: "))
    if magnitud < 3:
        print("Muy leve (imperceptible)")
    elif magnitud < 4:
        print("Leve (ligeramente perceptible)")
    elif magnitud < 5:
        print("Moderado (sentido por personas, pero generalmente no causa daños)")
    elif magnitud < 6:
        print("Fuerte (puede causar daños en estructuras débiles)")
    elif magnitud < 7:
        print("Muy Fuerte (puede causar daños significativos)")
    else:
        print("Extremo (puede causar graves daños a gran escala)")


def ejercicio10():
    
    hemi = input("Ingrese el hemisferio (N para norte, S para sur): ").strip().upper()
    mes = int(input("Ingrese el mes (1-12): "))
    dia = int(input("Ingrese el día: "))

    if hemi not in ("N", "S"):
        print("Hemisferio no válido. Debe ser 'N' o 'S'.")
        return

    if hemi == "N":
        if (mes == 12 and dia >= 21) or (mes in (1, 2)) or (mes == 3 and dia <= 20):
            estacion = "Invierno"
        elif (mes == 3 and dia >= 21) or (mes in (4, 5)) or (mes == 6 and dia <= 20):
            estacion = "Primavera"
        elif (mes == 6 and dia >= 21) or (mes in (7, 8)) or (mes == 9 and dia <= 20):
            estacion = "Verano"
        elif (mes == 9 and dia >= 21) or (mes in (10, 11)) or (mes == 12 and dia <= 20):
            estacion = "Otoño"
        else:
            estacion = "Fecha no válida"
    else:
        if (mes == 12 and dia >= 21) or (mes in (1, 2)) or (mes == 3 and dia <= 20):
            estacion = "Verano"
        elif (mes == 3 and dia >= 21) or (mes in (4, 5)) or (mes == 6 and dia <= 20):
            estacion = "Otoño"
        elif (mes == 6 and dia >= 21) or (mes in (7, 8)) or (mes == 9 and dia <= 20):
            estacion = "Invierno"
        elif (mes == 9 and dia >= 21) or (mes in (10, 11)) or (mes == 12 and dia <= 20):
            estacion = "Primavera"
        else:
            estacion = "Fecha no válida"
    
    print("La estación es:", estacion)



