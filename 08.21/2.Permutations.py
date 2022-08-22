from math import factorial
from random import choice
from itertools import permutations

set_of_words = {"cлишком", "стар", "я"}


# permuts = lambda x: " ".join("".join(x) for x in permutations(x))
# print("first way:", )
# print(permuts(set_of_words))
# print()
# oh, we need a generator ok

def easy_gen(set_of_words: set):
    p=permutations(set_of_words)
    for i in range(factorial(len(set_of_words))):
        yield "".join(p.__next__())


perms = easy_gen(set_of_words)
print("first way:", )
for i in perms:
    print(i,end=" ")
print("\n")

# bad method, but i think it's fun
def permut_2(elements: set) -> str:
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
# print(permut_2({"cлишком", "стар", "я"}))

perms = permut_2(elements=set_of_words)
for i in perms:
    print(i, end=" ")
# Копия вывода в виде комментария помещается в конец файла с кодом задачи.
"""
first way:
яcлишкомстар ястарcлишком cлишкомястар cлишкомстаря старяcлишком старcлишкомя

second way:
cлишкомстаря cлишкомястар старcлишкомя старяcлишком яcлишкомстар ястарcлишком
"""
