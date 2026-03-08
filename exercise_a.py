# IMPORTA LA LIBRERIA RANDOM PARA GENERAR FICHAS ALEATORIAS
import random

# CONFIGURACION DEL JUEGO
TA = 4  # LIMITE MAXIMO DE FICHAS QUE PUEDE QUITAR EL JUGADOR A
TB = 5  # LIMITE MAXIMO DE FICHAS QUE PUEDE QUITAR EL JUGADOR B
MAX_JUGADAS = 10  # NUMERO MAXIMO DE JUGADAS PERMITIDAS


# FUNCION QUE CALCULA EL TOTAL DE FICHAS EN TODOS LOS GRUPOS
def total_fichas(grupos):
    total = 0
    for g in grupos:
        total = total + g
    return total


# FUNCION QUE VERIFICA SI TODOS LOS GRUPOS ESTAN VACIOS
def todos_vacios(grupos):
    for g in grupos:
        if g != 0:
            return False
    return True


# FUNCION QUE MUESTRA EL ESTADO ACTUAL DE LOS GRUPOS
def mostrar_grupos(grupos):

    print("\nESTADO ACTUAL DE LOS GRUPOS")

    # RECORRE CADA GRUPO Y MUESTRA SU CANTIDAD DE FICHAS
    for i in range(len(grupos)):
        print("GRUPO", i, "TIENE", grupos[i], "FICHAS")

    print("NUMERO DE GRUPOS:", len(grupos))
    print("TOTAL DE FICHAS:", total_fichas(grupos))


# SECCION DE REGLAS DEL JUEGO
print("===================================")
print("REGLAS DEL JUEGO")
print("===================================")
print("1. EXISTEN VARIOS GRUPOS DE FICHAS.")
print("2. CADA JUGADOR ELIGE UN GRUPO EN SU TURNO.")
print("3. EL JUGADOR A PUEDE QUITAR HASTA", TA, "FICHAS POR TURNO.")
print("4. EL JUGADOR B PUEDE QUITAR HASTA", TB, "FICHAS POR TURNO.")
print("5. GANA EL JUGADOR QUE QUITA LA ULTIMA FICHA.")
print("6. EL MAXIMO DE JUGADAS ES:", MAX_JUGADAS)
print("===================================\n")


# SOLICITA CUANTOS GRUPOS DE FICHAS QUIEREN LOS JUGADORES
num_grupos = int(input("CUANTOS GRUPOS DE FICHAS QUIEREN JUGAR: "))

# CREA LA LISTA DE GRUPOS
grupos = []

# GENERA ALEATORIAMENTE ENTRE 1 Y 20 FICHAS POR GRUPO
for i in range(num_grupos):
    fichas = random.randint(1, 20)
    grupos.append(fichas)

print("\nSE HAN GENERADO LOS GRUPOS ALEATORIAMENTE")

# MUESTRA EL ESTADO INICIAL DEL JUEGO
mostrar_grupos(grupos)

# VARIABLE QUE CONTROLA EL TURNO
turno = "A"

# CONTADOR DE JUGADAS
jugadas = 0

print("\nINICIO DEL JUEGO")

# BUCLE PRINCIPAL DEL JUEGO
while not todos_vacios(grupos) and jugadas < MAX_JUGADAS:

    print("\n-----------------------------------")
    print("TURNO DEL JUGADOR", turno)

    # DEFINE EL LIMITE SEGUN EL JUGADOR
    if turno == "A":
        limite = TA
    else:
        limite = TB

    print("PUEDE QUITAR ENTRE 1 Y", limite, "FICHAS")

    mostrar_grupos(grupos)

    # SOLICITA EL GRUPO QUE EL JUGADOR QUIERE MODIFICAR
    grupo = int(input("INGRESE EL NUMERO DEL GRUPO: "))

    # SOLICITA CUANTAS FICHAS DESEA QUITAR
    quitar = int(input("CUANTAS FICHAS DESEA QUITAR: "))

    # VERIFICA QUE EL GRUPO EXISTA
    if grupo < 0 or grupo >= len(grupos):
        print("GRUPO INVALIDO")
        continue

    # VERIFICA QUE EL GRUPO NO ESTE VACIO
    if grupos[grupo] == 0:
        print("ESE GRUPO ESTA VACIO")
        continue

    # VERIFICA QUE LA CANTIDAD ESTE DENTRO DEL LIMITE
    if quitar < 1 or quitar > limite:
        print("CANTIDAD FUERA DEL LIMITE PERMITIDO")
        continue

    # VERIFICA QUE HAYA SUFICIENTES FICHAS
    if quitar > grupos[grupo]:
        print("NO HAY SUFICIENTES FICHAS EN EL GRUPO")
        continue

    # REALIZA EL MOVIMIENTO RESTANDO LAS FICHAS
    grupos[grupo] = grupos[grupo] - quitar

    # AUMENTA EL CONTADOR DE JUGADAS
    jugadas = jugadas + 1

    # VERIFICA SI EL JUEGO TERMINO
    if todos_vacios(grupos):
        print("\nTODOS LOS GRUPOS QUEDARON VACIOS")
        print("EL GANADOR ES EL JUGADOR", turno)
        break

    # CAMBIA EL TURNO ENTRE LOS JUGADORES
    if turno == "A":
        turno = "B"
    else:
        turno = "A"


# MENSAJE SI SE ALCANZA EL LIMITE DE JUGADAS
if jugadas == MAX_JUGADAS:
    print("\nSE ALCANZO EL LIMITE MAXIMO DE JUGADAS")
    print("EL JUEGO TERMINA")