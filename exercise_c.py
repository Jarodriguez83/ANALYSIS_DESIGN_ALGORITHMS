import cProfile
# FUNCION PARA ORDENAR LAS DENOMINACIONES DE MAYOR A MENOR
def ordenar_lista(lista):
    # METODO SIMPLE DE ORDENAMIENTO TIPO BURBUJA
    for i in range(len(lista)):
        for j in range(len(lista) - 1):
            if lista[j] < lista[j + 1]:
                temp = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = temp

    return lista
def main():
    print("\n SISTEMA DE CAMBIO PARA CAJERO")
    print(" - REGLAS DEL PROGRAMA:")
    print("1. EL USUARIO INGRESA EL VALOR DE LA COMPRA.")
    print("2. EL USUARIO INGRESA CON CUANTO DINERO PAGA.")
    print("3. EL SISTEMA CALCULA EL CAMBIO A ENTREGAR.")
    print("4. EXISTEN DENOMINACIONES DE MONEDAS Y BILLETES.")
    print("5. PARA CADA DENOMINACION SE INDICA CUANTAS UNIDADES HAY.")
    print("6. EL PROGRAMA INTENTA DAR EL CAMBIO CON EL MENOR")
    print("   NUMERO POSIBLE DE BILLETES Y MONEDAS.")
    print("7. SI NO HAY SUFICIENTE DINERO PARA EL CAMBIO")
    print("   EL SISTEMA MOSTRARA QUE NO ES POSIBLE.")

    compra = int(input("\n - INGRESE EL VALOR DE LA COMPRA: "))
    pago = int(input(" - INGRESE EL VALOR CON EL QUE PAGA EL CLIENTE: "))

    V = pago - compra # CALCULA EL CAMBIO

    # VERIFICA SI EL PAGO ES SUFICIENTE
    if V < 0:

        print("ALERTA: EL PAGO NO ES SUFICIENTE PARA LA COMPRA")
        exit()

    print("\n   - EL CAMBIO A ENTREGAR ES:", V)
    #INGRESA LAS DENOMINACIONES DE MONEDAS
    entrada_monedas = input("\n - INGRESE LAS DENOMINACIONES DE MONEDAS SEPARADAS POR ESPACIO: ")
    partes_monedas = entrada_monedas.split()
    DM = []
    cant_monedas = {}
    # GUARDA LAS DENOMINACIONES
    for p in partes_monedas:
        DM.append(int(p))
    # PREGUNTA CUANTAS MONEDAS HAY DE CADA TIPO
    for d in DM:
        cantidad = int(input("CUANTAS MONEDAS HAY DE " + str(d) + ": "))
        cant_monedas[d] = cantidad

    #INGRESA LAS DENOMINACIONES DE BILLETES
    entrada_billetes = input("\n - INGRESE LAS DENOMINACIONES DE BILLETES SEPARADAS POR ESPACIO: ")
    partes_billetes = entrada_billetes.split()
    DB = []
    cant_billetes = {}
    # GUARDA LAS DENOMINACIONES
    for p in partes_billetes:
        DB.append(int(p))
    # PREGUNTA CUANTOS BILLETES HAY DE CADA TIPO
    for d in DB:
        cantidad = int(input("CUANTOS BILLETES HAY DE " + str(d) + ": "))
        cant_billetes[d] = cantidad

    denominaciones = []

    # AGREGA BILLETES
    for d in DB:
        denominaciones.append(d)

    # AGREGA MONEDAS
    for d in DM:
        denominaciones.append(d)

    # ORDENA DE MAYOR A MENOR
    denominaciones = ordenar_lista(denominaciones)

    #CALCULA EL CAMBIO A ENTREGAR CON EL MENOR NUMERO DE DENOMINACIONES POSIBLE
    valor_restante = V
    total_piezas = 0
    resultado = {}

    for d in denominaciones:
        # VERIFICA SI ES BILLETE O MONEDA
        if d in cant_billetes:
            disponible = cant_billetes[d]
        else:
            disponible = cant_monedas[d]
        # CALCULA CUANTOS SE NECESITAN
        necesarios = valor_restante // d
        # LIMITA POR LA CANTIDAD DISPONIBLE
        usar = min(necesarios, disponible)
        resultado[d] = usar
        valor_restante = valor_restante - (usar * d)
        total_piezas = total_piezas + usar

    if valor_restante != 0:

        print("\n ALERTA: NO ES POSIBLE ENTREGAR EL CAMBIO EXACTO")
        print(" ALERTA: NO HAY SUFICIENTES MONEDAS O BILLETES")

    else:

        print("\n   CAMBIO ENTREGADO CORRECTAMENTE.")

        print(" - CAMBIO TOTAL:", V)
        print(" - NUMERO MINIMO DE DENOMINACIONES USADAS:", total_piezas)

        print("\nDETALLE DEL CAMBIO:")

        for d in resultado:
            if resultado[d] > 0:
                print(" -", resultado[d], " - DENOMINACIONES DE", d)

cProfile.run('main()')