# Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу.

# Считается, что любые два элемента, равные друг другу образуют одну пару, которую необходимо посчитать.
# Вводится список чисел. Все числа списка находятся на разных строках.
from time import time
from random import choices

start = time()

print(time() - start)

list_1 = [1, 2, 3, 4, 2, 3, 4, 3, 5, 6, 5, 3]

# list_2 = list(set(list_1))
# print(list_2)
# count = 0
# for i in range(len(list_2)):
#     count += list_1.count(list_2[i]) // 2
# print(count)

dict_list = {}.fromkeys(list_1, 0)
print(dict_list)
for i in list_1:
    dict_list[i] += 1

print(sum([i // 2 for i in dict_list.values() if not i % 2]))



# li = [1, 2, 4, 2, 5, 1, 6, 4, 4]

li = choices(range(3000), k=2000)
sum = 0
for i in li:
    if li.count(i) > 1:
        if li.count(i) % 2 != 0:
            sum += (li.count(i) - 1) / 4
            li.pop(i)
        else:
            sum += li.count(i) / 4
        print(f'i = {li.count(i) / 4}, sum = {sum}')