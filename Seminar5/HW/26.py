# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, 
# и возводит число А в целую степень B с помощью рекурсии.

a = int(input('Число: '))
b = int(input('Степень: '))

def multiplay(a, b):
    if b > 0:
        return a * multiplay(a, b - 1)
    elif b < 0:
        return (1 / a) * multiplay(a, b + 1)
    else:
        return 1

print(f'Результат:', multiplay(a, b))