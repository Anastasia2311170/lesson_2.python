import math


def square(numb):
    return math.ceil(numb**2)


square_side = float(input("Введите размер стороны квадрата: "))
result = square(square_side)
print(f"Площадь квадрата = {result}")
# This line forces the PR button to appear перевод
