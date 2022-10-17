from itertools import permutations
import time
from random import randint


class Generator:
    """Класс одного статического метода формирующего список случайного числа от 1 до 9"""

    @staticmethod
    def generate(count: int)->list:
        """Формирует список случайного числа от 1 до 9"""
        return [randint(1, 9) for _ in range(count)]


class Splitter:
    """Класс разбивающий квадрат на линии, идентичность которых в дальнейшем необходимо верифицировать"""

    @staticmethod
    def split(array: list[list]) -> list:
        """Разбивает 2d список на списки """
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
    """Класс верифицирующий квадрат"""

    @staticmethod
    def verify(arrays: list[list]) -> bool:
        """Верификация списков (Тру если все списки равны по сумме)"""
        first = sum(arrays[0])

        for i in range(1, len(arrays)):
            if sum(arrays[i]) != first:
                return False

        return True


class MagicSquareGenerator:
    """Класс формирующий магический квадрат"""

    def __init__(self, width: int):
        self.w = width
        self.gen = Generator()
        self.ver = Verifier()
        self.sp = Splitter()

    def generate(self)->str:
        """Генерирует квадрат с одинаковыми суммами по горизонтали, вертикали, диагонали"""
        while True:
            self.res = [self.gen.generate(self.w) for _ in range(self.w)]
            if self.ver.verify(self.sp.split(self.res)):
                return "\n".join(map(lambda a: "  ".join(map(str, a)), self.res))

    def joke_generate(self)->str:
        """
        генерация идеального "магического" квадрата
        :return: строковое представление квадрата
        """
        ran = randint(1, 999999)
        return ("\n" * self.w).join(
            map(lambda a: " ".join(a), [[str(ran) for _ in range(self.w)] for _ in range(self.w)]))


a = MagicSquareGenerator(3)

print(a.joke_generate())

time_ = time.time()
print(a.generate())
print(time.time() - time_)

"""
915077 915077 915077


915077 915077 915077


915077 915077 915077
7  8  6
6  7  8
8  6  7
"""
