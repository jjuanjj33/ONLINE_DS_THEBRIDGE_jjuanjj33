import numpy as np
import random


# Creación del tablero.
def crea_tablero(lado = 10):
    tablero = np.full((lado,lado)," ")
    return tablero


# Intenta colocar un barco aleatorio.
def coloca_barco(tablero_vacio, barco):
# Nos devuelve el tablero si puede colocar el barco, si no devuelve False, y avise por pantalla.
    num_max_filas = tablero_vacio.shape[0]
    num_max_columnas = tablero_vacio.shape[1]
    for pieza in barco:
        fila = pieza[0]
        columna = pieza[1]
        if fila < 0  or fila >= num_max_filas:
            # print(f"No puedo poner la pieza {pieza} porque se sale del tablero")
            return False
        if columna <0 or columna>= num_max_columnas:
            # print(f"No puedo poner la pieza {pieza} porque se sale del tablero")
            return False
        if tablero_vacio[pieza] == "O" or tablero_vacio[pieza] == "X":
            # print(f"No puedo poner la pieza {pieza} porque hay otro barco")
            return False
    
    for pieza in barco:   
        tablero_vacio[pieza] = "O"
    
    return tablero_vacio


# Creación de barcos manuales.
def crea_barcos_manual(mi_tablero_vacio, eslora = 2):
    while True:
        # Creamos una lista vacía que recogerá las coordenadas de las piezas del barco.
        barco = []
        # De forma aleatoria, se elige una coordenada de partida, será la primera pieza del barco.
        pieza_original = (int(input(f"Fila de la 1ª pieza de tu barco, de eslora {eslora} : "))-1,int(input(f"Columna de la 1ª pieza de tu barco, de eslora {eslora} : "))-1)
        # Se añade la pieza a la lista del barco.
        barco.append(pieza_original)
        # Se elige de forma aleatoria la dirección del barco (norte, sur, oeste, este).
        orientacion = input("Elige la orientación de tu barco entre 'N,'S','O','E': ")

        fila = pieza_original[0]
        columna = pieza_original[1]
        # Se crea un bucle for para iterar la cantidad de piezas que necesitará el barco.
        for i in range(eslora -1):
            if orientacion.upper() == "N":
                fila -= 1
            elif orientacion.upper()  == "S":
                fila += 1
            elif orientacion.upper() == "E":
                columna += 1
            else:
                columna -= 1
            # Finalmente se construye la siguiente pieza.
            pieza = (fila,columna)
            # Se añade la nueva pieza al barco.
            barco.append(pieza)

        # print("El barco ocupa las siguientes coordenadas: ", barco)

        # Ahora se coloca este barco en el tablero.
        mi_tablero_barcos = coloca_barco(mi_tablero_vacio, barco)
        print(mi_tablero_barcos,"\n","*"*42)
        if type(mi_tablero_barcos) == np.ndarray:
            return mi_tablero_barcos
        print("Tengo que intentar colocar otro barco")


# Creación de barcos aleatorios.
def crea_barco_aleatorio(tablero_rival_vacio,eslora = 4, num_intentos = 100):
    num_max_filas = tablero_rival_vacio.shape[0]
    num_max_columnas = tablero_rival_vacio.shape[1]
    while True:
        # Creamos una lista vacía que recogerá las coordenadas de las piezas del barco.
        barco = []
        # De forma aleatoria, se elige una coordenada de partida, será la primera pieza del barco.
        pieza_original = (random.randint(0,num_max_filas-1),random.randint(0, num_max_columnas -1))
        # Se añade la pieza a la lista del barco.
        barco.append(pieza_original)
        # Se elige de forma aleatoria la dirección del barco (norte, sur, oeste, este).
        orientacion = random.choice(["N","S","O","E"])

        fila = pieza_original[0]
        columna = pieza_original[1]
        # Se crea un bucle for para iterar la cantidad de piezas que necesitará el barco.
        for i in range(eslora -1):
            if orientacion == "N":
                fila -= 1
            elif orientacion  == "S":
                fila += 1
            elif orientacion == "E":
                columna += 1
            else:
                columna -= 1
            # Finalmente se construye la siguiente pieza.
            pieza = (fila,columna)
            # Se añade la nueva pieza al barco.
            barco.append(pieza)

        # print("El barco ocupa las siguientes coordenadas: ", barco)

        # Ahora se coloca este barco en el tablero.
        tablero_rival_barcos = coloca_barco(tablero_rival_vacio, barco)
        if type(tablero_rival_barcos) == np.ndarray:
            return tablero_rival_barcos
        # print("Tengo que intentar colocar otro barco")


# Definición de la función para cuando recibo el disparo del rival.
def recibir_disparo_rival(tablero, coordenada):
    # Creación de un nuevo tablero con impactos.
    tablero_disparo = tablero

    if tablero_disparo[coordenada] == "O":
        tablero_disparo[coordenada] = "X"
        print("(Yo)¡He recibido un misil rival, maldita sea!")
        print(tablero_disparo,"\n","*"*42)
        return 1
    elif tablero_disparo[coordenada] == "X":
        print("(Yo)¡Hey! El rival es tan malo que dispara al mismo sitio!")
        print(tablero_disparo,"\n","*"*42)
    elif tablero_disparo[coordenada] == "-":
        print("(Yo)¡Aguassss! jajaja!")
        print(tablero_disparo,"\n","*"*42)
    else:
        tablero_disparo[coordenada] = "-"
        print("(Yo)¡Aguassss! jajaja!")
        print(tablero_disparo,"\n","*"*42)
    return 0


# Definición de la función para cuando el rival reciba mi disparo.
def recibir_mi_disparo(tablero, coordenada, tablero_impacto_rival):
    # Creación de un nuevo tablero con impactos.
    tablero_disparo = tablero

    if tablero_disparo[coordenada] == "O":
        tablero_disparo[coordenada] = "X" 
        tablero_impacto_rival[coordenada] = "X"
        print("(Rival) ¡Has tocado algo, maldito! Ya me vengaré!! jajaja!")
        print(tablero_impacto_rival,"\n","*"*42)
        return 1
    elif tablero_disparo[coordenada] == "X":
        print("(Rival) ¡Hey! No vuelvas a disparar al mismo sitio, idiota!")
        print(tablero_impacto_rival,"\n","*"*42)
    elif tablero_disparo[coordenada] == "-":
        print("(Rival) ¡Hey! No vuelvas a disparar al mismo sitio, idiota!")
        print(tablero_impacto_rival,"\n","*"*42)
    else:
        tablero_disparo[coordenada] = "-"
        tablero_impacto_rival[coordenada] = "-"
        print("(Rival) Buuuu! Así no se dispara! Pobres peces...")
        print(tablero_impacto_rival,"\n","*"*42)
    return 0