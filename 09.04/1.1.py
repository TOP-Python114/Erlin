from __future__ import annotations


class ClassBuilder:
    """
    класс строитель формирующий текст кода класса, с конструктором и без с возможностью добавления полей
    """
    checker=1
    def __init__(self, class_name: str):
        self.cn = class_name
        self.fields: list[tuple[str, str | int | bool]] = []


    def add_field(self, name: str = f"someprop{checker}", value: str | int | bool = "somevalue"):
        """
        метод для добавления полей в список
        :param name: аттрибут
        :param value: значение
        :return: возвращает список кортежей - пар имя аттрибута - значение аттрибута
        """

        # при добавлении нового поля с занятым именем и другим значением его значение перезаписывается
        names = [x for x, _ in self.fields]
        if name not in names:
            self.fields += [(name, value)]
            self.checker+=1
        else:
            self.fields[names.index(name)] = (name, value)

        return self

    def __str__(self):
        """
        формирование готового кода и вывод
        type_chr: нужен для формирования кавычек у строковых значений
        :return: возвращает строковое предтавление готового текста класса
        """
        type_chr = lambda t: isinstance(t, str)
        if not self.fields:
            return f"Class {self.cn.title()}:\n\tpass"
        formatted_fields = '\n\t\t'.join(
            [f"self.{field[0]} = " + "'" * type_chr(field[1]) + f"{field[1]}" + "'" * type_chr(field[1]) for field in
             self.fields])

        return f"Class {self.cn.title()}:\n\tdef __init__(self):\n\t\t{formatted_fields}"


athlete = ClassBuilder("armwrestler")

print(athlete)
print()

athlete.add_field("name", "Alex Kurdecha").add_field("age", 28).add_field("senior", True).add_field("age", 33).add_field().add_field()

print(athlete)

"""
Class Armwrestler:
	pass

Class Armwrestler:
	def __init__(self):
		self.name = 'Alex Kurdecha'
		self.age = 28
		self.senior = True
"""
