from itertools import permutations
import time
from random import randint


class Generator:
    @staticmethod
    def generate(count: int):
        return [randint(1, 9) for _ in range(count)]


class Splitter:
    @staticmethod
    def split(array) -> list:
        result = []

        row_count = len(array)
        col_count = len(array[0])

        for r in range(row_count):
            the_row = []
            for c in range(col_count):
                the_row.append(array[r][c])
            result.append(the_row)

        for c in range(col_count):
            the_col = []
            for r in range(row_count):
                the_col.append(array[r][c])
            result.append(the_col)

        diag1 = []
        diag2 = []

        for c in range(col_count):
            for r in range(row_count):
                if c == r:
                    diag1.append(array[r][c])
                r2 = row_count - r - 1
                if c == r2:
                    diag2.append(array[r][c])

        result.append(diag1)
        result.append(diag2)

        return result


class Verifier:
    @staticmethod
    def verify(arrays) -> bool:
        first = sum(arrays[0])

        for i in range(1, len(arrays)):
            if sum(arrays[i]) != first:
                return False

        return True


class MagicSquareGenerator:
    def __init__(self, width: int):
        self.w = width
        self.gen = Generator()
        self.ver = Verifier()
        self.sp = Splitter()

    def generate(self):
        while True:
            self.res = [self.gen.generate(self.w) for _ in range(self.w)]
            if self.ver.verify(self.sp.split(self.res)):
                return "\n".join(map(lambda a: "  ".join(map(str,a)), self.res))

    def joke_generate(self):
        """
        генерация "магического" квадрата
        :return:
        """
        ran = randint(1, 9)
        return "\n".join(map(lambda a: "  ".join(map(str, a)), [[ran for _ in range(self.w)] for _ in range(self.w)]))


a = MagicSquareGenerator(3)

print(a.joke_generate())



time_ = time.time()
print(a.generate())
print(time.time() - time_)

"""
5  5  5
5  5  5
5  5  5
3  9  6
9  6  3
6  3  9
"""