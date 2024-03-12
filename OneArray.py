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

valor_maximo = int(input("Ingrese el valor maximo para los numeros aleatorios: "))
elemento = int(input("Ingrese el elemento a buscar: "))

arreglo = generar_arreglo(valor_maximo)
print("Arreglo original:")
imprimir_arreglo(arreglo)

def ordenar_arreglo(arreglo):
    arreglo.sort()
    return arreglo

arreglo_ordenado = ordenar_arreglo(arreglo)
print("Arreglo ordenado:")
imprimir_arreglo(arreglo_ordenado)

indice = buscar_secuencial(arreglo, elemento)
if indice != -1:
    print(f"El elemento {elemento} se encontro en el arreglo")
else:
    print(f"El elemento {elemento} no se encontro en el arreglo")

inicio = time.time()
arreglo = generar_arreglo(valor_maximo)
fin = time.time()
duracion = fin - inicio
print(f"El tiempo de ejecucion fue de {duracion} segundos")
