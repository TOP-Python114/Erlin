# у меня ни в какую не хочет работать 3.10
from __future__ import annotations
from pathlib import Path
from typing import Union
from sys import argv

index_file = Path(argv[0]).parent / 'index.html'


class HTMLElement:
    default_indent_size = 4
    NOT_CLOSING_TAGS = ["img", "br", "meta"]

    def __init__(self, name: str, value: str = '', **attrs):
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
    def __init__(self, root: str | HTMLElement, **attrs):
        if isinstance(root, str):
            self.__root = HTMLElement(root, **attrs)
        elif isinstance(root, HTMLElement):
            self.__root = root

    def add_child(self, name: str, value: str = '', **attrs):
        self.__root.elements += [
            el := HTMLElement(name, value, **attrs)
        ]
        return HTMLBuilder(el)

    def add_sibling(self, name: str, value: str = '', **attrs):
        self.__root.elements += [
            HTMLElement(name, value, **attrs)
        ]
        return self

    def __str__(self):
        return str(self.__root)

    def to_html(self):
        with open(index_file, "w", encoding="utf8") as fp:
            fp.write(str(self))
        return self


class CVBuilder:
    def __init__(self, full_name: str, age: int, field_of_activity: str, portfolio: list[str] = None, **contacts):
        self.full_name = full_name
        self.age = age
        self.foa = field_of_activity
        self.contacts: list = [contacts]
        self.portfolio = portfolio
        self.education: str = ""
        self.projects: list[dict] = []
        self.html = None
        self.body = None

    def add_education(self, *education: str | int):
        self.education = ", ".join(map(str, education))
        return self

    def add_project(self, *project):
        self.projects += [project]
        return self

    def add_contact(self, **contact):
        self.contacts += [contact]
        return self

    def build(self):

        self.html = HTMLBuilder("html")
        self.head = self.html.add_child("head").add_sibling("meta", content="text/html", charset="utf-8").add_sibling(
            "title", f"Портфолио: {self.full_name}")
        self.body = self.html.add_child("body")
        about = self.body.add_child("div", id="about").add_sibling("h2", "Обо мне")

        if self.education:
            about.add_sibling("p", "Образование: " + self.education)

        if self.projects:
            for project in self.projects:
                tempp = about.add_child("div", f"{project[0]}")
                tempp.add_sibling("br")
                # есть ли картинки в проектах
                if len(project) > 1:
                    for image in project[1:]:
                        tempp.add_child("img", src=image, width="80px", height="80px")

        for contact in self.contacts:
            about.add_sibling("p", f"{contact}"[1:-1])
        self.body.add_sibling("style",
                              "#about{background-color:darkgrey;margin-left: 40%;padding: 10px 50px 10px;width:200px;})")

        return self.html


cv1 = CVBuilder('Иванов Иван Иванович', 26, 'художник-фрилансер', email='ivv@abc.de') \
    .add_education("Новосибирский Государственный Университет", "Мехмат", 2005) \
    .add_contact(telegram="@gmaoof") \
    .add_project("Проект №1", "https://semantica.in/wp-content/uploads/2017/12/580b57fcd9996e24bc43c4c4-300x300-2.png",
                 "https://st2.depositphotos.com/1014014/7742/i/600/depositphotos_77422142-stock-photo-references-check-mark-sign-concept.jpg") \
    .add_project("Проект №2",
                 "https://semantica.in/wp-content/uploads/2017/12/580b57fcd9996e24bc43c4c4-300x300-2.png",
                 "https://st2.depositphotos.com/1014014/7742/i/600/depositphotos_77422142-stock-photo-references-check-mark-sign-concept.jpg") \
 \
    .build().to_html()

print(cv1)
