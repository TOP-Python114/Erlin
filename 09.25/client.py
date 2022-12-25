from socket import socket, AF_INET, SOCK_STREAM
from tkinter import ttk, StringVar, Button, Label, Tk


class GUInterface:
    def __init__(self):
        self.root = Tk()
        self.root.title('send request')
        self.root.geometry("430x120")

        # ИСПОЛЬЗОВАТЬ: в ситуации, когда нам нужно управлять не самим виджетом, а только данными в нём, мы поступаем наоборот: в атрибут сохраняем связанную переменную, а объект виджета отдельно не сохраняем, только упаковываем
        self.combo_entry = StringVar()
        ttk.Combobox(
            self.root,
            values=["200", "500", "403", "404", "37999"],
            textvariable=self.combo_entry
        ).pack()

        # ИСПРАВИТЬ: здесь аналогично: нас интересует только текст надписи, для которого необходимо создать переменную и записать её в атрибут
        self.output = Label(self.root)
        self.output.pack()

        Button(
            self.root,
            text="Отправить",
            width=10,
            height=1,
            command=self.button_click
        ).pack()

        # КОММЕНТАРИЙ: pack() простой в освоении vs. grid() быстрый в производительности и гибкий в использовании

    def button_click(self):
        self.output.config(text=Client.make_request(self.combo_entry.get()))

    # КОММЕНТАРИЙ: в случае, если в атрибутах прописаны виджеты — тот, кто использует класс графического интерфейса, вынужден взаимодействовать с виджетами и их полями/методами;
    #  а у нас должен получится класс графического интерфейса с полями (атрибутами) тех данных, с которыми работает интерфейс — это и есть создание очередного уровня абстракции, абстрагирование интерфейса


class Client:
    @staticmethod
    def make_request(ats):
        # ИСПОЛЬЗОВАТЬ: здесь отлично работает менеджер контекста:
        with socket(AF_INET, SOCK_STREAM) as client_sock:
            client_sock.connect(('127.0.0.1', 11111))
            client_sock.sendall(ats.encode("utf-8"))
            data = client_sock.recv(1024)

        if data != b" ":
            print(data.decode("utf-8"))
            return data.decode("utf-8")
        else:
            print("Wrong Format")
            return "Wrong format"


if __name__ == "__main__":
    interface = GUInterface()
    interface.root.mainloop()
