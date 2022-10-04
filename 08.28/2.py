"""Упражнение 67. Найти периметр многоугольника
Напишите программу для расчета периметра заданного многоугольника.
Начните с запроса у пользователя координат x и y первой точки многоугольника. Продолжайте запрашивать координаты следующих точек фигуры, пока пользователь не оставит строку ввода координаты по оси x пустой.
После ввода каждой пары значений вы должны вычислить длину очередной стороны многоугольника и прибавить полученное значение к будущему ответу.
По окончании ввода необходимо вычислить расстояние от последней введенной точки до первой, чтобы замкнуть фигуру, и вывести итоговый результат.

Для задачи №67 из Стивенсона реализуйте объектную модель из трёх классов: Polygon, LineSegment, Point.
Используйте композицию. Для расчёта значений используйте геттеры/сеттеры.
"""
from dataclasses import dataclass
from itertools import pairwise


@dataclass
class Point:
    x: int
    y: int

@dataclass
class LineSegment:
    point1:Point
    point2:Point

    @property
    def length(self):
        """Рассчитывает длину отрезка."""
        return ((self.point1.x - self.point2.x) ** 2
                + (self.point1.y - self.point2.y) ** 2) ** 0.5

#крутая тема унаследоваться от листа
class Polygon(list):
    def __init__(self: list[Point]):
        super().__init__()
    #Поясните пожалуйста зачем нужен конструктор?

    @property
    def perimeter(self):
        # ИСПРАВИТЬ: документацию функции
        """Вычисляет периметр"""
        if len(self) > 2:
            return sum([LineSegment(*segment).length for segment in pairwise(self + [self[0]])])
        else:
            raise ValueError("Минимум три точки")


poly = Polygon()
#
while True:
    x = input("Введите x: ")
    if not x:
        break
    y = input("введите y: ")
    try:
        y = int(y)
        x = int(x)
        poly.append(Point(int(x), int(y)))
    except ValueError:
        print("неверный формат")
        break


print(poly.perimeter)


# stdout:
"""
Введите x: 4
введите y: 3
Введите x: 1
введите y: 3
Введите x: 4
введите y: 7
Введите x: 
12.0
"""

# ИТОГ: неплохо, но можно лучше — 3/5

