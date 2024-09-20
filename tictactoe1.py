import random
from colorama import Fore, Style, init

# Inicializar Colorama
init(autoreset=True)

# Función para imprimir el tablero con colores
def mostrar_tablero(tablero):
    print(Fore.BLUE + "\nTablero actual:")
    for fila in range(0, 9, 3):
        print(Fore.BLUE + "---|---|---")
        print(f" {mostrar_celda(tablero[fila])} | {mostrar_celda(tablero[fila+1])} | {mostrar_celda(tablero[fila+2])} ")
    print(Fore.BLUE + "---|---|---\n")

# Función para mostrar cada celda con su respectivo color
def mostrar_celda(celda):
    if celda == 'X':
        return Fore.RED + 'X'
    elif celda == 'O':
        return Fore.GREEN + 'O'
    else:
        return celda

# Función para verificar si hay un ganador
def verificar_ganador(tablero, jugador):
    combinaciones_ganadoras = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Filas
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columnas
        [0, 4, 8], [2, 4, 6]              # Diagonales
    ]
    for combinacion in combinaciones_ganadoras:
        if tablero[combinacion[0]] == tablero[combinacion[1]] == tablero[combinacion[2]] == jugador:
            return True
    return False

# Función para obtener el movimiento de la computadora
def movimiento_computadora(tablero):
    posibles_movidas = [i for i, celda in enumerate(tablero) if celda == '-']
    return random.choice(posibles_movidas)

# Función para verificar si el tablero está lleno
def tablero_lleno(tablero):
    return '-' not in tablero

# Función principal del juego
def jugar_tic_tac_toe():
    tablero = ['-'] * 9
    jugador = input(Fore.BLUE + "¿Quién juega primero? (X para usuario, O para computadora): ").upper()

    while jugador not in ['X', 'O']:
        jugador = input(Fore.BLUE + "Opción inválida. Elige X (usuario) o O (computadora): ").upper()

    turno_actual = 'X' if jugador == 'X' else 'O'
    
    while True:
        mostrar_tablero(tablero)
        
        # Movimiento del jugador actual
        if turno_actual == 'X':
            movimiento_valido = False
            while not movimiento_valido:
                try:
                    movida = int(input(Fore.BLUE + "Elige una posición (1-9): ")) - 1
                    if tablero[movida] == '-':
                        tablero[movida] = 'X'
                        movimiento_valido = True
                    else:
                        print(Fore.BLUE + "Posición ocupada, elige otra.")
                except (ValueError, IndexError):
                    print(Fore.BLUE + "Entrada inválida, elige una posición entre 1 y 9.")
        else:
            print(Fore.BLUE + "Turno de la computadora...")
            movida = movimiento_computadora(tablero)
            tablero[movida] = 'O'

        # Verificar si hay un ganador
        if verificar_ganador(tablero, turno_actual):
            mostrar_tablero(tablero)
            if turno_actual == 'X':
                print(Fore.RED + "¡Felicidades, ganaste!")
            else:
                print(Fore.GREEN + "La computadora ha ganado.")
            break

        # Verificar si el tablero está lleno
        if tablero_lleno(tablero):
            mostrar_tablero(tablero)
            print(Fore.BLUE + "El juego termina en empate.")
            break

        # Cambiar de turno
        turno_actual = 'O' if turno_actual == 'X' else 'X'

# Ejecutar el juego
if __name__ == '__main__':
    jugar_tic_tac_toe()
