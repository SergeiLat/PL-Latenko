# 1. Найти все натуральные числа, не превосходящие заданного n, которые делятся на каждую из своих цифр.

num = int(input("Введите число \n"))
def find_numbers(num):
    result = []
    for i in range(1, num+1):
        number = i
        delimo = True
        while number > 0:
            a = number % 10
            if a == 0 or i % a != 0:
                delimo = False
                break
            number //= 10
        if delimo:
            result.append(i)
    return result
numbers = find_numbers(num)
print(f"Натуральные числа, которые делятся на каждую из своих цифр: \n{find_numbers(num)}")