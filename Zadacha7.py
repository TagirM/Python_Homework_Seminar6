# Задача 7.
# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму
# элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12.

from random import randint


def isint(value):
    try:
        int(value)
        return True
    except ValueError:
        return False


countElem = input('Введите количество элементов списка: ')
while isint(countElem) == False:
    countElem = input('Введите количество элементов списка: ')
countElem = int(countElem)

myList = [randint(0, 9) for elem in range(countElem) if elem % 2 != 0]
# print(f'Список: {myList}')
print(f'Сумма элементов на нечётных позициях равна {sum(myList)}')
