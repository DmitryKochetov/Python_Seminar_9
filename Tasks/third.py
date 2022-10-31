# 4.Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# *Пример:*

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

# decimal_num = int(input('Введите число: '))

def conv_to_bin(n):
    res = ''
    while n > 0:
        res = str(n % 2) + res
        n = n // 2
    return res

# print(conv_to_bin(decimal_num))


