# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3


# x = int(input("Введите X: "))
# y = int(input("Введите Y: "))

def find_quarter(x,y):
    if x == 0 or y == 0:
        return "координаты равны нулю"
    if x > 0 and y > 0:
        return 1
    if x < 0 and y > 0:
        return 2
    if x < 0 and y < 0:
        return 3
    if x > 0 and y < 0:
        return 4

# print(f'x={x}; y={y} -> {find_quarter(x,y)}') 