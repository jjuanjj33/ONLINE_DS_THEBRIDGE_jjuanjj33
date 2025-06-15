import random
from utils import crea_tablero, crea_barcos_manual, crea_barco_aleatorio, recibir_disparo_rival, recibir_mi_disparo


# Creamos mi tablero vacío.
mi_tablero_vacio = crea_tablero(10)
# print("Este es el tablero vacío\n",mi_tablero_vacio,"\n", "*"*42)


# Creamos el tablero vacío del rival.
tablero_rival_vacio = crea_tablero(10)


# Creación y colocación de mis barcos.
# Condición si quiero que la máquina los elija por mí o si quiero elegir yo.
while True:
    eleccion_propia = input("¿Quieres colocar tu barcos de forma aleatoria (S/N): ")
    if eleccion_propia.upper() == "S":
        mi_tablero_barcos = crea_barco_aleatorio(mi_tablero_vacio, eslora = 2)
        mi_tablero_barcos = crea_barco_aleatorio(mi_tablero_vacio, eslora = 2)
        mi_tablero_barcos = crea_barco_aleatorio(mi_tablero_vacio, eslora = 2)
        mi_tablero_barcos = crea_barco_aleatorio(mi_tablero_vacio, eslora = 3)
        mi_tablero_barcos = crea_barco_aleatorio(mi_tablero_vacio, eslora = 3)
        mi_tablero_barcos = crea_barco_aleatorio(mi_tablero_vacio, eslora = 4)
        print("\nEste es mi tablero con mis barcos dispuestos aleatoriamente\n", mi_tablero_barcos,"\n","*"*42)
        print("\nEste es el tablero rival en el que tendrás que apuntar tus disparos\n", tablero_rival_vacio,"\n","*"*42)
        break
    elif eleccion_propia.upper() == "N":
        mi_tablero_barcos = crea_barcos_manual(mi_tablero_vacio, eslora = 2)
        mi_tablero_barcos = crea_barcos_manual(mi_tablero_vacio, eslora = 2)
        mi_tablero_barcos = crea_barcos_manual(mi_tablero_vacio, eslora = 2)
        mi_tablero_barcos = crea_barcos_manual(mi_tablero_vacio, eslora = 3)
        mi_tablero_barcos = crea_barcos_manual(mi_tablero_vacio, eslora = 3)
        mi_tablero_barcos = crea_barcos_manual(mi_tablero_vacio, eslora = 4)
        print("\nEste es mi tablero con mis barcos dispuestos manualmente\n", mi_tablero_barcos,"\n","*"*42)
        print("\nEste es el tablero rival en el que tendrás que apuntar tus disparos\n", tablero_rival_vacio,"\n","*"*42)
        break
    else:
        continue


# Creación y colocación aleatoria de los barcos del rival.
tablero_rival_barcos = crea_barco_aleatorio(tablero_rival_vacio, eslora = 2)
tablero_rival_barcos = crea_barco_aleatorio(tablero_rival_vacio, eslora = 2)
tablero_rival_barcos = crea_barco_aleatorio(tablero_rival_vacio, eslora = 2)
tablero_rival_barcos = crea_barco_aleatorio(tablero_rival_vacio, eslora = 3)
tablero_rival_barcos = crea_barco_aleatorio(tablero_rival_vacio, eslora = 3)
tablero_rival_barcos = crea_barco_aleatorio(tablero_rival_vacio, eslora = 4)
# print("\nEste es el tablero rival con los barcos dispuestos aleatoriamente\n", tablero_rival_barcos,"\n","*"*42)


# Hacemos un bucle para definir los diferentes turnos de juego.
# Vamos a realizar un bucle while hasta que no queden piezas en el tablero.
# Definimos los impactos como 0 al principio.
impactos_rival = 0
mis_impactos = 0
tablero_impacto_rival = crea_tablero(10)

while impactos_rival < 3 and mis_impactos < 3:
    # Definimos primero mis disparos.
    if impactos_rival < 3:
        mi_disparo = (int(input("Indica la 'Fila' de tu disparo: "))-1,int(input("Indica la 'Columna' de tu disparo: "))-1)
        print("Mi disparo es: ",mi_disparo)
        impactos_rival += recibir_mi_disparo(tablero_rival_barcos, mi_disparo, tablero_impacto_rival)
        
        if impactos_rival == 3:
            print("¡Te he hundido toda tu flota!")
            print("¡He ganado!")
            break

    # Definimos los disparos automaticos del rival.
    if mis_impactos < 3:
        disparo_rival = (random.randint(0,9),random.randint(0, 9))
        print("El disparo rival es: ",disparo_rival)
        mis_impactos += recibir_disparo_rival(mi_tablero_barcos, disparo_rival)
        
        if mis_impactos == 3:
            print("He perdido toda mi flota...")
            print("He perdido...")
            break
