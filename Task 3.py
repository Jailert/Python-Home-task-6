# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример List comprehenssion.

import random

lst = []
for i in range(10):
    lst.append(random.randint(1, 10))
print(f'Array : {lst}')

size = len(lst)//2
changed_lst = [lst[i] * lst[-i - 1] for i in range(size)]

print(f'Changed lst : {changed_lst}')
