from pathlib import Path
from sys import argv
import datetime

class BNSh:
    # ДОБАВИТЬ: не ленитесь формулировать и писать документацию — это отлично помогает структурировать собственные мысли и лучше понять задачу
    def __init__(self):
        # КОММЕНТАРИЙ: вот это полезный атрибут
        self.processing = False
        self.logging = False
        # ДОБАВИТЬ: словарь с командами: результатами
        # ДОБАВИТЬ: хранилище последних команд

    # ДОБАВИТЬ: документацию метода
    def start(self):
        self.processing = True

    # ДОБАВИТЬ: документацию метода
    def interprete(self, command):
        # ДОБАВИТЬ: здесь должна происходить вся обработка команд

        # УДАЛИТЬ: если уж вынесли пользовательский ввод в код верхнего уровня, то стоило и экземпляр команды там же создавать и передавать сюда в качестве аргумента
        self.command = Command(command)

        if self.command.res_of_com() != 'exit':
            com1 = self.command.res_of_com()
            if command == "logging":
                self.logging = True
            if self.logging:
                self.logfile = Path(argv[0]).parent / 'log.txt'
                with open(self.logfile, "a", encoding='utf-8') as fp:
                    fp.write(f"{datetime.datetime.now()} {self.command} -> {com1} \n")
            return com1

        self.exit()

    # ДОБАВИТЬ: документацию метода
    def exit(self):
        self.processing = False
        return "good bye"


# КОММЕНТАРИЙ: по условию задачи этот класс нужен для обработки пользовательского ввода, передачи его на обработку оболочке, и вывода результатов обработки — это и есть выполнение команды с точки зрения данного класса
class Command:
    # ДОБАВИТЬ: не ленитесь формулировать и писать документацию — это отлично помогает структурировать собственные мысли и лучше понять задачу
    def __init__(self, command: str):
        self.command = command
        # УДАЛИТЬ: этот словарь должен быть в классе, который отвечает за обработку — BNSh в вашем случае
        self.commands = {"command1": "output of command1", "command2": "output of command2",
                         "command3": "output of command3", "logging": "logging is on"}
        # ДОБАВИТЬ: атрибут для аргументов команды
        # ДОБАВИТЬ: атрибут для результата команды

    # УДАЛИТЬ: тоже должно быть в классе BNSh
    def help(self):
        return "\n".join([f"команда: {c}\tрезультат: {r}" for c, r in self.commands.items()])

    # УДАЛИТЬ: нарушение принципа единственной ответственности: в нашем классе команды не должно быть обработки команды — экземпляр команды нужен для хранения пользовательского ввода — самой команды и её аргументов — и результата, который выдаёт обработчик команды (опциональными атрибутами могут быть метка времени, код выполнения и прочая техническая информация)
    def res_of_com(self):
        if self.command == 'exit':
            return "exit"
        if self.command == 'help':
            return self.help()
        if self.command in self.commands.keys():
            return self.commands[self.command]
        return f"{self.command} не является командой"

    def __str__(self):
        # ИСПРАВИТЬ: здесь стоит оставить вывод только результата команды
        return self.command

    # ДОБАВИТЬ: а в методе __repr__() вернуть строку, содержащую саму команду и её аргументы — удобно для дальнейшего поиска в истории команд


shell = BNSh()
shell.start()
while shell.processing:
    print(">>> ", end="")
    print(shell.interprete(input()))
    # ИСПОЛЬЗОВАТЬ: вот так я бы это использовал, если оставаться близко к вашему коду
    # c = Command(input('>>> '))
    # shell.interprete(c)
    # print(c)


# ИТОГ: хорошая попытка, доработайте — 4/7
