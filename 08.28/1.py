from pathlib import Path
from sys import argv
import datetime

class BNSh:
    def __init__(self):
        self.processing = False
        self.logging = False

    def start(self):
        self.processing = True

    def interprete(self, command):
        self.command = Command(command)

        if self.command.res_of_com() != 'exit':
            com1 = self.command.res_of_com()
            if command == "logging":
                self.logging = True
            if self.logging:
                self.logfile = Path(argv[0]).parent / 'log.txt'
                with open(self.logfile, "a", encoding='utf-8') as fp:
                    fp.write(f"{datetime.datetime.now()}  command: {self.command},результат: {com1} \n")
            return com1

        self.exit()

    def exit(self):
        self.processing = False
        return "good bye"


class Command:
    def __init__(self, command: str):
        self.command = command
        self.commands = {"command1": "output of command1", "command2": "output of command2",
                         "command3": "output of command3", "logging": "logging is on"}
    def help(self):
        return "\n".join([f"команда:{c} результат:{r}" for c,r in self.commands.items()])

    def res_of_com(self):
        if self.command == 'exit':
            return "exit"
        if self.command == 'help':
            return self.help()
        if self.command in self.commands.keys():
            return self.commands[self.command]
        return f"{self.command} не является командой"

    def __str__(self):
        return self.command


interpret = BNSh()
interpret.start()
while interpret.processing:
    print(">>>", end="")
    print(interpret.interprete(input()))
