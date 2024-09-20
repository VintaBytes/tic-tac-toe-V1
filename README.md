# Juego de Tic Tac Toe en la Terminal - V1

<span><img src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue"/></span>

Este proyecto es un juego de **Tic Tac Toe** implementado en Python que se juega directamente en la terminal. Se utiliza la biblioteca **Colorama** para darle color a los símbolos y al tablero. El usuario compite contra la computadora, y el juego sigue las reglas tradicionales de Tic Tac Toe.

<span><img src="https://github.com/VintaBytes/tic-tac-toe-V1/blob/main/tictactoe1.png?raw=true"/></span>

## Descripción del Código

El código está estructurado en varias funciones, cada una encargada de tareas específicas, como la gestión del flujo del juego, la impresión del tablero, la verificación de las condiciones de victoria o empate, y la toma de decisiones de la computadora.

### Bibliotecas Utilizadas

Se utiliza la biblioteca **Colorama** para dar color al texto en la terminal. Las **X** se muestran en rojo, las **O** en verde y las líneas del tablero y los mensajes se presentan en azul. Colorama se inicializa con `autoreset=True` para que los colores se restablezcan después de cada línea de texto.

### Función: `mostrar_tablero(tablero)`

Esta función imprime el tablero actual del juego en la terminal. El tablero está representado por una lista de 9 elementos. Dependiendo del contenido de cada celda, la función colorea las **X** en rojo, las **O** en verde y las celdas vacías se muestran sin color. Las líneas divisorias del tablero se imprimen en azul para que sea visualmente claro.

### Función: `mostrar_celda(celda)`

Esta función se encarga de devolver la representación de cada celda con su respectivo color. Si la celda contiene una **X**, la devuelve en rojo. Si contiene una **O**, la devuelve en verde. Si está vacía, se devuelve la celda vacía sin color.

### Función: `verificar_ganador(tablero, jugador)`

La función `verificar_ganador` revisa si el jugador actual ha ganado el juego. Utiliza las combinaciones ganadoras clásicas de Tic Tac Toe (filas, columnas y diagonales) y compara las posiciones del tablero para verificar si hay tres símbolos consecutivos del mismo jugador. Si hay una combinación ganadora, la función devuelve `True`, de lo contrario, devuelve `False`.

### Función: `movimiento_computadora(tablero)`

Esta función elige un movimiento aleatorio de entre las posiciones disponibles en el tablero. Recorre el tablero buscando celdas vacías y selecciona una al azar para hacer el movimiento de la computadora.

### Función: `tablero_lleno(tablero)`

Esta función verifica si el tablero está completamente lleno. Si no quedan celdas vacías, devuelve `True`, indicando que el juego ha terminado en empate. De lo contrario, devuelve `False`.

### Función Principal: `jugar_tic_tac_toe()`

Esta es la función principal del juego. Inicia el tablero vacío y solicita al usuario que elija quién jugará primero, eligiendo entre **X** (jugador humano) o **O** (computadora). Dependiendo de la elección, el juego alterna entre los turnos del jugador humano y la computadora.

Para el turno del jugador, la función solicita al usuario que ingrese un número del 1 al 9 para colocar su **X** en la posición correspondiente del tablero. Si la celda seleccionada ya está ocupada, el juego le pedirá al usuario que elija otra. Para la computadora, se utiliza la función `movimiento_computadora` para realizar su jugada automáticamente.

Después de cada movimiento, se verifica si hay un ganador mediante la función `verificar_ganador`. Si alguien gana, se imprime el tablero final y se muestra un mensaje con el resultado. Si el tablero está lleno y no hay ganador, el juego termina en empate y se notifica al usuario.

### Ejecución del Juego

El juego se ejecuta mediante un bloque `if __name__ == '__main__'` que llama a la función `jugar_tic_tac_toe`. Esto permite que el juego se inicie automáticamente cuando el archivo es ejecutado desde la terminal.

## Código completo:

```python
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

```

