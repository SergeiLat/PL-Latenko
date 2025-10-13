print("""2. Cоставить программу вычисления площади выпуклого четырехугольника, 
заданного длинами четырех сторон и диагонали.""")
import math
def triangle_area(a, b, c):
    # Формула Герона
    p = (a + b + c) / 2
    area = math.sqrt(p * (p - a) * (p - b) * (p - c))
    return area

print("Введите длины сторон четырехугольника и диагонали:")
a = float(input("Сторона AB: "))
b = float(input("Сторона BC: "))
c = float(input("Сторона CD: "))
d = float(input("Сторона DA: "))
diagonal = float(input("Диагональ AC: "))


if a <= 0 or b <= 0 or c <= 0 or d <= 0 or diagonal <= 0:
    print("Все длины должны быть положительными")
else:
    if (a + b > diagonal and a + diagonal > b and b + diagonal > a and
        c + d > diagonal and c + diagonal > d and d + diagonal > c):
        
        area1 = triangle_area(a, b, diagonal)
        area2 = triangle_area(c, d, diagonal)
        total_area = area1 + area2
        print(f"Площадь четырехугольника: {total_area}")