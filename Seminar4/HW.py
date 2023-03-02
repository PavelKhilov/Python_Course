# реализация 1 задача 16
list_nums = [int(input()) for _ in range(int(input()))]
print(list_nums.count(int(input())))

# реализация 2 задача 16
from random import choices

num = int(input())
list_num = choices(range(num * 2), k = num)
print(list_num)

result = list_num.count(int(input()))
print(result)

# реализация 2 задача 18
from random import randint

n = int(input())
lit_num = [randint(1, 50) for _ in range(n)]

print(list_num)

b = int(input())
m = min(list_num, key=lambda x: abs(x - b))
print(m)

# реализация 1 задача 20
ang_dict = {"AEIOULNSTRАВЕИНОРСТ": 1, "DGДКЛМПУ": 2, 
         "BCMPБГЁЬЯ": 3, "FHVWYЙЫ": 4, "KЖЗХЦЧ": 5, 
         "JXШЭЮ": 8, "QZФЩЪ": 10}

word = input()

print = sum([i[1]for i in ang_dict.items() for j in word if j.upper() in i[0]])