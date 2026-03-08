# IMPORTA LA LIBRERIA RANDOM PARA GENERAR NUMEROS ALEATORIOS
import random


# FUNCION QUE VERIFICA SI UN NUMERO TIENE DIGITOS REPETIDOS
def tiene_repetidos(numero):

    # CONVIERTE EL NUMERO EN TEXTO PARA PODER RECORRER CADA DIGITO
    texto = str(numero)

    # COMPARA CADA DIGITO CON LOS DEMAS
    for i in range(len(texto)):
        for j in range(i + 1, len(texto)):

            # SI DOS DIGITOS SON IGUALES SIGNIFICA QUE HAY REPETIDOS
            if texto[i] == texto[j]:
                return True

    return False


# FUNCION QUE GENERA EL CODIGO SECRETO SIN DIGITOS REPETIDOS
def generar_codigo(longitud):

    # BUCLE QUE INTENTA GENERAR NUMEROS HASTA ENCONTRAR UNO VALIDO
    while True:

        # GENERA UN NUMERO ALEATORIO CON LA LONGITUD INDICADA
        minimo = 10 ** (longitud - 1)
        maximo = (10 ** longitud) - 1

        numero = random.randint(minimo, maximo)

        # VERIFICA QUE EL NUMERO NO TENGA DIGITOS REPETIDOS
        if not tiene_repetidos(numero):
            return str(numero)


# FUNCION QUE CALCULA LAS PICAS Y FIJAS
def calcular_picas_fijas(secreto, intento):

    fijas = 0
    picas = 0

    # RECORRE CADA POSICION DEL NUMERO
    for i in range(len(secreto)):

        # SI EL DIGITO ES IGUAL Y ESTA EN LA MISMA POSICION ES FIJA
        if intento[i] == secreto[i]:
            fijas = fijas + 1

        else:

            # SI EL DIGITO EXISTE EN EL CODIGO PERO EN OTRA POSICION ES PICA
            for j in range(len(secreto)):
                if intento[i] == secreto[j]:
                    picas = picas + 1

    return fijas, picas

print("====================================")
print("BIENVENIDO AL JUEGO PICAS Y FIJAS")
print("====================================")

print("REGLAS DEL JUEGO")
print("1. EL COMPUTADOR GENERA UN CODIGO SECRETO.")
print("2. EL CODIGO TIENE DIGITOS SIN REPETIR.")
print("3. EL JUGADOR DEBE ADIVINAR EL CODIGO.")
print("4. DESPUES DE CADA INTENTO SE CALCULAN:")
print("   - FIJAS: DIGITOS CORRECTOS EN LA POSICION CORRECTA.")
print("   - PICAS: DIGITOS CORRECTOS PERO EN POSICION DIFERENTE.")
print("5. EL JUGADOR TIENE MAXIMO 10 INTENTOS.")
print("6. SI TODAS LAS POSICIONES SON FIJAS EL JUGADOR GANA.")
print("====================================\n")


# SOLICITA AL USUARIO LA LONGITUD DEL CODIGO
L = int(input("INGRESE LA LONGITUD DEL CODIGO SECRETO: "))

# GENERA EL CODIGO SECRETO
codigo_secreto = generar_codigo(L)

# NUMERO MAXIMO DE INTENTOS
MAX_INTENTOS = 10

print("\nEL CODIGO SECRETO HA SIDO GENERADO")
print("DEBE ADIVINAR UN NUMERO DE", L, "DIGITOS SIN REPETIR\n")

# CONTADOR DE INTENTOS
intento_actual = 0


# BUCLE PRINCIPAL DEL JUEGO
while intento_actual < MAX_INTENTOS:

    intento_actual = intento_actual + 1

    print("-----------------------------------")
    print("INTENTO NUMERO:", intento_actual)

    intento = input("INGRESE SU INTENTO: ")

    # VERIFICA QUE EL INTENTO TENGA LA LONGITUD CORRECTA
    if len(intento) != L:
        print("EL NUMERO DE DIGITOS ES INCORRECTO")
        intento_actual = intento_actual - 1
        continue

    # VERIFICA QUE NO TENGA DIGITOS REPETIDOS
    if tiene_repetidos(intento):
        print("EL NUMERO TIENE DIGITOS REPETIDOS")
        intento_actual = intento_actual - 1
        continue

    # CALCULA LAS PICAS Y LAS FIJAS
    fijas, picas = calcular_picas_fijas(codigo_secreto, intento)

    print("INTENTO:", intento, "→", fijas, "FIJAS,", picas, "PICAS")

    # VERIFICA SI EL JUGADOR GANO
    if fijas == L:
        print("\nFELICIDADES")
        print("USTED ADIVINO EL CODIGO SECRETO")
        break


# SI SE ACABAN LOS INTENTOS EL JUGADOR PIERDE
if intento_actual == MAX_INTENTOS and fijas != L:

    print("\nSE ACABARON LOS INTENTOS")
    print("EL JUGADOR PERDIO")


# MUESTRA EL CODIGO SECRETO AL FINAL DEL JUEGO
print("EL CODIGO SECRETO ERA:", codigo_secreto)