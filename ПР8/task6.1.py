# 1. Дана целочисленная квадратная матрица. Найти в каждой строке наибольший элемент и в каждом столбце наименьший. Вывести на экран.
A = [
    [4, 6, 2],
    [7, 2, 9],
    [8, 2, 5]
]
max_lane = 0
max_colum = 0
print("Исходный массив: ")
for i in range(len(A)):
    for j in range(len(A)):
        print(A[i][j], end=' ')
    print()

for i in range(len(A)):
    for j in range(len(A)):
        if max_lane < A[i][j]:
            max_lane = A[i][j]
    print(f"Максимальный элемент в строке {i+1} = {max_lane}")
    max_lane = 0

for i in range(len(A)):
    for j in range(len(A)):
        if max_colum < A[j][i]:
            max_colum = A[j][i]
    print(f"Максимальный элемент в столбце {i+1} = {max_colum}")
    max_colum = 0