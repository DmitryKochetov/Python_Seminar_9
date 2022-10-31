
# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между
# ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

# пришлось сначала городить огород с decimal, пока не понял, что ошибка в условии, 5.09 должно не округляться, 
# а просто откидывать дробную часть до 2 знака. Оставил как есть, не трогал, раз работает

from decimal import Decimal, ROUND_FLOOR

# ax = 3
# ay = 6
# bx = 2
# by = 1

def find_distance(ax, ay, bx, by):
    # return round((((ax-bx)**2+(ay-by)**2)**(0.5)), 2)
    number = Decimal(((ax-bx)**2+(ay-by)**2)**(0.5))
    return float(number.quantize(Decimal("1.00"), ROUND_FLOOR))

# print(f'A ({ax},{ay}); B ({bx},{by}) -> {find_distance(ax,ay,bx,by)}')
