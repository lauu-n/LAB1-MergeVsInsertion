import random
import time
import matplotlib.pyplot as plt

# DEFINIR MERGE SORT
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

# DEFINIR INSERTION SORT
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Valores de n
valores_n = [1000, 10000, 100000, 1000000, 10000000]

# Listas para guardar tiempos
tiempos_merge = []
tiempos_insertion = []

# ~ PRUEBA ~
print("\nMERGE SORT vs INSERTION SORT")

# PRUEBA MERGE SORT
print("\n~ MERGE SORT ~")
print("n | tiempo (segundos)")
print("----------------------")

for n in valores_n:
    arreglo = [random.randint(1, 100000) for _ in range(n)]
    inicio = time.time()
    merge_sort(arreglo)
    fin = time.time()
    tiempo = fin - inicio
    tiempos_merge.append(tiempo)
    print(n, "|", tiempo)

# PRUEBA INSERTION SORT
print("\n~ INSERTION SORT ~")
print("n | tiempo (segundos)")
print("----------------------")

for n in valores_n:
    arreglo = [random.randint(1, 100000) for _ in range(n)]
    inicio = time.time()
    insertion_sort(arreglo)
    fin = time.time()
    tiempo = fin - inicio
    tiempos_insertion.append(tiempo)
    print(n, "|", tiempo)


# GRAFICA MERGE SORT
plt.figure()
plt.plot(valores_n, tiempos_merge, marker='o')
plt.title("Tiempo de ejecución - Merge Sort")
plt.xlabel("Tamaño del arreglo (n)")
plt.ylabel("Tiempo (segundos)")
plt.grid(True)
plt.show()


# GRAFICA INSERTION SORT
plt.figure()
plt.plot(valores_n, tiempos_insertion, marker='o')
plt.title("Tiempo de ejecución - Insertion Sort")
plt.xlabel("Tamaño del arreglo (n)")
plt.ylabel("Tiempo (segundos)")
plt.grid(True)
plt.show()
