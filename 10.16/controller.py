import re

from model import Email
from view import CLIView


class Application:
    """класс контроллер"""
    def __init__(self, view: CLIView):
        self.em = None
        self.view = view

    def start(self)->None:
        "Приветствует и начинает проверку"
        self.view.start_view()
        self.check_email()

    def one_else(self):
        "Зацикливает ввод почты"
        param = input("еще?\n")
        if param in ('y', 'Y', 'д', "Д"):
            return self.check_email()
        else:
            self.end()

    def check_email(self) -> None:
        """Проверяет почту"""
        try:
            self.em = Email(self.view.input_email())
            print("почта в порядке")
            save_or_not = input("Сохранить?\n")
            if save_or_not in ('y', 'Y', 'д', "Д"):
                self.save_email()
                self.one_else()
            else:
                self.end()
        except ValueError:
            print("Неверная почта")
            self.one_else()


    def save_email(self)->None:
        """СОхраняет почту"""
        self.em.save()

    def end(self)->None:
        """Завершает работу"""
        self.view.end_view()


#if __name__ == '__main__':

app = Application(CLIView())
app.start()
