# Реализация 1
n = int(input())
count = 0

for i in range(n):
    if int(input()):
        count += 1

print(min(count, n - count))

# Реализация 2
counter = int(input('Сколько элементов вы планируете ввести? '))

numbers = []
for i in range(counter):
    numbers.append(int(input('Введите очередное число: ')))

print(numbers)
num_value = len(set(numbers))
print(num_value)