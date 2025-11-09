# Дана действительная квадратная матрица порядка N (N — нечетное), все элементы которой различны. Найти наибольший элемент среди 
# стоящих на главной и побочной диагоналях и поменять его местами с элементом, стоящим на пересечении этих диагоналей.
def swap_max_with_center(matrix):
    N = len(matrix)
    if N % 2 == 0:
        raise ValueError("N должно быть нечётное")
    
    k = (N - 1) // 2
    center_row, center_col = k, k
    
    # Ищем максимум на диагоналях
    max_val = float('-inf')
    max_row, max_col = -1, -1
    
    # Главная диагональ
    for i in range(N):
        if matrix[i][i] > max_val:
            max_val = matrix[i][i]
            max_row, max_col = i, i
    
    # Побочная диагональ (без повторного учета центра)
    for i in range(N):
        j = N - 1 - i
        if matrix[i][j] > max_val:
            max_val = matrix[i][j]
            max_row, max_col = i, j
    
    # Swap
    if (max_row, max_col) != (center_row, center_col):
        matrix[center_row][center_col], matrix[max_row][max_col] = matrix[max_row][max_col], matrix[center_row][center_col]

    return matrix

def print_matrix (a):
    for i in a:
        print(i)

example_matrix = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
]
print("Изначальная матрица:")
print_matrix(example_matrix)
result = swap_max_with_center(example_matrix)
print("Итоговая матрица:")
print_matrix(result)