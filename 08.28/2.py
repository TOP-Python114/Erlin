
"""Упражнение 67. Найти периметр многоугольника
Напишите программу для расчета периметра заданного многоугольника.
Начните с запроса у пользователя координат x и y первой точки много-
угольника. Продолжайте запрашивать координаты следующих точек фи-
гуры, пока пользователь не оставит строку ввода координаты по оси x
пустой. После ввода каждой пары значений вы должны вычислить длину
очередной стороны многоугольника и прибавить полученное значение
к будущему ответу. По окончании ввода необходимо вычислить расстояние
от последней введенной точки до первой, чтобы замкнуть фигуру,
и вывести итоговый результат. Пример ввода координат точек много-
угольника и вывода периметра показан ниже. Введенные пользователем
значения выделены жирным.

Для задачи №67 из Стивенсона реализуйте объектную модель из трёх классов: Polygon, LineSegment, Point.

Используйте композицию. Для расчёта значений используйте геттеры/сеттеры.

"""


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


    def get_x(self):
        """геттер координаты x"""
        return self.x

    def get_y(self):
        """геттер координаты y"""
        return self.y


class LineSegment:
    def __init__(self, point1: 'Point', point2: 'Point'):
        self.point1 = point1
        self.point2 = point2

    def get_length(self):
        """рассчет длины отрезка"""
        return ((self.point1.get_x() - self.point2.get_x()) ** 2 + (
                self.point1.get_y() - self.point2.get_y()) ** 2) ** .5


class Polygon:
    def __init__(self):
        self.poly = list()

    def __len__(self):
        return len(self.poly)

    def add_point(self, point: 'Point'):
        """сеттер точки в полигоне"""
        self.poly.append(point)

    def get_points(self):
        """геттер точек полигона, наверное он не нужен, ибо вычисления периметра идут внутри класса, оставил на память"""
        return self.poly

    def calc_perim(self):
        """вычисление периметра, предусматривает невозможность замыкания отрезка и точки"""
        sum = 0
        for cou_i in range(len(self) - 1):
            sum += LineSegment(poly.get_points()[cou_i], poly.get_points()[cou_i + 1]).get_length()
        return sum + LineSegment(poly.get_points()[0], poly.get_points()[-1]).get_length() if len(self) != 2 else sum


poly = Polygon()

while True:
    x = input("Введите x: ")
    if not x:
        break
    y = input("введите y: ")
    try:
        y=int(y)
        x=int(x)
        poly.add_point(Point(int(x), int(y)))
    except ValueError:
        print("неверный формат")
        break


print(poly.calc_perim())

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