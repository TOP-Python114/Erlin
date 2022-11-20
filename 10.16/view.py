"""CLI представление MVC."""

from time import sleep


class CLIView:
    def start_view(self) -> None:
        print('Приветствую в валидаторе электронной почты')
        sleep(1)

    def input_email(self) -> str:
        prompt = 'Введите почту\n'
        email = input(prompt)
        return email

    def end_view(self) -> None:
        print('Пока!')
        sleep(2)
