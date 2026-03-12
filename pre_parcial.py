import time
import matplotlib.pyplot as plt

# -----------------------------
# Metodo 1: Sin formula (bucle)
# -----------------------------
def gauss_iterativo(n):
    suma = 0
    for i in range(1, n + 1):
        suma += i
    return suma


# -----------------------------
# Metodo 2: Con formula de Gauss
# -----------------------------
def gauss_formula(n):
    return n * (n + 1) // 2


# -----------------------------
# Valores de prueba
# -----------------------------
valores_n = [10, 100, 1000, 5000, 10000, 20000, 40000]

tiempos_iterativo = []
tiempos_formula = []


# -----------------------------
# Benchmarking
# -----------------------------
for n in valores_n:

    inicio = time.perf_counter()
    gauss_iterativo(n)
    fin = time.perf_counter()
    tiempos_iterativo.append(fin - inicio)

    inicio = time.perf_counter()
    gauss_formula(n)
    fin = time.perf_counter()
    tiempos_formula.append(fin - inicio)


# -----------------------------
# Mostrar resultados
# -----------------------------
print("Resultados de Benchmarking:\n")

for i in range(len(valores_n)):
    print(f"n = {valores_n[i]}")
    print(f"Iterativo: {tiempos_iterativo[i]:.8f} segundos")
    print(f"Formula:   {tiempos_formula[i]:.8f} segundos")
    print()


# -----------------------------
# Grafica
# -----------------------------
plt.figure()

plt.plot(valores_n, tiempos_iterativo, marker='o', label="Iterativo O(n)")
plt.plot(valores_n, tiempos_formula, marker='o', label="Formula O(1)")

plt.xlabel("Tamaño del problema (n)")
plt.ylabel("Tiempo de ejecución (segundos)")
plt.title("Benchmark: Suma Iterativa vs Formula de Gauss")

plt.legend()
plt.grid(True)

plt.show()