import random
import cProfile
import pstats


# ---------------------------------
# MERGE SORT
# ---------------------------------

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    medio = len(arr) // 2
    izquierda = merge_sort(arr[:medio])
    derecha = merge_sort(arr[medio:])

    return merge(izquierda, derecha)


def merge(izq, der):
    resultado = []
    i = 0
    j = 0

    while i < len(izq) and j < len(der):

        if izq[i] < der[j]:
            resultado.append(izq[i])
            i += 1
        else:
            resultado.append(der[j])
            j += 1

    resultado.extend(izq[i:])
    resultado.extend(der[j:])

    return resultado


# ---------------------------------
# QUICK SORT
# ---------------------------------

def quick_sort(arr):

    if len(arr) <= 1:
        return arr

    pivote = arr[len(arr) // 2]

    menores = [x for x in arr if x < pivote]
    iguales = [x for x in arr if x == pivote]
    mayores = [x for x in arr if x > pivote]

    return quick_sort(menores) + iguales + quick_sort(mayores)


# ---------------------------------
# GENERAR DATOS
# ---------------------------------

def generar_arreglo(n):
    return [random.randint(0, 100000) for _ in range(n)]


# ---------------------------------
# FUNCIONES PARA PERFILAR
# ---------------------------------

def probar_merge():
    arr = generar_arreglo(10000)
    merge_sort(arr)


def probar_quick():
    arr = generar_arreglo(10000)
    quick_sort(arr)


# ---------------------------------
# PROFILING
# ---------------------------------

print("Profiling Merge Sort...")
cProfile.run("probar_merge()", "merge_stats")

print("\nProfiling Quick Sort...")
cProfile.run("probar_quick()", "quick_stats")


# ---------------------------------
# MOSTRAR RESULTADOS
# ---------------------------------

print("\nResultados Merge Sort")
stats = pstats.Stats("merge_stats")
stats.sort_stats("time").print_stats(10)

print("\nResultados Quick Sort")
stats = pstats.Stats("quick_stats")
stats.sort_stats("time").print_stats(10)