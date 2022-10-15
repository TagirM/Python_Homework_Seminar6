# Задача 3. Написать функцию, аргументы - имена сотрудников, возвращает словарь, ключи -
# первые буквы имен, значения - списки, содержащие имена, начинающиеся с соответствующей буквы.

from collections import defaultdict

names = ["Иван", "Мария", "Петр", "Илья", "Марина", "Алина", "Бибочка", "Петр"]

def myNewDict(arguments):
    myDict = defaultdict(list)    
    for j in arguments:        
        myDict[j[0]].append(j)    
    return myDict

print(myNewDict(names))
