from dataclasses import dataclass
from datetime import datetime as dt
from random import randrange as rr, choice as ch
from string import ascii_lowercase as alc
from typing import Optional


@dataclass
class Serb:
    name: str

    def __str__(self):
        return self.name


class SomeModifier:
    """Класс цепочки, запускает обработку данных."""

    def __init__(self, some_tc: 'TestCase'):
        self.cache = []
        self.history: list[list[str, list | str | Serb]] = []
        self.stc = some_tc
        self.previous_modifier: Optional[SomeModifier] = None
        self.next_modifier: Optional[SomeModifier] = None

    def add_modifier(self, modifier: 'SomeModifier'):
        """Формирует звено цепочки."""
        if self.next_modifier is None:
            self.next_modifier = modifier
            self.next_modifier.previous_modifier = self
        else:
            self.next_modifier.add_modifier(modifier)

    def undo(self):
        self.next_modifier = None
        if self.previous_modifier:
            self.previous_modifier.undo()
        self.previous_modifier = None

    def print_msg(self):
        msg = self.stc.messages.pop()
        self.cache += [msg]
        self.history += [[str(dt.now()), "Печать сообщения", msg]]
        print(msg)

    def sum_nums(self):
        nums = self.stc.numbers.pop()
        self.cache += [nums]
        self.history += [[str(dt.now()), "Печать суммы последнего элемента", nums]]
        print(sum(nums))

    def marry_two_serbians(self):
        serb1 = self.stc.serbian_lastnames.pop()
        serb2 = self.stc.serbian_lastnames.pop()
        self.history += [[str(dt.now()), "Женитьба сербов", (serb1.name, serb2.name)]]
        print(f"{serb1}+{serb2}")
        self.cache += [serb1] + [serb2]

#
class AllModifiers(SomeModifier):
    """
    класс универсальный модификатор
    """
    def print_msg(self):
        super().print_msg()

    def sum_nums(self):
        super().sum_nums()

    def marry_two_serbians(self):
        super().marry_two_serbians()

    def undo(self):
        """
        отмена последней модификации
        :return:
        """
        if isinstance(self.cache[-1], list):
            self.history += [[str(dt.now()), "отмена операции", f" возвращение удаленного списка чисел {self.cache[-1]}"]]
            self.stc.numbers += [self.cache.pop()]
        elif isinstance(self.cache[-1], str):
            self.history += [[str(dt.now()), "отмена операции", f" возвращение удаленного сообщения {self.cache[-1]}"]]
            self.stc.messages += [self.cache.pop()]
        elif isinstance(self.cache[-1], Serb):
            self.history += [[str(dt.now()), "отмена операции", f" возвращение сербов в стек холостых {self.cache[-1]} и {self.cache[-2]}"]]
            self.stc.serbian_lastnames += [self.cache.pop()]
            self.stc.serbian_lastnames += [self.cache.pop()]

        super().undo()


class TestCase:
    messages: []
    numbers: []
    serbian_lastnames: []

    def __init__(self):
        self.messages = [
            ''.join(ch(alc) for _ in range(rr(3, 6)))
            for _ in range(10)
        ]
        self.numbers = [
            [rr(10, 100) for _ in range(rr(4, 7))]
            for _ in range(10)
        ]
        self.serbian_lastnames = [
            Serb(ch(["Йовано", "Ивано", "Петро", "Михайло", "Нико", "Родолюбо", "Цвияно", "Йо"]) + ch(
                ["вич", "шич", "лич", "ич"])) for _ in range(10)]


tc = TestCase()
root = AllModifiers(tc)
root.sum_nums()
root.marry_two_serbians()
root.print_msg()
root.undo()
root.undo()
root.undo()
for command in root.history:
    print(f"{command[0]} : {command[1]} - {command[-1]}")

"""
151
Цвияношич+Петрович
gkd
2022-09-29 16:50:55.127739 : Печать суммы последнего элемента - [45, 24, 45, 37]
2022-09-29 16:50:55.127739 : Женитьба сербов - ('Цвияношич', 'Петрович')
2022-09-29 16:50:55.127739 : Печать сообщения - gkd
2022-09-29 16:50:55.127739 : отмена операции -  возвращение удаленного сообщения gkd
2022-09-29 16:50:55.127739 : отмена операции -  возвращение сербов в стек холостых Петрович и Цвияношич
2022-09-29 16:50:55.127739 : отмена операции -  возвращение удаленного списка чисел [45, 24, 45, 37]
"""