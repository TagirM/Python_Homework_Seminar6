# Задача 1. Представлен список чисел. Необходимо вывести элементы
# исходного списка, значения которых больше предыдущего элемента

dataList = [1, 5, 3, 6, 5, 9, 2, 4]
myList = [dataList[0]]
myList = [dataList[index] for index in range(
    1, len(dataList)) if dataList[index] > dataList[index-1]]
print(myList)
