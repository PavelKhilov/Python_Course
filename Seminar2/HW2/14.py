# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

n = int(input('Введите число N: '))
res = 1
while res <= n:
    print(res)
    res *= 2