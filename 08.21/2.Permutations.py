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
    p = permutations(elements)
    for i in range(factorial(len(elements))):
        yield "".join(p.__next__())


perms = permutes_gen1(set_of_words)
print("first way:", )
for i in perms:
    print(i,end=" ")
print("\n")


# bad method, but i think it's fun
def permutes_gen2(elements: set) -> str:
    res = list()
    tempelem = ""
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
