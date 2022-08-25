from os import path
from time import sleep


def logging(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        if path.exists("log.txt"):
            with open("log.txt", "a") as fp:
                fp.write(f"name: {func.__name__} \n"
                         f"\tpositional args: {args} \n"
                         f"\tkeyword args: {kwargs} \n\n")
        else:
            with open("log.txt", "w") as fp:
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