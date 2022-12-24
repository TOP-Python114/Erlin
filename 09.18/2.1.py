# Passenger & Cargo Carriers
from abc import abstractmethod, ABC


class Carrier(ABC):
    """
    абстрактный класс назначения груза
    """

    @abstractmethod
    def carry_military(self, items):
        pass

    @abstractmethod
    def carry_commercial(self, items):
        pass


class Cargo(Carrier):
    """
    класс груза
    """

    def carry_military(self, items):
        """Выводит в stdout описание военного грузового самолета"""
        print(f"Военный самолет перевозящий {items} тонн груза ")

    def carry_commercial(self, items):
        """Выводит в stdout описание грузового гражданского самолета """
        print(f"Гражданский самолет перевозящий {items} тонн груза")


class CargoMail(Cargo):
    """
    класс почта
    """

    def carry_military(self, items):
        """Выводит в stdout описание самолета военной спецсвязи"""
        print(f"Самолет военной спецсвязи везет {items} единиц секретной почты")

    def carry_commercial(self, items):
        """Выводит в stdout описание почтового самолета"""
        print(f"Гражданский самолет перевозящий {items} почтовых отправлений")


class Passengers(Carrier):
    """класс пассажиров"""

    def carry_military(self, items):
        """Выводит в stdout описание военно-транспортного самолета"""
        print(f"В военный самолет село {items} солдат ")

    def carry_commercial(self, items):
        """Выводит в stdout описание транспортного самолета"""
        print(f"В самолет село {items} пассажиров")


# Military & Commercial Planes
class Plane(ABC):
    """
    абстрактный класс назначения самолета
    """
    def __init__(self, carry: Carrier, objects):
        self.carrier = carry
        self.objects = objects

    @abstractmethod
    def display_description(self):
        """
        Выводит в stdout готовое описание объекта
        :return: None
        """
        pass

    @abstractmethod
    def add_objects(self, new_objects: int):
        """
        Добавляет нужное количество груза / пассажиров / почты
        :param new_objects: количество груза / пассажиров / почты
        :return: None
        """
        pass


class Commercial(Plane):
    """
    класс коммерческого (гражданского) самолета
    """

    def display_description(self):
        """Выводит в stdout описание назначения коммерческого самолета"""
        self.carrier.carry_commercial(self.objects)

    def add_objects(self, new_objects):
        """Добавляет объекты: коммерческого груза / людей """
        self.objects += new_objects


class Military(Plane):
    """
    класс военного самолета
    """

    def display_description(self):
        """Выводит в stdout описание военного самолета"""
        self.carrier.carry_military(self.objects)

    def add_objects(self, new_objects):
        """Добавляет объекты: военного груза / солдат / почты"""
        self.objects += new_objects


cargo = Cargo()
pass_ = Passengers()
post = CargoMail()
commercial_car = Commercial(cargo, 150)
military_pass = Military(pass_, 300)
mil_post = Military(post, 1000)
mil_post.add_objects(400)
commercial_car.display_description()
military_pass.display_description()
mil_post.display_description()

"""
В самолет загружено 150 тонн гражданского груза
В самолет село 300 солдат 
Самолет военной спецсвязи везет 1000 единиц секретной почты
"""


# ИТОГ: очень хорошо — 6/6
