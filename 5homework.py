# Задача №35. Решение в группах
# Напишите функцию, которая принимает одно число и
# проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое
# имеет 2 делителя: 1 и n(само число)
# def digit_check(n):
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True
# print(digit_check(25))

# Задача №37.
# Дано натуральное число N и
# последовательность из N элементов.
# Требуется вывести эту последовательность в
# обратном порядке.
# Примечание. В программе запрещается
# объявлять массивы и использовать циклы
# (даже для ввода и вывода).
# Input: 2 -> 3 4
# Output: 4 3
def pos(n):
    if n == 0:
        return " "
    a = int(input("Введите число: "))
    return pos(n-1) + f' {a}'
n = int(input("Введите количество элементов: "))
print(pos(n))