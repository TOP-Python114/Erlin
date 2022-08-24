from math import factorial
from random import choice
from itertools import permutations


set_of_words = {"cлишком", "стар", "я"}


# permutes = lambda x: " ".join("".join(x) for x in permutations(x))
# print("first way:", )
# print(permutes(set_of_words))
# print()
# oh, we need a generator ok


def permutes_gen1(elements: set):
    # ИСПОЛЬЗОВАТЬ: зачем столько лишних действий? если берёте функцию permutations(), то итерировались бы прямо по ней
    for p in permutations(elements):
        yield "".join(p)


perms = permutes_gen1(set_of_words)
print("first way:", )
for i in perms:
    print(i,end=" ")
print("\n")


# bad method, but i think it's fun
# ИСПРАВИТЬ: как насчёт адекватной собственной функции по нахождению перестановок? смешной вариант можно было предложить третьим, а пока незачёт
def permutes_gen2(elements: set) -> str:
    res = list()
    tempelem = ""
    # ИСПРАВИТЬ: не стоит вычислять факториал на каждой итерации
    while len(res) != factorial(len(elements)):
        temp_set = set(elements)
        while temp_set:
            a = choice(list(temp_set))
            tempelem += a
            temp_set.remove(a)
        if tempelem not in res:
            yield tempelem
            res.append(tempelem)
        tempelem = ""


print("second way:", )
perms = permutes_gen2(set_of_words)
for i in perms:
    print(i, end=" ")


# stdout:
# first way:
# яcлишкомстар ястарcлишком cлишкомястар cлишкомстаря старяcлишком старcлишкомя
#
# second way:
# cлишкомстаря cлишкомястар старcлишкомя старяcлишком яcлишкомстар ястарcлишком


# ИТОГ: знание стандартной библиотеки похвально, однако свои функции и методы надо бы писать получше 3/7
