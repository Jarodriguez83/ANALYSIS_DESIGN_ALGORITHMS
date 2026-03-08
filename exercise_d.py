# ------------------------------------------------------------
# PROGRAMA: ANALISIS DE NUMEROS SEGUN SUS DIVISORES PROPIOS
# ------------------------------------------------------------
# ESTE PROGRAMA LEE UN NUMERO ENTERO POSITIVO N INGRESADO
# POR EL USUARIO Y ANALIZA TODOS LOS NUMEROS DESDE 1 HASTA N.
#
# PARA CADA NUMERO n:
# - CALCULA SUS DIVISORES PROPIOS (DIVISORES POSITIVOS < n)
# - CALCULA LA SUMA DE ESOS DIVISORES s(n)
# - CLASIFICA EL NUMERO COMO:
#       PERFECTO    SI s(n) = n
#       DEFICIENTE  SI s(n) < n
#       ABUNDANTE   SI s(n) > n
#
# ADEMAS:
# - MUESTRA LOS DIVISORES DE CADA NUMERO
# - BUSCA TODOS LOS PARES DE NUMEROS AMIGOS (a,b)
# - IMPRIME LOS NUMEROS PERFECTOS ENCONTRADOS
# - IMPRIME LA CANTIDAD DE NUMEROS DEFICIENTES,
#   PERFECTOS Y ABUNDANTES
# - IMPRIME LOS PARES DE NUMEROS AMIGOS
# ------------------------------------------------------------

# FUNCION PARA CALCULAR LOS DIVISORES PROPIOS DE UN NUMERO
def divisores_propios(n):
    divisores = []
    for i in range(1, n):
        if n % i == 0:
            divisores.append(i)
    return divisores


# FUNCION PARA CALCULAR LA SUMA DE DIVISORES PROPIOS
def suma_divisores(n):
    divisores = divisores_propios(n)
    return sum(divisores)


# LECTURA DEL NUMERO N
N = int(input("INGRESE UN NUMERO ENTERO POSITIVO N: "))

# CONTADORES
cantidad_deficientes = 0
cantidad_perfectos = 0
cantidad_abundantes = 0

# LISTA PARA GUARDAR NUMEROS PERFECTOS
numeros_perfectos = []

# DICCIONARIO PARA GUARDAR s(n)
sumas = {}

print("\nANALISIS DE NUMEROS\n")

# RECORRER NUMEROS DESDE 1 HASTA N
for n in range(1, N + 1):

    divisores = divisores_propios(n)
    s = sum(divisores)

    # GUARDAR LA SUMA PARA BUSCAR NUMEROS AMIGOS
    sumas[n] = s

    # MOSTRAR DIVISORES
    print("NUMERO:", n)
    print("DIVISORES PROPIOS:", divisores)
    print("SUMA DE DIVISORES:", s)

    # CLASIFICACION
    if s == n:
        print("CLASIFICACION: PERFECTO\n")
        cantidad_perfectos += 1
        numeros_perfectos.append(n)

    elif s < n:
        print("CLASIFICACION: DEFICIENTE\n")
        cantidad_deficientes += 1

    else:
        print("CLASIFICACION: ABUNDANTE\n")
        cantidad_abundantes += 1


# BUSQUEDA DE NUMEROS AMIGOS
pares_amigos = []

for a in range(1, N + 1):
    b = sumas[a]

    if b > a and b <= N:
        if sumas.get(b, 0) == a:
            pares_amigos.append((a, b))


# RESULTADOS FINALES
print("--------------------------------------------------")
print("RESULTADOS FINALES")
print("--------------------------------------------------")

print("NUMEROS PERFECTOS ENCONTRADOS:")
print(numeros_perfectos)

print("\nCANTIDAD DE NUMEROS:")
print("DEFICIENTES:", cantidad_deficientes)
print("PERFECTOS:", cantidad_perfectos)
print("ABUNDANTES:", cantidad_abundantes)

print("\nPARES DE NUMEROS AMIGOS ENCONTRADOS:")
if len(pares_amigos) == 0:
    print("NO SE ENCONTRARON PARES AMIGOS")
else:
    for par in pares_amigos:
        print(par)