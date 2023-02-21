# Дано натуральное число A > 1.
# Определите, каким по счету числом Фибоначчи
# оно является, то есть выведите такое число n,
# что φ(n)=A. Если А не является числом Фибоначчи, выведите число -1.

# 1  2  3  4  5  6  7   8   9  10  11
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55

fibo_n = int(input('Введите число: '))
count = 2
a = 0
b = 1

while fibo_n >= b:
    if fibo_n == b:
        print(count)
        break
    a, b = b, a + b
    count += 1
else:
    print(-1)

# number = int(input("Введите число"))
# result = 1
# count = 3
# if number == 1:
#     print("Номер будет и 2 и 3")
# elif number == 0:
#     print("Первый номер")
# else:
#     while result < number:
#         count += 1
#         if result == number:
#             break
#         result = int(round(1.68 * result, 0))
#         print(result)
#     print("Номер будет ", count)