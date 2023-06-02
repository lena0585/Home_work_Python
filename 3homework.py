# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в списке A.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
# 5
#     1 2 3 4 5
#     3
#     -> 1

# n = int(input('Введите размер элементов списка: '))
# some_list = []
# x = int (input('Введите число х: '))
# count = 0
# from random import randint
# for i in range(n):
#     some_list.append(randint(1,10))
# print(some_list)
# for i in range(n):
#     if some_list[i] == x:
#         count += 1
# print(f'Число {x} встречается в списке А {count} раз.')
# Задача 18: Требуется найти в списке A самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
# 5
#     1 2 3 4 5
#     6
#     -> 5
n = int(input("Введите количество элементов списка: "))
import random
numbers = [random.randint(1,5) for i in range(n)]
print (numbers)
x = int(input('Заданное число: '))
find_number = numbers[0]
for number in numbers:
    if abs(x - number) < abs(x - find_number):
        find_number = number
print(find_number) 


