from __future__ import annotations

from math import factorial
from random import choice
from itertools import permutations

set_of_words = {"cлишком", "стар", "я"}


def permutes_gen1(elements: set):
    # ИСПОЛЬЗОВАТЬ: зачем столько лишних действий? если берёте функцию permutations(), то итерировались бы прямо по ней
    for p in permutations(elements):
        yield "".join(p)



# bad method, but i think it's fun
# ИСПРАВИТЬ: как насчёт адекватной собственной функции по нахождению перестановок? смешной вариант можно было предложить третьим, а пока незачёт
#исправил
def permutes_gen2(elements:set|list):
    elements=list(elements)
    if len(elements) <=1:
        yield elements
    else:
        for permutation in permutes_gen2(elements[1:]):
            for i in range(len(elements)):
                yield permutation[:i] + elements[0:1] + permutation[i:]


def permutes_gen3(elements: set) -> str:
    fact_of_set = factorial(len(elements))
    res = list()
    tempelem = ""
    # ИСПРАВИТЬ: не стоит вычислять факториал на каждой итерации
    # исправил
    while len(res) != fact_of_set:
        temp_set = set(elements)
        while temp_set:
            a = choice(list(temp_set))
            tempelem += a
            temp_set.remove(a)
        if tempelem not in res:
            yield tempelem
            res.append(tempelem)
        tempelem = ""

print("first way:")
a=permutes_gen1(set_of_words)
for i in a:
    print("".join(i), end=" ")
print("\n")
print("second way:")
a=permutes_gen2(set_of_words)
for i in a:
    print("".join(i), end=" ")
print("\n")
print("third way:")
perms = permutes_gen3(set_of_words)
for i in perms:
    print(i, end=" ")

# stdout:
# first way:
# яcлишкомстар ястарcлишком cлишкомястар cлишкомстаря старяcлишком старcлишкомя
#
#second way
#слишкомястар яслишкомстар ястарслишком слишкомстаря старслишкомя старяслишком

# third way:
# cлишкомстаря cлишкомястар старcлишкомя старяcлишком яcлишкомстар ястарcлишком


# ИТОГ: знание стандартной библиотеки похвально, однако свои функции и методы надо бы писать получше — 3/7
