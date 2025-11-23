def swap_max_with_center(matrix):
    N = len(matrix)
    if N % 2 == 0:
        raise ValueError("N должно быть нечётное")

    k = (N - 1) // 2
    center_row, center_col = k, k

    max_val = float('-inf')
    max_row, max_col = -1, -1

    # главная диагональ
    for i in range(N):
        if matrix[i][i] > max_val:
            max_val = matrix[i][i]
            max_row, max_col = i, i

    # побочная диагональ
    for i in range(N):
        j = N - 1 - i
        if matrix[i][j] > max_val:
            max_val = matrix[i][j]
            max_row, max_col = i, j

    # обмен
    if (max_row, max_col) != (center_row, center_col):
        matrix[center_row][center_col], matrix[max_row][max_col] = matrix[max_row][max_col], matrix[center_row][center_col]

    return matrix


def read_matrix(filename):
    with open(filename, "r") as f:
        lines = f.readlines()
    N = int(lines[0].strip())
    matrix = [list(map(int, line.split())) for line in lines[1:N+1]]
    return matrix


def write_matrix(filename, matrix):
    with open(filename, "w") as f:
        for row in matrix:
            f.write(" ".join(map(str, row)) + "\n")

matrix = read_matrix("LatenkoSO_YB52_vvod.txt")
result = swap_max_with_center(matrix)
write_matrix("LatenkoSO_YB52_vivod.txt", result)
