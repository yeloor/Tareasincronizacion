def bubble_sort(fila):
    # Implementar el algoritmo Bubble Sort para ordenar la fila
    n = len(fila)
    for i in range(n):
        for j in range(0, n-i-1):
            if fila[j] > fila[j+1]:
                # Intercambiar si el elemento actual es mayor que el siguiente
                fila[j], fila[j+1] = fila[j+1], fila[j]

def ordenar_fila(matriz, fila_index):
    # Ordenar una fila específica en la matriz
    if fila_index < 0 or fila_index >= len(matriz):
        print("Índice de fila fuera de rango.")
        return
    fila = matriz[fila_index]
    bubble_sort(fila)
    matriz[fila_index] = fila

# Definir una matriz 3x3 con valores numéricos
matriz = [
    [9, 2, 5],
    [1, 8, 4],
    [7, 6, 3]
]

# Mostrar la matriz original
print("Matriz original:")
for fila in matriz:
    print(fila)

# Índice de la fila que queremos ordenar
indice_fila = 1  # Puedes cambiar este valor para ordenar una fila diferente

# Llamar a la función para ordenar la fila
ordenar_fila(matriz, indice_fila)

# Mostrar la matriz con la fila ordenada
print("\nMatriz con la fila ordenada:")
for fila in matriz:
    print(fila)