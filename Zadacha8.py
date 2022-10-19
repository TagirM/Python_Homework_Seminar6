# Задача 8.
# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

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
multiList = []

myList = [randint(0, 20) for elem in range(countElem)]
print(f'Список: {myList}')

if countElem % 2 == 0:
    multiList = [myList[elem]*myList[-1-elem] for elem in range(countElem//2)]
else:
    for elem in range(countElem//2+1):
        multiList.append(myList[elem]*myList[-1-elem])
        if elem == countElem//2+1:
            multiList.append(myList[elem]*myList[elem])

print(f'Произведение пар чисел списка: {multiList}')
