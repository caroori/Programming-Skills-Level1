import time
import sys
import os

opcion = 0

#diccionario
jugadores = {
    8: {"nombre": "Bruno Fernandes", "goles": 5, "velocidad": 6, "asistencias": 9, "precision_pases": 10, "involucramientos_defensivos": 3},
    11: {"nombre": "Rasmus Hojlund", "goles": 12, "velocidad": 8, "asistencias": 2, "precision_pases": 6, "involucramientos_defensivos": 2},
    5: {"nombre": "Harry Maguire", "goles": 1, "velocidad": 5, "asistencias": 1, "precision_pases": 7, "involucramientos_defensivos": 9},
    17: {"nombre": "Alejandro Garnacho", "goles": 8, "velocidad": 7, "asistencias": 8, "precision_pases": 6, "involucramientos_defensivos": 0},
    7: {"nombre": "Mason Mount", "goles": 2, "velocidad": 6, "asistencias": 4, "precision_pases": 8, "involucramientos_defensivos": 1}
}


################## F U N C I O N E S ##################

def menu():  ##siempre ingresando el numero **
    print("1. Revision de jugador")  ## ** muestra datos
    print("2. Comparar dos jugadores") # **
    print("3. Jugador más rápido")  
    print("4. Máximo goleador")
    print("5. Jugador con mas asistencias")
    print("6. Jugador con mayor precisión de pases")
    print("7. Jugador con más involucramientos defensivos")

#### CONSOLA
def limpiar_consola():
    sistema_operativo = os.name
    if sistema_operativo == 'posix':  # Linux y macOS
        os.system('clear')
    elif sistema_operativo == 'nt':   # Windows
        os.system('cls')

##### casos ####
def revision(numero_camiseta):  ### tira los datos del jugador
    jugador = jugadores.get(numero_camiseta)
    if jugador:
        print("Nombre: ", jugador["nombre"])
        print("Cantidad de goles: ", jugador["goles"])
        print("Velocidad: ", jugador["velocidad"])
        print("Asistencias: ", jugador["asistencias"])
        print("Precision de pases: ", jugador["precision_pases"])
        print("Involucramientos defensivos: ", jugador["involucramientos_defensivos"])

def comparar_jugadores(numero1_camiseta, numero2_camiseta):
    jugador1 = jugadores.get(numero1_camiseta)
    jugador2 = jugadores.get(numero2_camiseta)
    print(f"Nombres: {jugador1['nombre']} -- {jugador2['nombre']}")
    print(f"Goles: {jugador1['goles']} - {jugador2['goles']}")   
    print(f"Velocidades: {jugador1['velocidad']} - {jugador2['velocidad']}")  
    print(f"Asistencias: {jugador1['asistencias']} - {jugador2['asistencias']}")
    print(f"Precision de pases: {jugador1['precision_pases']} - {jugador2['precision_pases']}")
    print(f"Involucramientos defensivos: {jugador1['involucramientos_defensivos']} - {jugador2['involucramientos_defensivos']}")
    print(" ")

############# ORDEN  #############
def orden_burbuja(jugadores, tipo):
    n = len(jugadores)
    for i in range(n):
        for j in range(0, n-i-1):
            if jugadores[j][tipo] < jugadores[j+1][tipo]:
                jugadores[j], jugadores[j+1] = jugadores[j+1], jugadores[j]
    return jugadores[0] ##solo muestra el primero

############# CAMISETA NO ENCONTRADA  #############
def camiseta_existe(numero):
    if numero not in jugadores:
        print("Camiseta no encontrada...")
        time.sleep(1.5)
        limpiar_consola()
        return False ##indica que no existe
    return True ##indica que existe


################# F I N   F U N C I O N E S  ##################

while True:
    menu()
    opcion = int(input("Seleccione una opcion: "))
    limpiar_consola()

    if opcion == 1:
        numero_camiseta = int(input("Ingrese el número de camiseta del jugador: "))
        if camiseta_existe(numero_camiseta):
            revision(numero_camiseta)
        print(" ")

    elif opcion == 2:
        numero1_camiseta = int(input("Ingrese el numero de la camiseta del primer jugador: "))      
        numero2_camiseta = int(input("Ingrese el numero de camiseta del segundo jugador: "))
        if camiseta_existe(numero1_camiseta) and camiseta_existe(numero2_camiseta):
            limpiar_consola()
            comparar_jugadores(numero1_camiseta, numero2_camiseta)
        print(" ")

    elif opcion == 3:
        print("El jugador más rapido es: ")
        mas_velocidad = orden_burbuja(list(jugadores.values()), "velocidad")
        print(f"Nombre: {mas_velocidad['nombre']}")
        print(f"Con una velocidad de: {mas_velocidad['velocidad']}")
        print(" ")

    elif opcion == 4:
        print("El jugador con mas goles es: ")
        mas_goles = orden_burbuja(list(jugadores.values()), "goles")
        print(f"Nombre: {mas_goles['nombre']}")
        print(f"Cantidad de goles: {mas_goles['goles']}")
        print(" ")

    elif opcion == 5:
        print("El jugador con más asistencias es: ")
        mas_asistencias = orden_burbuja(list(jugadores.values()), "asistencias")
        print(f"Nombre: {mas_asistencias['nombre']}")
        print(f"Cantidad de asistencias: {mas_asistencias['asistencias']}")
        print(" ")

    elif opcion == 6:
        print("El jugador con mayor precision de pases es: ")
        mas_precision = orden_burbuja(list(jugadores.values()), "precision_pases")
        print(f"Nombre: {mas_precision['nombre']}")
        print(f"Cantidad de precision de pases: {mas_precision['precision_pases']}")
        print(" ")

    elif opcion == 7:
        print("El jugador con más involucramientos defensivos es: ")
        mas_involucramiento = orden_burbuja(list(jugadores.values()), "involucramientos_defensivos")
        print(f"Nombre: {mas_involucramiento['nombre']}")
        print(f"Cantidad de involucramientos defensivos : {mas_involucramiento['involucramientos_defensivos']}")
        print(" ")
    
    else:
        print("Esa opcion no existe")
        time.sleep(1.5)
        limpiar_consola()
