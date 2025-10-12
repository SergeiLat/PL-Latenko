# 1. Найдите сумму и произведение элементов списка. Результаты вывести на экран. 
print("Задание 1. Найдите сумму и произведение элементов списка. Результаты вывести на экран.")
numbers = [2, 3, 5, 7, 11]
sum_result = 0
product_result = 1

for num in numbers:
    sum_result += num
    product_result *= num

print(f"Список: {numbers}")
print(f"Сумма элементов: {sum_result}")
print(f"Произведение элементов: {product_result}\n")

# 2. В массиве действительных чисел все нулевые элементы заменить на среднее арифметическое всех элементов массива. 
print("Задание 2. В массиве действительных чисел все нулевые элементы заменить на среднее арифметическое всех элементов массива.")
numbers = [1.5, 0, 3.2, 0, 4.8]
total_sum = sum(numbers)
count = len(numbers)
average = total_sum / count
print(f"Исходный массив: {numbers}")
    
for i in range(count):
    if numbers[i] == 0:
        numbers[i] = average

print(f"Результат: {numbers}")