# Задача 2. Для чисел в пределах от 20 до N найти числа, кратные 20 или 21.

def isint(value):
    try:
        int(value)
        return True
    except ValueError:
        return False
numberN = input('Введите целое число N - правую границу списка чисел: ')
while isint(numberN) == False:
    numberN = input('ВВведите целое число N - правую границу списка чисел: ')
numberN=int(numberN)
myList = [element for element in range(
    20, numberN) if element % 20 == 0 or element % 21 == 0]
print(myList)