from abc import ABC, abstractmethod


class Dish(ABC):
    def __init__(self, name,description, making_method, cost, how_to_eat,type_):
        self.name = name
        self.description = description
        self.making_method = making_method
        self.cost = cost
        self.hte = how_to_eat
        self.type_ = type_

    @abstractmethod
    def eat(self):
        pass


class Pasta(Dish):
    def eat(self):
        print('Едим пасту')


class Curry(Dish):
    def drink(self):
        print('Я не люблю кофе')

class DishFactory(ABC):
    @staticmethod
    @abstractmethod
    def serving():
        pass

class PastaFactory(DishFactory):
    @staticmethod
    def serving():
        return Pasta("Паста","Итальянские макарошки с соусом","варим парим вспе такое",400,"ртом","итальянская")

