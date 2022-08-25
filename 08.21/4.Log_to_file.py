# ИСПОЛЬЗОВАТЬ: применяйте более современный и удобный модуль pathlib для работы с путями и файлами
from pathlib import Path
from sys import argv
from time import sleep

# ИСПОЛЬЗОВАТЬ: правильно указывайте путь до каталога с файлом скрипта
logfile = Path(argv[0]).parent / 'log.txt'

def logging(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        # ИСПОЛЬЗОВАТЬ: нет нужды в проверке на существование файла — будучи открытым в режиме добавления, этот файл будет создан, если ещё не существует
        #               а вот кодировку лучше указать, так как по умолчанию данный параметр будет определён ОС
        with open(logfile, "a", encoding='utf-8') as fp:
            fp.write(f"name: {func.__name__} \n"
                     f"\tpositional args: {args} \n"
                     f"\tkeyword args: {kwargs} \n\n")
    return wrapper


@logging
def sleepy(*args, **kwargs):
    sleep(1)

@logging
def printy(wordy):
    print(wordy)

sleepy(d=6)
printy("romero")

# КОММЕНТАРИЙ: файл журнала зачем убрали под игнор? в задании писал: прикрепить


# ИТОГ: хорошо — 5/6
