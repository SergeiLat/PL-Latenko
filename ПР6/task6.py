# Дан одномерный массив из 10 целых чисел. Найти максимальный элемент и 
# сравнить с ним остальные элементы. Вывести количество меньших 
# максимального и больших максимального элемента.
print("""Задание 1. Дан одномерный массив из 10 целых чисел. Найти максимальный элемент и 
сравнить с ним остальные элементы. Вывести количество меньших 
максимального и больших максимального элемента.""")
import random
mass = []
for i in range(10):
    a = random.randint(-10, 10)
    mass.append(a)
print(f"Исходный массив: {mass}")
max_num = mass[0]
count_max_number = 0
count_min_number = 0
for i in mass:
    if i > max_num:
        max_num = i
print(f"Максимальное число: {max_num}")
for i in mass:
    if i > max_num:
        count_max_number += 1
    elif i < max_num:
        count_min_number += 1
print(f"Количество элементов, больше максимального: {count_max_number}")
print(f"Количество элементов, меньше максимального: {count_min_number}")
