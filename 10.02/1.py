from typing import Optional

from dataclasses import dataclass
from enum import Enum
from string import ascii_lowercase as a_lc

import re


class SquareColor(int, Enum):
    """Цвет поля на доске."""
    LIGHT = 0
    DARK = 1


class PieceColor(Enum):
    """Цвет фигуры."""
    WHITE = 0
    BLACK = 1


class PieceKind(Enum):
    """Вид фигуры."""
    KING = 0
    QUEEN = 1
    ROOK = 2
    BISHOP = 3
    KNIGHT = 4
    PAWN = 5


@dataclass
class Piece:
    """Описывает сущность фигуры."""
    color: PieceColor
    kind: PieceKind
    square: Optional['Square']
    _current_state: int = 0

    # self._changes: list[Memento] = [Memento(start_balance)]

    def __post_init__(self):
        self.removed: bool = False
        self._changes: list['Turn'] = [Turn(self, self.square)]

    def __del__(self):
        """Удаляет фигуру с поля."""
        self.square.piece = None
        self.square = None
        self.removed = True

    def __repr__(self):
        return f'{self.color.name.title()} {self.kind.name.title()}'

    def __str__(self):
        return self.color.name[0] + self.kind.name[0]

    def move(self, end_square: 'Square'):
        """Осуществляет проверку, ход фигуры и взятие фигуры противника."""

        # turn.start = self.square
        # turn.figure = self
        if end_square.piece is not None:
            if end_square.piece.color is self.color:
                # попытка взятия своей фигуры
                raise Exception
            else:
                # взятие фигуры
                del end_square.piece
        state = Turn(self, end_square)
        self.square.piece = None
        self.square = end_square
        end_square.piece = self

        # turn.end = self.square

        # print(end_square)
        self._changes += [state]
        self._current_state += 1
        return self._changes[-1]


@dataclass
class Square:
    """Описывает сущность поля."""
    color: SquareColor
    file: str
    rank: str
    piece: Optional[Piece] = None

    def __repr__(self):
        return f'<{self.file + self.rank}: {self.piece!r}>'

    def __str__(self):
        return self.file + self.rank


class Chessboard(dict):
    """Описывает сущность игровой доски."""

    class File(dict):
        """Вертикаль игровой доски."""

        def __init__(self, file: str, start_color: SquareColor):
            super().__init__()
            for i in range(4):
                for j in range(2):
                    rank = i * 2 + j + 1
                    self[rank] = Square(
                        list(SquareColor)[start_color - j],
                        file,
                        str(rank)
                    )

    def __init__(self):
        """Создаёт и нумерует игровою доску и заполняет её пустыми полями соответствующих цветов."""
        super().__init__()
        for i in range(8):
            for _ in range(4):
                for j in range(2):
                    self[a_lc[i]] = self.__class__.File(a_lc[i], list(SquareColor)[j - i % 2])
        self.__post_init__()

    def __post_init__(self):
        """Расставляет фигуры на игровой доске в начальную позицию."""
        self['a1'].piece = Piece(PieceColor.WHITE, PieceKind.ROOK, self['a1'])
        self['b1'].piece = Piece(PieceColor.WHITE, PieceKind.KNIGHT, self['b1'])
        self['c1'].piece = Piece(PieceColor.WHITE, PieceKind.BISHOP, self['c1'])
        self['d1'].piece = Piece(PieceColor.WHITE, PieceKind.QUEEN, self['d1'])
        self['e1'].piece = Piece(PieceColor.WHITE, PieceKind.KING, self['e1'])
        self['f1'].piece = Piece(PieceColor.WHITE, PieceKind.BISHOP, self['f1'])
        self['g1'].piece = Piece(PieceColor.WHITE, PieceKind.KNIGHT, self['g1'])
        self['h1'].piece = Piece(PieceColor.WHITE, PieceKind.ROOK, self['h1'])
        for rank in a_lc[:8]:
            self[rank][2].piece = Piece(PieceColor.WHITE, PieceKind.PAWN, self[rank][2])
        self['a8'].piece = Piece(PieceColor.BLACK, PieceKind.ROOK, self['a8'])
        self['b8'].piece = Piece(PieceColor.BLACK, PieceKind.KNIGHT, self['b8'])
        self['c8'].piece = Piece(PieceColor.BLACK, PieceKind.BISHOP, self['c8'])
        self['d8'].piece = Piece(PieceColor.BLACK, PieceKind.QUEEN, self['d8'])
        self['e8'].piece = Piece(PieceColor.BLACK, PieceKind.KING, self['e8'])
        self['f8'].piece = Piece(PieceColor.BLACK, PieceKind.BISHOP, self['f8'])
        self['g8'].piece = Piece(PieceColor.BLACK, PieceKind.KNIGHT, self['g8'])
        self['h8'].piece = Piece(PieceColor.BLACK, PieceKind.ROOK, self['h8'])
        for rank in a_lc[:8]:
            self[rank][7].piece = Piece(PieceColor.BLACK, PieceKind.PAWN, self[rank][7])

    def __rank(self, number) -> list[Square]:
        """Возвращает горизонталь игровой доски."""
        return [file[number] for file in self.values()]

    def __getitem__(self, key: str | int):
        """Обеспечивает вариативный доступ к полям игровой доски."""
        if re.match(r'^[a-h][1-8]$', key := str(key).lower()):
            return super().__getitem__(key[0])[int(key[1])]
        elif re.match(r'^[a-h]$', key):
            return super().__getitem__(key)
        elif re.match(r'^[1-8]$', key):
            return self.__rank(int(key))
        else:
            raise KeyError


