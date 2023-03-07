# все делители числа 284
# 220 = 1 + 2 + 4 + 71 + 142
# все делители числа 220
# 284 = 1 + 2 + 4 + 5 + 10 + 11 + 20 + 22 + 44 + 55 + 110
from time import time
from random import choices

li = []
user_in = abs(int(input("Input a number: ")))

start = time()

def sum_dev(user_num):
    cou = 1
    for i in range(2, int(user_num ** 0.5)):
        if user_num % i == 0:
            cou += i + user_num / i
    return cou

for j in range(10, user_in):
    first = sum_dev(j)
    second = sum_dev(first)
    if second == j and first < second:
        print(j, first)

print(time() - start)

# print(li)
# print(sum(li))

