"""CLI представление MVC."""

from time import sleep


class CLIView:
    # ИСПРАВИТЬ здесь и далее: если у вас де-факто получился статический метод, то декорируйте его как статический и уберите лишние параметры
    def start_view(self) -> None:
        print('Приветствую в валидаторе электронной почты')
        # УДАЛИТЬ: искусственная "спячка" аккурат перед запуском пользовательского ввода не нужна
        sleep(1)

    def input_email(self) -> str:
        prompt = 'Введите почту\n'
        email = input(prompt)
        return email

    def end_view(self) -> None:
        print('Пока!')
        sleep(2)
