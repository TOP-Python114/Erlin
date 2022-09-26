from abc import ABC, abstractmethod
from random import choice

# ДОБАВИТЬ: строки документации для классов и методов!
# ДОБАВИТЬ: аннотации типов параметров!


class Dish(ABC):
    def __init__(self, dish, description, making_method, price, how_to_eat, type_):
        self.dish = dish
        self.description = description
        self.making_method = making_method
        self.price = price
        self.hte = how_to_eat
        self.type_ = type_

    @abstractmethod
    def eat(self):
        pass

    def __str__(self):
        return f"Блюдо: {self.dish}\n" \
               f"Описание: {self.description}\n" \
               f"Способ приготовления: {self.making_method}\n" \
               f"Цена: {self.price}\n" \
               f"Способ употребления: {self.hte}\n" \
               f"Кухня: {self.type_}"


class Pasta(Dish):
    def eat(self):
        print('Едим пасту')


class Pizza(Dish):
    PIZZA_SIZES = {
        "size30": 400,
        "size40": 500,
        "size50": 600}
    def eat(self):
        print('Едим пиццу')


class Curry(Dish):
    def eat(self):
        print('Едим карри')

# ДОБАВИТЬ: больше классов блюд — выбрать не из чего....)



class CuisineFactory(ABC):
    @staticmethod
    @abstractmethod
    def serve(*args):
        pass

# КОММЕНТАРИЙ: боюсь, вы не поняли смысл задачи — у нас должно быть фабрик по числу кухонь: каждая фабрика возвращает не отдельное блюдо, а набор или наборы блюд определённой кухни, выступая таким образом ещё и как фильтр

#  ДОБАВИТЬ: реализации фабрик, пример использования, вывод примера


# stdout:


# ИТОГ: переработать — 3/6
