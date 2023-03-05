# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.

n = int(input('Введите число элементов первого множества: '))
m = int(input('Введите число элементов второго множества: '))
n_array = [int(i) for i in input().split()]
m_array = [int(j) for j in input().split()]

c = sorted(set(n_array).intersection(set(m_array)))
print(c)