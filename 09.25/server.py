from abc import ABC, abstractmethod
from socket import socket, AF_INET, SOCK_STREAM


class Request(ABC):
    @abstractmethod
    def next_request(self, request: "Server"):
        """Передает выполнение команды следующему в цепочке ответственности."""
        pass

    @abstractmethod
    def execute(self, order: int):
        """Принимает команду на исполнение."""
        pass


# ИСПРАВИТЬ: нарушение SRP — обработку цепочки запросов и запуск сервера стоит разделить на разные классы
class Server(Request):
    # КОММЕНТАРИЙ: который...?
    """Класс TCP сервер, который """

    def __init__(self):
        self.__next_request = None

    def next_request(self, request: Request):
        """Реализует абстрактный метод next_request."""
        self.__next_request = request
        return request

    def execute(self, order: str):
        """Исполняет переданный в него запрос."""
        if self.__next_request is not None:
            return self.__next_request.execute(order)
        return "Отправленного вами запроса не существует"

    @staticmethod
    def send_request(string):
        ok = OK()
        forbidden = Forbidden()
        not_found = NotFound()
        internal = InternalServerError()

        ok.next_request(forbidden).next_request(not_found).next_request(internal)
        return ok.execute(string)

    @classmethod
    def start_server(cls):
        serv_sock = socket(AF_INET, SOCK_STREAM, proto=0)
        serv_sock.bind(('', 11111))
        serv_sock.listen(10)

        while True:
            client_sock, client_addr = serv_sock.accept()
            while True:
                data = client_sock.recv(1024)
                if not data:
                    break
                client_sock.sendall(cls.send_request(data.decode("utf-8")).encode("utf-8"))

            client_sock.close()


class OK(Server):
    """Запрос 200."""

    def execute(self, order: str):
        if order == '200':
            return "Code 200 - OK"
        else:
            return super().execute(order)


class Forbidden(Server):
    """Запрос 403."""

    def execute(self, order: str):
        if order == '403':
            return "Code 403 : Forbidden!"
        else:
            return super().execute(order)


class NotFound(Server):
    """Запрос 404."""

    def execute(self, order: str):
        if order == '404':
            return "Code 404 - Not found"
        else:
            return super().execute(order)


class InternalServerError(Server):
    """Запрос 500."""

    def execute(self, order: str):
        if order == '500':
            return "Code 500 : Internal Server Error!"
        else:
            return super().execute(order)


if __name__ == "__main__":
    # КОММЕНТАРИЙ: ваш сервер (и обработчик цепочки тоже) написан так, что создание экземпляра ему не требуется
    Server().start_server()
