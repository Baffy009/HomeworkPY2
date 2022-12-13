# Дан массив размера N. После каждого отрицательного элемента массива вставьте элемент с нулевым значением.

import random
num = int (input('Введите число:  '))
numbers = []
for i in range(num):
    numbers.append(random.randit(-99,100))
print(f'исходный массив {numbers}')

i = 0
for n in numbers:
    i +=1
    if n < 0:
        numbers.insert(i, 0)
print(f'новый массив {numbers}') 


