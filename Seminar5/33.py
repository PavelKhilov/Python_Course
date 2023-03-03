# Хакер Василий получил доступ к классному
# журналу и хочет заменить все свои минимальные
# оценки на максимальные. Напишите программу,
# которая заменяет оценки Василия,
# но наоборот: все максимальные – на минимальные.

import random

n = int(input('Введите колличество оценок: '))

array = [random.randint(1, 5) for i in range(n)]
print(array)
min_value = min(array)
max_value = max(array)
result = [min_value if i == max_value else i for i in array]
print(result)