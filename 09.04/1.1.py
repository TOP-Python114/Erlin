
# ИСПОЛЬЗОВАТЬ: для сложносочинённых типов используют отдельные переменные
FieldAttr = list[tuple[str, int | str]]
#ок
class ClassBuilder:
    """Класс строитель формирующий текст кода класса, с конструктором и без с возможностью добавления полей."""
    checker = 1
    def __init__(self, class_name: str):
        self.name = class_name
        self.fields: FieldAttr = []

    def add_field(self,
                  name: str = f"someprop{checker}",
                  # ИСПОЛЬЗОВАТЬ: класс bool наследует от int, поэтому, если вы допускаете возможность передачи обоих, то достаточно указать родительский класс
                  value: str | int = "somevalue"):
        # ИСПРАВИТЬ: строка документации для функции/метода начинается с глагола и одним предложением отвечает на вопрос "что делает функция/метод?" — слово метод избыточно, так как мы это и так видим и в коде, и в документации
        """
        Добавляет поле в список полей

        :param name: аттрибут
        :param value: значение
        :return: возвращает список кортежей - пар имя аттрибута - значение аттрибута
        """
        # при добавлении нового поля с занятым именем и другим значением его значение перезаписывается
        names = [x for x, _ in self.fields]
        if name not in names:
            self.fields += [(name, value)]
            self.checker += 1
        else:
            self.fields[names.index(name)] = (name, value)

        return self

    def __str__(self):
        # УДАЛИТЬ: для специальных методов не используют строки документации, так как уже известно, что делают эти методы и в каких обстоятельствах используются
        #ok
        if not self.fields:
            return f"Class {self.name.title()}:\n" \
                   f"\tpass"

        formatted_fields = '\n\t\t'.join([
            f"self.{field[0]} = "
            # ИСПОЛЬЗОВАТЬ: lambda-функции настоятельно не рекомендуется сохранять в переменные — а в данном случае в этом и нет необходимости
            # намотал на ус
            + "'"*isinstance(field[1], str)
            + f"{field[1]}"
            + "'"*isinstance(field[1], str)
            for field in self.fields
        ])

        return f"Class {self.name.title()}:\n" \
               f"\tdef __init__(self):\n" \
               f"\t\t{formatted_fields}"


athlete = ClassBuilder("armwrestler")

print(athlete)
print()

athlete.add_field("name", "Alex Kurdecha")\
    .add_field("age", 28)\
    .add_field("senior", True)\
    .add_field("age", 33)\
    .add_field()\
    .add_field()

print(athlete)


# stdout:
"""
Class Armwrestler:
	pass

Class Armwrestler:
	def __init__(self):
		self.name = 'Alex Kurdecha'
		self.age = 33
		self.senior = True
		self.someprop1 = 'somevalue'
"""


# ИТОГ: довольно хорошо — 4/5
