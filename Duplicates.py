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

def encontrar_duplicados(arreglo):
    elementos_unicos = set()
    duplicados = set()

    for elemento in arreglo:
        if elemento in elementos_unicos:
            duplicados.add(elemento)
        else:
            elementos_unicos.add(elemento)

    return list(duplicados)

valor_maximo = int(input("Ingrese el valor máximo para los números aleatorios: "))

arreglo = generar_arreglo(valor_maximo)
print("Arreglo original:")
imprimir_arreglo(arreglo)

def ordenar_arreglo(arreglo):
    arreglo.sort()
    return arreglo

arreglo_ordenado = ordenar_arreglo(arreglo)
print("Arreglo ordenado:")
imprimir_arreglo(arreglo_ordenado)

duplicados = encontrar_duplicados(arreglo)
if len(duplicados) > 0:
    print(f"\nElementos duplicados encontrados: {duplicados}")
else:
    print("\nNo se encontraron elementos duplicados en el arreglo.")

inicio = time.time()
arreglo = generar_arreglo(valor_maximo)
fin = time.time()
duracion = fin - inicio
print(f"El tiempo de ejecucion fue de {duracion} segundos")
