import re


class Processor:
    """
    адаптер позволяющий выводить слова в подярке очередности начиая с наиболее редко появляющихся
    """
    def process_text(self, text):
        return [word for word, _ in sorted([(word, counter) for word, counter in WordCounter(text).get_all_words().items()], key=lambda pair: pair[1])]


class TextParser:
    """Парсер текстовых данных в некой системе."""

    def __init__(self, text: str):
        tmp = re.sub(r'\W', ' ', text.lower())  # удаляем все что не текст, буквы и _
        tmp = re.sub(r' +', ' ', tmp).strip()
        self.text = tmp

    def get_processed_text(self, processor) -> None:
        """Вызывает метод класса обработчика.

        :param processor: экземпляр класса обработчика
        """
        result = processor.process_text(self.text)
        print(*result,sep="\n")

    def __str__(self):
        return self.text


class WordCounter:
    """Счётчик частотности слов в тексте."""

    def __init__(self, text: str) -> None:
        """Обрабатывает переданный текст и создаёт словарь с частотой слов."""
        self.__words = {x: text.split().count(x) for x in text.split()}

    def get_count(self, word: str) -> int:
        """Возвращает частоту переданного слова."""
        return self.__words.get(word, 0)

    def get_all_words(self) -> dict[str, int]:
        """Возвращает словарь с частотой слов."""
        return self.__words.copy()


proc = Processor()
texto = TextParser("пять пять пять пять пять три три три один четыре четыре четыре четыре !@№;%:%;№: два два")
texto.get_processed_text(proc)

"""
один
два
три
четыре
пять
"""
