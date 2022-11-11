# Задайте список из нескольких чисел.
# Напишите программу, которая найдёт сумму элементов списка,
# стоящих на нечётной позиции.
# Пример через enumerate

import random

lst = []
for i in range(10):
    lst.append(random.randint(1, 10))
lst2 = [v for i, v in enumerate(lst, start=0) if i % 2]
print(f'Array :{lst}')
print(f'Odd index :{lst2}')
print(f'Sum odd :{sum(lst2)}')
