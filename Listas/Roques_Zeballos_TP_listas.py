#ejercicio1
lista = ["a", "b", "c", "d"]
print(lista[-2])  
# ejercicio2
lista = []
lista.append("Hola")
lista.append("Mundo")
print(lista)  
# ejercicio3
lista = []
lista.append("Hola")
lista.append("Mundo")
print(lista)  
#ejercicio4
animales = ["perro", "gato", "conejo", "pez"]
animales[1] = "loro"
animales[-1] = "oso"
#ejercicio5
numeros = [8, 15, 3, 22, 7]
numeros.remove(max(numeros))  
print(numeros)  
#ejrcicio6
lista = list(range(10, 31, 5))  
print(lista[:2]) 
 #ejercicio7
autos = ["sedan", "polo", "suran", "gol"]
autos[1:3] = ["nuevo1", "nuevo2"] 
# ejercicio8
dobles = []
dobles.append(5 * 2)
dobles.append(10 * 2)
print(dobles)  
#ejercicio9
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
compras[2].append("jugo")  
compras[1][1] = "tallarines"  
compras[0].remove("pan")  
#ejercicio10
lista_anidada = [
    15,
    True,
    [25.5, 57.9, 30.6],
    False
]