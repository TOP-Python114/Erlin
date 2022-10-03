# КОММЕНТАРИЙ: так не описывают проблему — тренируйтесь содержательно формулировать свои наблюдения
# виноват
# ДОБАВИТЬ: строки документации для классов и методов!

class HTMLElement:
    """
    attrs - аттрибуты тега имя:значение
    класс - HTML тэг, конструктор позволяет получить имя тега, его значение и выставить аттрибуты и их значение
    """
    default_indent_size = 4

    def __init__(self, name: str, value: str = '', **attrs: str):
        self.name = name
        self.value = value
        self.elements: list['HTMLElement'] = []
        # ДОБАВИТЬ: аннотацию типа для атрибута attrs
        self.attrs = "".join([f' {n}="{v}"' for n, v in attrs.items()])

    def __str__(self):
        return self.__str()

    def __str(self, indent_lvl: int = 0):
        """
        Приводит к строке тег (финт ушами для возможности использования рекурсии)
        :param indent_lvl: уровень отступа
        :return: тег с вычисленным отступом
        """
        indent = ' ' * indent_lvl * self.__class__.default_indent_size
        ret = f'{indent}<{self.name}{self.attrs}>{self.value}'
        if self.elements:
            for element in self.elements:
                ret += '\n' + element.__str(indent_lvl + 1)
            ret += f'\n{indent}</{self.name}>'
        else:
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

    def add_child(self, name: str, value: str = '', **attrs: str):
        """
        добаваляет в себя дочерний элемент
        :attrs - дикт со именем и значением аттрибута
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


# ручное создание элементов и связей между ними
# li1 = HTMLElement('li', 'элемент 1')
# li2 = HTMLElement('li', 'элемент 2')
# ul = HTMLElement('ul')
# ul.elements += [li1, li2]
# div = HTMLElement('div')
# div.elements += [ul]
# print(div)

# использование строителя
body = HTMLBuilder("body", id="body_bro")
menu = body.add_child('div', id="block1", display="flex").add_child('ul')
menu.add_child('li', 'File') \
    .add_sibling('p', 'New') \
    .add_sibling('p', 'Open') \
    .add_sibling('p', 'Save')
menu.add_child('li', 'Edit') \
    .add_sibling('p', 'Undo') \
    .add_sibling('p', 'Redo') \
    .add_sibling('p', 'Cut') \
    .add_sibling('p', 'Copy') \
    .add_sibling('p', 'Paste')
print(body)

# stdout:
"""
<body id="body_bro">
    <div id="block1" display="flex">
        <ul>
            <li>File
                <p>New</p>
                <p>Open</p>
                <p>Save</p>
            </li>
            <li>Edit
                <p>Undo</p>
                <p>Redo</p>
                <p>Cut</p>
                <p>Copy</p>
                <p>Paste</p>
            </li>
        </ul>
    </div>
</body>
"""

# ИТОГ: с документацией было бы очень хорошо — 3/4
