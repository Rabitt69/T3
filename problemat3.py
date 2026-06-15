import time
import copy

laberinto = [
    ["F",  1,  1,  1, 0, 1, 1, 1, 1],
    [-2,   0,  0, -1, 0, 1, 0, 1, 0],
    [ 1,   1,  0,  1, 1, 1, 0, 1, 0],
    [ 0,   1,  0, -1, 0, 0, 0,-1, 0],
    [ 1,   1,  1,  1, 1, 1, 1, 1, 0],
    [-1,   0,  0,  0, 0, 0, 0, 1, 1],
    [ 1,   1,  1,  1,-1, 1, 1, 1, 0],
    [ 1,   0,  0,  1, 0, 1, 0, 1, 0],
    ["I",  1, -1,  1, 1, 1, 0, 1, 1]
]

FILAS = len(laberinto)
COLUMNAS = len(laberinto[0])


solucion = [[0 for _ in range(COLUMNAS)] for _ in range(FILAS)]


movimientos = [
    (1, 0),
    (0, 1),
    (-1, 0),
    (0, -1)
]

def mostrar_matriz(m):
    for fila in m:
        print(" ".join(f"{str(x):>2}" for x in fila))
    print()

def obtener_valor(fila, columna):
    valor = laberinto[fila][columna]

    if valor == "I" or valor == "F":
        return 1

    return valor

def backtracking(fila, columna, vidas):

    
    if fila < 0 or fila >= FILAS or columna < 0 or columna >= COLUMNAS:
        return False

    valor = laberinto[fila][columna]

    
    if valor == 0:
        return False

    if solucion[fila][columna] == 1:
        return False

    vidas_actuales = vidas

    if valor == -1:
        vidas_actuales -= 1

    elif valor == -2:
        vidas_actuales -= 2

    # Sin vidas
    if vidas_actuales <= 0:
        return False

    solucion[fila][columna] = 1

    print(f"Posición: ({fila},{columna}) | Vidas: {vidas_actuales}")
    mostrar_matriz(solucion)
    time.sleep(0.3)

    # Llegó al final
    if valor == "F":
        return True

    
    for df, dc in movimientos:
        nf = fila + df
        nc = columna + dc

        if backtracking(nf, nc, vidas_actuales):
            return True

    
    solucion[fila][columna] = 0

    return False


print("LABERINTO ORIGINAL")
mostrar_matriz(laberinto)


inicio_fila = 8
inicio_columna = 0

vidas_iniciales = 3

encontrado = backtracking(
    inicio_fila,
    inicio_columna,
    vidas_iniciales
)

if encontrado:
    print("\n✅ EL RATÓN LOGRÓ LLEGAR A LA SALIDA")
    print("\nMATRIZ SOLUCIÓN:")
    mostrar_matriz(solucion)
else:
    print("\n❌ NO EXISTE UN CAMINO VÁLIDO")