class Turn:
    """Класс хранитель хода(номер хода, фигура, начальное поле, конечное поле"""
    def __init__(self, piece: Optional[Piece], end: Optional[Square], id=None):
        self.id = id
        self.piece = piece
        if piece:
            self.start = piece.square
            self.end = end
        else:
            self.start = None
            self.end = None

    def __str__(self):
        return f"{self.id}: {self.piece}{self.start}{self.end}"


class Game:
    """Класс игра, способный управлять экземпляром доски, делать ходы, отменять ходы повторять ходы"""
    def __init__(self):
        self.board = Chessboard()
        self._current_state = 0
        self._changes = [Turn(None, None)]

    def move(self, start: Square, end: Square):
        """Осуществляет ход"""
        state = Turn(start.piece, end)
        state.id = self._current_state + 1
        self._changes += [state]
        start.piece.move(end)
        self._current_state += 1

    @property
    def game_log(self):
        """Возвращает историю ходов"""
        return "\n".join(map(str, self._changes[1:]))

    def undo(self):
        """
        Откатывает игру на 1 ход
        """
        if self._current_state > 0:
            self.board[str(self._changes[self._current_state].start)].piece = self._changes[
                self._current_state].end.piece
            self.board[str(self._changes[self._current_state].end)].piece = None
            self._current_state -= 1
            state = self._changes[self._current_state]
            return state
        return None

    def redo(self):
        """Повторяет отмененный ход"""
        if self._current_state < len(self._changes) - 1:
            self._current_state += 1
            state = self._changes[self._current_state]
            # возвращаем фигуру
            self.board[str(state.end)].piece = self._changes[self._current_state].piece
            # обнуляем прошлое поле
            self.board[str(state.start)].piece = None
            self.square = state.end
            return state
        return None

    def to_step(self, step: int):
        """переносит игру к нужному ходу"""
        if step in [turn.id for turn in self._changes]:
            if self._current_state < step:
                while step != self._current_state:
                    self.redo()
                print(f"Игра перемещена в начало {step} хода")
            elif self._current_state > step:
                while step != self._current_state+1:
                    self.undo()
                print(f"Игра перемещена в начало {step} хода")
            else:
                self.undo()
                print(f"Игра перемещена в начало {step} хода")
        else:
            print("Выход за рамки ходов")


game = Game()
b = game.board

# print(game.board["e2"].piece)
print("Изначальное положение фигур:")
print(b)
print("-"*1000)
game.move(b["e2"], b["e4"])
game.move(b["e7"], b["e5"])
game.move(b["d1"], b["h5"])
game.move(b["g8"], b["c6"])
game.move(b["h5"], b["f7"])
print("\n'Экскурсия ферзя':")
print(b)
print("-"*1000)
game.undo()
print("\nОтмена хода:")
print(b)
game.redo()
print("\nПовтор хода:")
print(b)
print("\nПереход на начало 2 хода:")
game.to_step(2)
print(b)

print("\nЗапись шахматной партии:")
print(game.game_log)


