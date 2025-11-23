# Чтение матрицы из файла
with open("LatenkoSO_YB52_vvod.txt", "r") as f:
    lines = f.readlines()

# Преобразуем строки файла в матрицу чисел
A = [list(map(int, line.split())) for line in lines]

max_line = 0
max_colum = 0

# Открываем файл для записи результатов
with open("LatenkoSO_YB52_vivod.txt", "w") as f_out:
    f_out.write("Исходный массив:\n")
    for row in A:
        f_out.write(" ".join(map(str, row)) + "\n")
    f_out.write("\n")

    # Максимальные элементы по строкам
    for i in range(len(A)):
        for j in range(len(A)):
            if max_line < A[i][j]:
                max_line = A[i][j]
        f_out.write(f"Максимальный элемент в строке {i+1} = {max_line}\n")
        max_line = 0

    f_out.write("\n")

    # Максимальные элементы по столбцам
    for i in range(len(A)):
        for j in range(len(A)):
            if max_colum < A[j][i]:
                max_colum = A[j][i]
        f_out.write(f"Максимальный элемент в столбце {i+1} = {max_colum}\n")
        max_colum = 0
