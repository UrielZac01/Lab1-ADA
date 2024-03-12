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

def encontrar_numeros_iguales(arreglo1, arreglo2):
    return list(set(arreglo1) & set(arreglo2))

valor_maximo = int(input("Ingrese el valor máximo para los números aleatorios: "))

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

print("-" * 50)

arregloB = generar_arreglo(valor_maximo)
print("Arreglo B:")
imprimir_arreglo(arregloB)

arregloB_ordenado = ordenar_arreglo(arregloB)
print("Arreglo ordenado:")
imprimir_arreglo(arregloB_ordenado)

print("-" * 50)

numeros_iguales = encontrar_numeros_iguales(arreglo, arregloB)

if len(numeros_iguales) > 0:
    print(f"\nNúmeros iguales encontrados: {numeros_iguales}")
else:
    print("\nNo se encontraron números iguales en ambos arreglos.")

inicio = time.time()
arreglo = generar_arreglo(valor_maximo)
arregloB = generar_arreglo(valor_maximo)
arreglo_ordenado = ordenar_arreglo(arreglo)
fin = time.time()
duracion = fin - inicio
print("-" * 50)
print(f"El tiempo de ejecucion fue de {duracion} segundos")
