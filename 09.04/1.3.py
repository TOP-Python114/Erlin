from pathlib import Path
from typing import Union
from sys import argv

index_file = Path(argv[0]).parent / 'index.html'
# слорносочененная аннотация типов, действительно пишется КэмелКейсом?
FieldProjects = list[tuple[str, tuple]]


#

# ДОБАВИТЬ: строки документации для классов и методов!

class HTMLElement:
    """
      класс - HTML тэг, конструктор позволяет получить имя тега, его значение и выставить аттрибуты и их значение
      attrs - аттрибуты тега
      """
    default_indent_size = 4
    # КОММЕНТАРИЙ: отлично
    NOT_CLOSING_TAGS = ["img", "br", "meta"]

    def __init__(self, name: str, value: str = '', **attrs: str):
        self.name = name
        self.value = value
        self.elements: list['HTMLElement'] = []
        self.attrs = "".join([f' {n}="{v}"' for n, v in attrs.items()])

    def __str__(self):
        return self.__str()

    def __str(self, indent_lvl: int = 0):
        indent = ' ' * indent_lvl * self.__class__.default_indent_size
        ret = f'{indent}<{self.name}{self.attrs}>{self.value}'
        if self.elements:
            for element in self.elements:
                ret += '\n' + element.__str(indent_lvl + 1)
            ret += f'\n{indent}</{self.name}>'
        else:
            if self.name not in self.NOT_CLOSING_TAGS:
                ret += f'</{self.name}>'
        return ret


class HTMLBuilder:
    """
    класс строитель HTML блока | документа
    """

    def __init__(self, root: str | HTMLElement, **attrs: str):
        if isinstance(root, str):
            self.__root = HTMLElement(root, **attrs)
        elif isinstance(root, HTMLElement):
            self.__root = root

    def add_child(self, name: str, value: str = '', **attrs):
        """
           добваляет в себя дочерний элемент
           :param name: имя тега
           :param value: текст внутри тега
           :param attrs: аттрибуты
           :return:
           """
        self.__root.elements += [
            el := HTMLElement(name, value, **attrs)
        ]
        return HTMLBuilder(el)

    def add_sibling(self, name: str, value: str = '', **attrs: str):
        """
       добваляет в себя  элемент "брат"
       :param name: имя тега
       :param value: текст внутри тега
       :param attrs: аттрибуты
       :return:
       """
        self.__root.elements += [
            HTMLElement(name, value, **attrs)
        ]
        return self

    def __str__(self):
        return str(self.__root)

    # КОММЕНТАРИЙ: очень хорошо
    def to_html(self):
        """
        импорт в HTML файл
        :return:
        """
        with open(index_file, "w", encoding="utf8") as fp:
            fp.write(str(self))
        return self


class CVBuilder:
    """
    класс строитель HTML документа
    """
    def __init__(self,
                 full_name: str,
                 age: int,
                 field_of_activity: str,
                 # ДОБАВИТЬ: параметр для обязательного аргумента email
                 # ОТВЕТИТЬ: вы принимаете контакты и в конструкторе, и в отдельном методе — чем оправдана избыточность?
                 # поправил
                 email: str):
        self.full_name = full_name
        self.age = age
        # ИСПРАВИТЬ/УДАЛИТЬ: атрибут не используется
        self.field_of_activity = field_of_activity
        # ДОБАВИТЬ: в общий список контактов обязательный параметр email
        self.contacts: list[tuple[str, str]] = [("email", email)]
        self.education: str = ""
        # ИСПРАВИТЬ: словари ли внутри списка?
        self.projects: FieldProjects = []

        # ОТВЕТИТЬ: эти объекты инициализируются и используются только в одном методе — у вас есть аргументация для того, чтобы записывать их в атрибуты, а не в локальные переменные метода build()?
        # сделал локальными

    # КОММЕНТАРИЙ: удобство использования таких дополнительных методов, как три метода ниже, во многом зависит от того, как вы настроите их сигнатуры — здесь вы предлагаете тому, кто будет их использовать, передавать какие угодно аргументы в каком угодно порядке: следовательно кому-то может захотеться передать сюда явно не учитываемые вами значения

    def add_education(self, education: str):
        """
        добавляет в блок информацию об образовании
        :param education : добавить образование: Вуз , факультет, год
        :return: селф
        """
        # КОММЕНТАРИЙ: а если бы уточнили параметры, то можно было бы, например, дополнить строку с информацией об образовании до предложения
        self.education = education
        return self

    # ИСПРАВИТЬ: мне представляется, что параметры данного метода стоит раскрыть, уже потому, что в методе build() вы используете содержимое каждого кортежа довольно определённым образом: заголовок и изображения — в такой ситуации стоит выделить заголовок в отдельный параметр метода, а уже изображения принимать произвольным кортежем
    # done
    def add_project(self, name: str, *images: str):
        """
        Добавляет проект в список проектов первый элемент кортежа название проекта, второй - кортеж изображений
        :param name: имя проекта
        :images: картинки проекта
        :return:
        """
        self.projects += [(name, images)]
        return self

    def add_contact(self, type_of_contact: str, contact: str):
        """
        :param type_of_contact: тип контакта (мыло, телега...etc)
        :param contact: непосредственно контакт
        :return:
        """
        self.contacts += [(type_of_contact, contact)]
        return self

    def build(self):

        html = HTMLBuilder("html")
        head = html. \
            add_child("head"). \
            add_sibling("meta", content="text/html", charset="utf-8"). \
            add_sibling("title", f"Портфолио: {self.full_name}")
        body = html.add_child("body")

        about = body. \
            add_child("div", id="about"). \
            add_sibling("h2", "Обо мне")

        if self.education:
            about.add_sibling("p", "Образование: " + self.education)

        if self.projects:
            for project in self.projects:
                tempp = about.add_child("div", f"{project[0]}")
                tempp.add_sibling("br")
                # есть ли картинки в проектах
                if project[1]:
                    # КОММЕНТАРИЙ: а здесь точно только картинки?
                    # теперь да
                    for image in project[1]:
                        tempp.add_child("img", src=image, width="80px", height="80px")

        for contact in self.contacts:
            # ИСПРАВИТЬ: не так сложно раскрыть словарь — синтаксические кавычки не очень уместны
            about.add_sibling("p", f"{': '.join(contact)}")

        body.add_sibling(
            "style",
            "#about{background-color:darkgrey;margin-left: 30%;padding: 10px 50px 10px;width:300px;})"
        )
        return html


cv1 = CVBuilder('Иванов Иван Иванович', 26, 'художник-фрилансер', email='ivv@abc.de') \
    .add_education("Новосибирский Государственный Университет, Мехмат, 2005") \
    .add_contact('telegram', "@gmaoof") \
    .add_project(
    "Проект №1",
    # КОММЕНТАРИЙ: есть такая классная штука, как сокращение ссылок — генерирование нового URL, который становится коротким псевдонимом для длинного исходного URL — например, https://clck.ru/
    "https://clck.ru/32EDuN",
    "https://clck.ru/32EDvB") \
    .add_project(
    "Проект №2",
    "https://clck.ru/32EDuN",
    "https://clck.ru/32EDvB").add_project("проект №3") \
    .build().to_html()

print(cv1)

# ИТОГ: весьма хорошо, а с более продуманными методами и документацией было бы ещё лучше — 8/11
