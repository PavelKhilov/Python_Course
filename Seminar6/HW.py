# Разбор ДЗ с преподователем

# def pow_num(a, b):
#     if b == 0:
#         return 1
#     if b < 0:
#         return pow_num(a, b + 1) * 1 / a
#     return pow_num(a, b - 1) * a

# print(pow_num(int(input()), int(input())))

def f(a, b):
    if b < 0 < a:
        a, b = b, a
    if b == 0:
        return a
    return f(a + 1, b - 1)

n = int(input())
m = int(input())
print(f(n, m))