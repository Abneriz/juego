import os
from readchar import readkey, key

def borrar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def mapa(cadena_mapa):
    filas = cadena_mapa.strip().split('\n')
    laberinto = []
    
    for fila in filas:
        caracteres_fila = list(fila)
        laberinto.append(caracteres_fila)

    return laberinto   

def mover_personaje(laberinto, direccion, px, py):
    nueva_px, nueva_py = px, py

    if direccion == key.DOWN:
        nueva_px += 1
    elif direccion == key.LEFT:
        nueva_py -= 1
    elif direccion == key.RIGHT:
        nueva_py += 1
    elif direccion == key.UP:
        nueva_px -= 1

    if (
        0 <= nueva_px < len(laberinto) and
        0 <= nueva_py < len(laberinto[0]) and
        laberinto[nueva_px][nueva_py] != '#'
    ):
        laberinto[px][py] = '.'
        px, py = nueva_px, nueva_py
        laberinto[px][py] = 'P'

    return px, py

def jugar(laberinto, px, py, posicion_final):
    while (px, py) != posicion_final:
        enseñar_mapa(laberinto)
        direccion = readkey()

        if direccion in [key.DOWN, key.LEFT, key.RIGHT, key.UP]:
            px, py = mover_personaje(laberinto, direccion, px, py)

        if (px, py) == posicion_final:
            break

def enseñar_mapa(laberinto):
    borrar_terminal()
    for fila in laberinto:
        print("".join(fila))

cadena_mapa = """
..###################
........#...#.#.#.#.#
#.#########.#.#.#.#.#
#.......#...........#
#.#########.#.###.###
#...#.#...#.#...#...#
#.###.#.#####.#####.#
#.#.#...........#...#
#.#.#.#.###.#.#.#####
#.....#...#.#.#...#.#
#.#######.#########.#
#.#.#.#.#.#.......#.#
###.#.#.#.#.#.###.#.#
#...#.....#.#.#...#.#
###.#.#####.#######.#
#.#.#.#...#...#.....#
#.#.#.###.###.###.###
#...#...#.#.........#
#.#.#.#.#.###.#####.#
#.#...#.......#.....
###################.

"""
matriz_laberinto = mapa(cadena_mapa)

posicion_inicial = (0, 0)
posicion_final = (20, 20)

px, py = posicion_inicial
matriz_laberinto[px][py] = 'P'   

print(">>Ingresa tu nombre para jugar<<:")
nombre = input()
print(f">>Bienvenid@", nombre, f"comencemos está aventura:<<")
print(">>Presiona UP en cualquier momento para comenzar<<:")
print(">>preciona cualquier tecla para confirmar que todo esta bien<<:")
print(">>Preciona la letra N sumar números en el bucle<<:")

numero = 0

while True:
  k = readkey()

  if k == key.DOWN:
    print("Abajo")
        
  elif k == key.LEFT:
    print("Izquierda")
   
  elif k == key.RIGHT:

    print("Derecha")

  elif k == key.UP:
        print("Arriba")
        enseñar_mapa(matriz_laberinto)
        px, py = jugar(matriz_laberinto, px, py, posicion_final)

  if (px, py) == posicion_final:
        print("¡Bien hecho, Has completado el laberinto!")
        break   
  
  elif k == key.UP:
    print("Arriba")
    break

  if k == 'n':
        borrar_terminal()
        print(f"Preciona n para sumar número: {numero}")
        numero += 1
        if numero > 50:
            numero = 0
            
  else:
     print(k)
  

