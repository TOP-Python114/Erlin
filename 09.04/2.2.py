from abc import ABC, abstractmethod
from random import choice


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
               f"Cпособ употребления: {self.hte}\n" \
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


class DishFactory(ABC):
    @staticmethod
    @abstractmethod
    def serving(*args):
        pass


class PastaFactory(DishFactory):
    @staticmethod
    def serving():
        pst = Pasta("Паста", "Итальянские макарошки с соусом", "варим лапшу, делаем соус", 400,
                    "вилка, большая тарелка", "итальянская")
        pst.eat()
        return pst


class PizzaFactory(DishFactory):
    @staticmethod
    def serving(name: str, size: int):
        return Pizza(f"Пицца: {name}",
                     "Открытый пирог в виде лепешки, покрытой начинками, в первую очередь, расплавленным сыром",
                     "тесто, соус, сыр, топпинги, скомплектовать и запечь", size, "вилка, большая тарелка", "итальянская")


class CurryFactory(DishFactory):
    @staticmethod
    def serving():
        return Curry("Карри", "Курица со специями ", "берем индуса, пусть готовит", 350, "ртом, руками", "индийская")


PIZZAS_NAMES = ["Margarita", "Pepperoni", "Quattro Stagioni", "Napoletana"]
pzs = []
for _ in range(20):
    pzs += [PizzaFactory().serving(choice(PIZZAS_NAMES), choice([Pizza.PIZZA_SIZES[size] for size in ("size30","size40","size50")]))]

for pzz in pzs:
    print(pzz)
    print("\n")
