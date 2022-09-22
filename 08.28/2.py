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


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    # УДАЛИТЬ:
    #  во-первых, это не геттер; в Python геттеры создаются с помощью декоратора property
    #  во-вторых, в условии предлагалось использовать геттеры для расчёта значений — здесь же ничего не происходит
    #  в-третьих, в конструкторе вы объявили атрибут x публичным — зачем такому атрибуту геттер?
    def get_x(self):
        """геттер координаты x"""
        return self.x

    # УДАЛИТЬ: то же самое
    def get_y(self):
        """геттер координаты y"""
        return self.y


class LineSegment:
    def __init__(self, point1: 'Point', point2: 'Point'):
        self.point1 = point1
        self.point2 = point2

    # ИСПОЛЬЗОВАТЬ:
    @property
    def length(self):
        """Рассчитывает длину отрезка."""
        # ИСПОЛЬЗОВАТЬ: вот я заменил вызовы ваших "геттеров" на обращение к атрибутам, и ничего не изменилось, и не изменится ни при каких входных данных — это как раз и говорит о том, что они были бесполезны
        return ((self.point1.x - self.point2.x)**2
                + (self.point1.y - self.point2.y)**2)**0.5


class Polygon:
    def __init__(self):
        self.poly = list()

    def __len__(self):
        return len(self.poly)

    def add_point(self, point: 'Point'):
        # ИСПРАВИТЬ: документация функции начинается с глагола и одним предложением отвечает на вопрос "что делает функция?"
        # КОММЕНТАРИЙ: сеттер — это метод, перезаписывающий значение соответствующего атрибута; метод append() изменяет список не перезаписывая его, следовательно сеттером не является
        """сеттер точки в полигоне"""
        self.poly.append(point)

    def get_points(self):
        # ИСПРАВИТЬ: необходимо разделять документацию и комментарии
        """геттер точек полигона, наверное он не нужен, ибо вычисления периметра идут внутри класса, оставил на память"""
        return self.poly

    def calc_perimeter(self):
        # ИСПРАВИТЬ: документацию функции
        """вычисление периметра, предусматривает невозможность замыкания отрезка и точки"""
        # ИСПРАВИТЬ: sum — это имя встроенной функции, мы не используем имена встроенных функций для своих идентификаторов
        sum = 0
        # ИСПРАВИТЬ: есть замечательная функция pairwise() в модуле itertools стандартной библиотеки
        for cou_i in range(len(self) - 1):
            sum += LineSegment(poly.get_points()[cou_i], poly.get_points()[cou_i + 1]).length
        return sum + LineSegment(poly.get_points()[0], poly.get_points()[-1]).length if len(self) != 2 else sum


poly = Polygon()
#
# while True:
#     x = input("Введите x: ")
#     if not x:
#         break
#     y = input("введите y: ")
#     try:
#         y = int(y)
#         x = int(x)
#         poly.add_point(Point(int(x), int(y)))
#     except ValueError:
#         print("неверный формат")
#         break
#
#
# print(poly.calc_perimeter())


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


# ИСПОЛЬЗОВАТЬ: пример реализации

@dataclass
class Point:
    """Определяет точку на плоскости в декартовой системе координат."""
    x: int
    y: int


@dataclass
class LineSegment:
    """Определяет отрезок на плоскости, заданный двумя точками."""
    p1: Point
    p2: Point

    @property
    def length(self) -> float:
        """Вычисляет длину отрезка."""
        return round(
            ((self.p1.x - self.p2.x)**2 + (self.p1.y - self.p2.y)**2)**0.5,
            1
        )


class Polygon(list):
    """Определяет многоугольник на плоскости, заданный списком точек."""
    def __init__(self: list[Point]):
        super().__init__()

    @property
    def perimeter(self):
        """Вычисляет периметр многоугольника при наличии трёх и более точек в списке."""
        if len(self) > 2:
            return sum(
                LineSegment(p1, p2).length
                for p1, p2 in pairwise(self + [self[0]])
            )
        else:
            raise ValueError('задайте минимум три точки для построения многоугольника')


triangle = Polygon()
triangle.append(Point(0, 0))
triangle.append(Point(3, 4))
try:
    print(triangle.perimeter)
except ValueError as e:
    print(e)
triangle.append(Point(3, 0))
print(triangle.perimeter)
