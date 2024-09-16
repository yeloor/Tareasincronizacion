def buscar_valor(matriz, valor_buscado):
    # Iterar sobre cada fila y columna de la matriz
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            # Verificar si el valor en la posición actual es el valor buscado
            if matriz[i][j] == valor_buscado:
                return (i, j)  # Devolver la posición (fila, columna)
    return None  # Devolver None si el valor no se encuentra

# Definir una matriz 3x3 con valores numéricos
matriz = [
    [5, 8, 2],
    [3, 6, 7],
    [9, 1, 4]
]

# Valor que queremos buscar
valor_buscado = 7

# Llamar a la función de búsqueda
resultado = buscar_valor(matriz, valor_buscado)

# Mostrar resultados
if resultado:
    print(f"El valor {valor_buscado} se encontró en la posición {resultado}.")
else:
    print(f"El valor {valor_buscado} no se encontró en la matriz.")
