import random

def main():
    print("Bienvenido al juego de Carrera Numérica")
    
    # Solicitar la cantidad de jugadores
    while True:
        try:
            num_jugadores = int(input("Ingrese la cantidad de jugadores (entre 2 y 4): "))
            if num_jugadores < 2 or num_jugadores > 4:
                print("Error: Debe ingresar un número de jugadores entre 2 y 4.")
            else:
                break
        except ValueError:
            print("Error: Debe ingresar un número válido.")
    
    # Solicitar el nivel de tablero a jugar
    niveles = {
        1: 20,
        2: 30,
        3: 50,
        4: 100
    }
    while True:
        print("\nSeleccione el nivel de tablero a jugar:")
        print("1. Nivel básico (Tablero de 20 posiciones)")
        print("2. Nivel intermedio (Tablero de 30 posiciones)")
        print("3. Nivel avanzado (Tablero de 50 posiciones)")
        print("4. Nivel experto (Tablero de 100 posiciones)")
        try:
            nivel = int(input("Ingrese el número correspondiente al nivel: "))
            if nivel not in niveles:
                print("Error: Seleccione un nivel válido.")
            else:
                tablero = niveles[nivel]
                break
        except ValueError:
            print("Error: Debe ingresar un número válido.")
    
    # Inicializar la posición de cada jugador en el tablero
    posiciones = [0] * num_jugadores
    
    # Contador de pares consecutivos para cada jugador
    pares_consecutivos = [0] * num_jugadores
    
    # Comenzar el juego
    ganador = None
    while ganador is None:
        for jugador in range(num_jugadores):
            input(f"\nEs el turno del jugador {jugador + 1}. Presione Enter para lanzar los dados.")
            
            # Lanzar los dados
            dado1 = random.randint(1, 6)
            dado2 = random.randint(1, 6)
            suma_dados = dado1 + dado2
            print(f"El jugador {jugador + 1} obtuvo un {dado1} y un {dado2}, avanzará {suma_dados} posiciones.")
            
            # Mover al jugador
            posiciones[jugador] += suma_dados
            
            # Verificar si el jugador ha llegado a la meta
            if posiciones[jugador] >= tablero:
                ganador = jugador + 1
                break
            
            # Verificar si el jugador ha obtenido un par
            if dado1 == dado2:
                pares_consecutivos[jugador] += 1
                if pares_consecutivos[jugador] == 3:
                    print(f"El jugador {jugador + 1} ha obtenido tres pares consecutivos. ¡Es el ganador!")
                    ganador = jugador + 1
                    break
            else:
                pares_consecutivos[jugador] = 0
            
            # Mostrar la posición actual de cada jugador
            print(f"El jugador {jugador + 1} está en la posición {posiciones[jugador]}")
    
    print(f"\n¡El jugador {ganador} ha ganado el juego!")
    
if __name__ == "__main__":
    main()


