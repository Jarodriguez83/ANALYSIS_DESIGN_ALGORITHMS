# UTILIZAR PROFILING PARA LA MEDICIÓN DEL TIEMPO REAL DE UN PROGRAMA

import random #GENERAR FICHAS ALEATORIAMENTE

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
        print(" - GRUPO", i, "TIENE", grupos[i], "FICHAS")

    print("\n")
    print("NÚMERO DE GRUPOS:", len(grupos))
    print("TOTAL DE FICHAS EN JUEGO:", total_fichas(grupos))

print(" REGLAS DEL JUEGO")
print("1. EXISTEN VARIOS GRUPOS DE FICHAS.")
print("2. CADA JUGADOR ELIGE UN GRUPO EN SU TURNO.")
print("3. EL JUGADOR A PUEDE ELIMINAR HASTA", TA, "FICHAS POR TURNO.")
print("4. EL JUGADOR B PUEDE ELIMINAR HASTA", TB, "FICHAS POR TURNO.")
print("5. GANA EL JUGADOR QUE ELIMINA LA ULTIMA FICHA.")
print("6. EL MAXIMO DE JUGADAS ES:", MAX_JUGADAS)


# SOLICITA CUANTOS GRUPOS DE FICHAS QUIEREN LOS JUGADORES
num_grupos = int(input(" - CON CUANTOS GRUPOS DE FICHAS QUIEREN JUGAR: "))

# CREA LA LISTA DE GRUPOS
grupos = []

# GENERA ALEATORIAMENTE ENTRE 1 Y 20 FICHAS POR GRUPO
for i in range(num_grupos):
    fichas = random.randint(1, 20)
    grupos.append(fichas)

print("\nSE GENERARON LOS GRUPOS ALEATORIAMENTE")

# MUESTRA EL ESTADO INICIAL DEL JUEGO
mostrar_grupos(grupos)

turno = "A" #VARIABLE PARA EL TURNO
jugadas = 0 #CONTADOR DE JUGADAS

print("\n")
print(" INICIO DEL JUEGO")

while not todos_vacios(grupos) and jugadas < MAX_JUGADAS:

    print("\n")
    print("     TURNO PARA EL JUGADOR", turno)

    # DEFINE EL LIMITE SEGUN EL JUGADOR
    if turno == "A":
        limite = TA
    else:
        limite = TB

    print("PUEDE ELIMINAR ENTRE 1 Y", limite, "FICHAS")

    mostrar_grupos(grupos)

    # SOLICITA EL GRUPO QUE EL JUGADOR QUIERE MODIFICAR
    grupo = int(input(" - INGRESE EL NUMERO DEL GRUPO: "))

    # SOLICITA CUANTAS FICHAS DESEA QUITAR
    quitar = int(input(" - CUANTAS FICHAS DESEA ELIMINAR: "))

    # VERIFICA QUE EL GRUPO EXISTA
    if grupo < 0 or grupo >= len(grupos):
        print("ALERTA: ESTE GRUPO NO ES VÁLIDO")
        continue

    # VERIFICA QUE EL GRUPO NO ESTE VACIO
    if grupos[grupo] == 0:
        print("ALERTA: ESE GRUPO ESTA VACIO")
        continue

    # VERIFICA QUE LA CANTIDAD ESTE DENTRO DEL LIMITE
    if quitar < 1 or quitar > limite:
        print("ALERTA: CANTIDAD FUERA DEL LIMITE")
        continue

    # VERIFICA QUE HAYA SUFICIENTES FICHAS
    if quitar > grupos[grupo]:
        print("ALERTA: NO HAY SUFICIENTES FICHAS EN EL GRUPO")
        continue

    # REALIZA EL MOVIMIENTO RESTANDO LAS FICHAS
    grupos[grupo] = grupos[grupo] - quitar

    # AUMENTA EL CONTADOR DE JUGADAS
    jugadas = jugadas + 1

    # VERIFICA SI EL JUEGO TERMINO
    if todos_vacios(grupos):
        print("\nTODOS LOS GRUPOS QUEDARON VACIOS")
        print(" - EL GANADOR ES EL JUGADOR", turno)
        break

    # CAMBIA EL TURNO ENTRE LOS JUGADORES
    if turno == "A":
        turno = "B"
    else:
        turno = "A"


# MENSAJE SI SE ALCANZA EL LIMITE DE JUGADAS
if jugadas == MAX_JUGADAS:
    print("\n SE ALCANZO EL LIMITE MAXIMO DE JUGADAS")
    print("EL JUEGO HA TERMINADO SIN UN GANADOR DEFINIDO")