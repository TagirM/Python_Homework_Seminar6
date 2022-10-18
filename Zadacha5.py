# Задача 5. Реализовать функцию, возвращающую n шуток, сформированных из трех
# случайных слов, взятых из трех списков (по одному из каждого).
from random import randint
text_1 = ["дом", "огонь", "лес", "автомобиль", "город"]
text_2 = ["ночью", "завтра", "вчера", "сегодня", "позавчера"]
text_3 = ["мягкий", "зеленый", "яркий", "веселый", "утопичный"]


def isint(value):
    try:
        int(value)
        return True
    except ValueError:
        return False


nJuke = input('Введите количество шуток: ')
while isint(nJuke) == False:
    nJuke = input('Введите количество шуток: ')
nJuke = int(nJuke)


juke = [' '.join((text_1[randint(0, len(text_1)-1)], text_2[randint(0, len(text_2)-1)],
                  text_3[randint(0, len(text_3)-1)])) for i in range(nJuke)]
print(juke)
