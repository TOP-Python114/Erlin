import socket
from tkinter import ttk, StringVar, Button, Label, Tk


class Interface:
    def __init__(self):
        self.root = Tk()
        name = StringVar()
        self.root.title('send request')
        self.root.geometry("430x120")

        self.combo_entry = ttk.Combobox(self.root,
                                        values=[
                                        "200",
                                        "500",
                                        "403",
                                        "404"], textvariable=name)
        self.combo_entry.pack()
        self.output = Label(self.root)
        self.output.pack()
        b1 = Button(self.root, text="Отправить", width=10, height=1, command=self.button_click)
        b1.pack()

    def button_click(self):
        self.output.config(text=Client.make_request(self.combo_entry.get()))

class Client:
    @staticmethod
    def make_request(ats):
        client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_sock.connect(('127.0.0.1', 11111))
        client_sock.sendall(ats.encode("utf-8"))
        data = client_sock.recv(1024)

        client_sock.close()
        if data != b" ":
            print(data.decode("utf-8"))
            return data.decode("utf-8")
        else:
            print("Wrong Format")
            return "Wrong format"


if __name__ == "__main__":
    interface=Interface()
    interface.root.mainloop()