"""
stdout
Изначальное положение фигур:
{'a': {1: <a1: White Rook>, 2: <a2: White Pawn>, 3: <a3: None>, 4: <a4: None>, 5: <a5: None>, 6: <a6: None>, 7: <a7: Black Pawn>, 8: <a8: Black Rook>}, 'b': {1: <b1: White Knight>, 2: <b2: White Pawn>, 3: <b3: None>, 4: <b4: None>, 5: <b5: None>, 6: <b6: None>, 7: <b7: Black Pawn>, 8: <b8: Black Knight>}, 'c': {1: <c1: White Bishop>, 2: <c2: White Pawn>, 3: <c3: None>, 4: <c4: None>, 5: <c5: None>, 6: <c6: None>, 7: <c7: Black Pawn>, 8: <c8: Black Bishop>}, 'd': {1: <d1: White Queen>, 2: <d2: White Pawn>, 3: <d3: None>, 4: <d4: None>, 5: <d5: None>, 6: <d6: None>, 7: <d7: Black Pawn>, 8: <d8: Black Queen>}, 'e': {1: <e1: White King>, 2: <e2: White Pawn>, 3: <e3: None>, 4: <e4: None>, 5: <e5: None>, 6: <e6: None>, 7: <e7: Black Pawn>, 8: <e8: Black King>}, 'f': {1: <f1: White Bishop>, 2: <f2: White Pawn>, 3: <f3: None>, 4: <f4: None>, 5: <f5: None>, 6: <f6: None>, 7: <f7: Black Pawn>, 8: <f8: Black Bishop>}, 'g': {1: <g1: White Knight>, 2: <g2: White Pawn>, 3: <g3: None>, 4: <g4: None>, 5: <g5: None>, 6: <g6: None>, 7: <g7: Black Pawn>, 8: <g8: Black Knight>}, 'h': {1: <h1: White Rook>, 2: <h2: White Pawn>, 3: <h3: None>, 4: <h4: None>, 5: <h5: None>, 6: <h6: None>, 7: <h7: Black Pawn>, 8: <h8: Black Rook>}}
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

'Экскурсия ферзя':
{'a': {1: <a1: White Rook>, 2: <a2: White Pawn>, 3: <a3: None>, 4: <a4: None>, 5: <a5: None>, 6: <a6: None>, 7: <a7: Black Pawn>, 8: <a8: Black Rook>}, 'b': {1: <b1: White Knight>, 2: <b2: White Pawn>, 3: <b3: None>, 4: <b4: None>, 5: <b5: None>, 6: <b6: None>, 7: <b7: Black Pawn>, 8: <b8: Black Knight>}, 'c': {1: <c1: White Bishop>, 2: <c2: White Pawn>, 3: <c3: None>, 4: <c4: None>, 5: <c5: None>, 6: <c6: Black Knight>, 7: <c7: Black Pawn>, 8: <c8: Black Bishop>}, 'd': {1: <d1: None>, 2: <d2: White Pawn>, 3: <d3: None>, 4: <d4: None>, 5: <d5: None>, 6: <d6: None>, 7: <d7: Black Pawn>, 8: <d8: Black Queen>}, 'e': {1: <e1: White King>, 2: <e2: None>, 3: <e3: None>, 4: <e4: White Pawn>, 5: <e5: Black Pawn>, 6: <e6: None>, 7: <e7: None>, 8: <e8: Black King>}, 'f': {1: <f1: White Bishop>, 2: <f2: White Pawn>, 3: <f3: None>, 4: <f4: None>, 5: <f5: None>, 6: <f6: None>, 7: <f7: White Queen>, 8: <f8: Black Bishop>}, 'g': {1: <g1: White Knight>, 2: <g2: White Pawn>, 3: <g3: None>, 4: <g4: None>, 5: <g5: None>, 6: <g6: None>, 7: <g7: Black Pawn>, 8: <g8: None>}, 'h': {1: <h1: White Rook>, 2: <h2: White Pawn>, 3: <h3: None>, 4: <h4: None>, 5: <h5: None>, 6: <h6: None>, 7: <h7: Black Pawn>, 8: <h8: Black Rook>}}
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Отмена хода:
{'a': {1: <a1: White Rook>, 2: <a2: White Pawn>, 3: <a3: None>, 4: <a4: None>, 5: <a5: None>, 6: <a6: None>, 7: <a7: Black Pawn>, 8: <a8: Black Rook>}, 'b': {1: <b1: White Knight>, 2: <b2: White Pawn>, 3: <b3: None>, 4: <b4: None>, 5: <b5: None>, 6: <b6: None>, 7: <b7: Black Pawn>, 8: <b8: Black Knight>}, 'c': {1: <c1: White Bishop>, 2: <c2: White Pawn>, 3: <c3: None>, 4: <c4: None>, 5: <c5: None>, 6: <c6: Black Knight>, 7: <c7: Black Pawn>, 8: <c8: Black Bishop>}, 'd': {1: <d1: None>, 2: <d2: White Pawn>, 3: <d3: None>, 4: <d4: None>, 5: <d5: None>, 6: <d6: None>, 7: <d7: Black Pawn>, 8: <d8: Black Queen>}, 'e': {1: <e1: White King>, 2: <e2: None>, 3: <e3: None>, 4: <e4: White Pawn>, 5: <e5: Black Pawn>, 6: <e6: None>, 7: <e7: None>, 8: <e8: Black King>}, 'f': {1: <f1: White Bishop>, 2: <f2: White Pawn>, 3: <f3: None>, 4: <f4: None>, 5: <f5: None>, 6: <f6: None>, 7: <f7: None>, 8: <f8: Black Bishop>}, 'g': {1: <g1: White Knight>, 2: <g2: White Pawn>, 3: <g3: None>, 4: <g4: None>, 5: <g5: None>, 6: <g6: None>, 7: <g7: Black Pawn>, 8: <g8: None>}, 'h': {1: <h1: White Rook>, 2: <h2: White Pawn>, 3: <h3: None>, 4: <h4: None>, 5: <h5: White Queen>, 6: <h6: None>, 7: <h7: Black Pawn>, 8: <h8: Black Rook>}}

Повтор хода:
{'a': {1: <a1: White Rook>, 2: <a2: White Pawn>, 3: <a3: None>, 4: <a4: None>, 5: <a5: None>, 6: <a6: None>, 7: <a7: Black Pawn>, 8: <a8: Black Rook>}, 'b': {1: <b1: White Knight>, 2: <b2: White Pawn>, 3: <b3: None>, 4: <b4: None>, 5: <b5: None>, 6: <b6: None>, 7: <b7: Black Pawn>, 8: <b8: Black Knight>}, 'c': {1: <c1: White Bishop>, 2: <c2: White Pawn>, 3: <c3: None>, 4: <c4: None>, 5: <c5: None>, 6: <c6: Black Knight>, 7: <c7: Black Pawn>, 8: <c8: Black Bishop>}, 'd': {1: <d1: None>, 2: <d2: White Pawn>, 3: <d3: None>, 4: <d4: None>, 5: <d5: None>, 6: <d6: None>, 7: <d7: Black Pawn>, 8: <d8: Black Queen>}, 'e': {1: <e1: White King>, 2: <e2: None>, 3: <e3: None>, 4: <e4: White Pawn>, 5: <e5: Black Pawn>, 6: <e6: None>, 7: <e7: None>, 8: <e8: Black King>}, 'f': {1: <f1: White Bishop>, 2: <f2: White Pawn>, 3: <f3: None>, 4: <f4: None>, 5: <f5: None>, 6: <f6: None>, 7: <f7: White Queen>, 8: <f8: Black Bishop>}, 'g': {1: <g1: White Knight>, 2: <g2: White Pawn>, 3: <g3: None>, 4: <g4: None>, 5: <g5: None>, 6: <g6: None>, 7: <g7: Black Pawn>, 8: <g8: None>}, 'h': {1: <h1: White Rook>, 2: <h2: White Pawn>, 3: <h3: None>, 4: <h4: None>, 5: <h5: None>, 6: <h6: None>, 7: <h7: Black Pawn>, 8: <h8: Black Rook>}}

Переход на начало 2 хода:
Игра перемещена в начало 2 хода
{'a': {1: <a1: White Rook>, 2: <a2: White Pawn>, 3: <a3: None>, 4: <a4: None>, 5: <a5: None>, 6: <a6: None>, 7: <a7: Black Pawn>, 8: <a8: Black Rook>}, 'b': {1: <b1: White Knight>, 2: <b2: White Pawn>, 3: <b3: None>, 4: <b4: None>, 5: <b5: None>, 6: <b6: None>, 7: <b7: Black Pawn>, 8: <b8: Black Knight>}, 'c': {1: <c1: White Bishop>, 2: <c2: White Pawn>, 3: <c3: None>, 4: <c4: None>, 5: <c5: None>, 6: <c6: None>, 7: <c7: Black Pawn>, 8: <c8: Black Bishop>}, 'd': {1: <d1: White Queen>, 2: <d2: White Pawn>, 3: <d3: None>, 4: <d4: None>, 5: <d5: None>, 6: <d6: None>, 7: <d7: Black Pawn>, 8: <d8: Black Queen>}, 'e': {1: <e1: White King>, 2: <e2: None>, 3: <e3: None>, 4: <e4: White Pawn>, 5: <e5: None>, 6: <e6: None>, 7: <e7: Black Pawn>, 8: <e8: Black King>}, 'f': {1: <f1: White Bishop>, 2: <f2: White Pawn>, 3: <f3: None>, 4: <f4: None>, 5: <f5: None>, 6: <f6: None>, 7: <f7: None>, 8: <f8: Black Bishop>}, 'g': {1: <g1: White Knight>, 2: <g2: White Pawn>, 3: <g3: None>, 4: <g4: None>, 5: <g5: None>, 6: <g6: None>, 7: <g7: Black Pawn>, 8: <g8: Black Knight>}, 'h': {1: <h1: White Rook>, 2: <h2: White Pawn>, 3: <h3: None>, 4: <h4: None>, 5: <h5: None>, 6: <h6: None>, 7: <h7: Black Pawn>, 8: <h8: Black Rook>}}

Запись шахматной партии:
1: WPe2e4
2: BPe7e5
3: WQd1h5
4: BKg8c6
5: WQh5f7

"""