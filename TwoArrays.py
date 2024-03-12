import random
import time

def generar_arreglo(tamano):
    arreglo = []
    for i in range(tamano):
        numero = random.randint(1, valor_maximo)
        arreglo.append(numero)
    return arreglo

def imprimir_arreglo(arreglo):
    texto = ", ".join(str(x) for x in arreglo)
    print(texto)

def buscar_secuencial(arreglo, elemento):
    for i, x in enumerate(arreglo):
        if x == elemento:
            return i
    return -1

valor_maximo = int(input("Ingrese el valor máximo para los números aleatorios: "))
elemento = int(input("Ingrese el elemento a buscar: "))

print("-" * 50)

arreglo = generar_arreglo(valor_maximo)
print("Arreglo A:")
imprimir_arreglo(arreglo)

def ordenar_arreglo(arreglo):
    arreglo.sort()
    return arreglo

arreglo_ordenado = ordenar_arreglo(arreglo)
print("Arreglo ordenado:")
imprimir_arreglo(arreglo_ordenado)

indice = buscar_secuencial(arreglo, elemento)
if indice != -1:
    print(f"El elemento {elemento} se encontró en el arreglo")
else:
    print(f"El elemento {elemento} no se encontró en el arreglo")

print("-" * 50)

arregloB = generar_arreglo(valor_maximo)
print("Arreglo B:")
imprimir_arreglo(arregloB)

def ordenar_arreglo(arregloB):
    arregloB.sort()
    return arregloB

arreglo_ordenado = ordenar_arreglo(arregloB)
print("Arreglo ordenado:")
imprimir_arreglo(arreglo_ordenado)

indice = buscar_secuencial(arregloB, elemento)
if indice != -1:
    print(f"El elemento {elemento} se encontró en el arreglo")
else:
    print(f"El elemento {elemento} no se encontró en el arreglo")

inicio = time.time()
arreglo = generar_arreglo(valor_maximo)
arregloB = generar_arreglo(valor_maximo)
buscar_secuencial(arreglo, elemento)
arreglo_ordenado = ordenar_arreglo(arreglo)
buscar_secuencial(arreglo_ordenado, elemento)
fin = time.time()
duracion = fin - inicio
print("-" * 50)
print(f"El tiempo de ejecucion fue de {duracion} segundos")
