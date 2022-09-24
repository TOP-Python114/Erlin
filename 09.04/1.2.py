# у меня ни в какую не хочет работать 3.10
from __future__ import annotations


class HTMLElement:
    default_indent_size = 4

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
