from typing import Optional
from numbers import Real


# ДОБАВИТЬ: строки документации для классов и методов!
# ДОБАВИТЬ: аннотации типов параметров!

class Actor:
    def __init__(self, fullname, age, *films):
        self.fullname = fullname
        self.age = age
        # ИСПРАВИТЬ: если вы хотите, чтобы фильмы не повторялись, то лучше использовать множество или словарь — последний может также пригодиться, если вы хотите сохранить ещё и роль актёра в фильме
        self.films: set['FilmCard'] = set(films)

    # def add_films(self, film: 'FilmCard'):
    #     self.films.add(film)

    def __str__(self):
        return f"Имя: {self.fullname}: возраст{self.age}: фильмы: {', '.join(x.name for x in self.films)}"

    @property
    def name(self):
        return self.fullname


class FilmCard:
    # ИСПОЛЬЗОВАТЬ: для чисел в широком понимании есть generic тип Real, а для логического сложения любого типа с None есть специальный тип Optional
    def __init__(self, id_, name, genre, year, rating: Optional[Real] = None, *actors):
        self.id = id_
        # ИСПРАВИТЬ: если вы хотите инкапсулировать поля name и genre, то в начале их имён необходимо добавить один _ или два __ символа подчёркивания — так в Python мы обозначаем частный (private) и защищённый (protected) атрибуты
        self._name = name
        # ДОБАВИТЬ: для жанров стоило бы сделать отдельный класс перечислитель (Enum)
        self._genre = genre
        self._year = year
        self._rating = rating
        self._actors: set['Actor'] = set(actors)

    # ИСПРАВИТЬ: это метод настройки уже существующего экземпляра, следовательно должен находиться в фабрике
    # ИСПРАВИТЬ: передавая сюда только одного актёра за вызов, вы вынуждаете вызывать этот метод снова и снова — приближаясь к пошаговому подходу строителя

    # ИСПРАВИТЬ: если вы хотите инкапсулировать поля name и genre, то в Python мы для этого используем свойства — декоратор @property

    @property
    def name(self):
        return self._name

    @property
    def genre(self):
        return self._genre

    def __str__(self):
        return f"Карточка фильма:\n" \
               f"\tID: {self.id}\n" \
               f"\tНазвание: {self._name}\n" \
               f"\tГод: {self._year}\n" \
               f"\tЖанр: {self._genre}\n" \
               f"\tРейтинг: {self._rating}\n" \
               f"\tАктеры: {', '.join(x.name for x in self._actors)}\n"
        # ИСПОЛЬЗОВАТЬ: дополнительные переносы строк — прерогатива кода верхнего уровня


# КОММЕНТАРИЙ: раз уж вы добавили сюда класс Actor, то можно было бы организовать совместное одновременное "производство" на фабрике фильмов и актёров
class FilmFactory:
    def __init__(self):
        # КОММЕНТАРИЙ: вот это хорошо
        self.id = 0

    # ИСПОЛЬЗОВАТЬ: для чисел в широком понимании есть generic тип Real, а для логического сложения любого типа с None есть специальный тип Optional
    def create_film(self, name, genre, year, rating: Optional[Real] = None, *actors):
        self.id += 1
        return FilmCard(self.id, name, genre, year, rating, *actors)

    def create_actor(self, name, age, films: Optional[list] = None):
        return Actor(name, age, films)


class FilmSorter:
    @staticmethod
    def fantastic(*films):
        cards = '\n'.join([
            str(x)
            for x in films
            if x.genre == 'Фантастика'
        ])
        return f"Фантастика:\n{'-' * 50}\n{cards}{'-' * 50}"

    @staticmethod
    def action_movie(*films):
        cards = '\n'.join([
            str(x)
            for x in films
            if x.genre == 'Боевик'
        ])
        return f"Боевики:\n{'-' * 50}\n{cards}{'-' * 50}"


actor1 = Actor("Alex Nevsky", 1971)
actor2 = Actor("Adrian Poul", 1959)
actor3 = Actor("Matthias Hues", 1959)
actor4 = Actor("Mark Daсasсos", 1964)

ff = FilmFactory()
# КОММЕНТАРИЙ: слишком похоже на строитель, не находите?) разница во многом заключается в пошаговом или разовом подходе к созданию объекта
# потому что фильмы не штампуют, фильмы создают =)
black_rose = ff.create_film("Черная Роза", "Боевик", 2014, 1.5, actor1, actor2, actor3)
star_track_6 = ff.create_film("Звездный Путь", "Фантастика", 1991, 7.2, actor3)
highlander = ff.create_film("Горец", "Фантастика", 1992, None, actor2)

print(black_rose)
print(star_track_6)
fs = FilmSorter()
fantas = fs.fantastic(black_rose, highlander, star_track_6)
print(fantas, end='\n' * 3)

action = fs.action_movie(black_rose, highlander, star_track_6)
print(action, end='\n' * 3)

# stdout:
"""
Фантастика:
--------------------------------------------------
Карточка фильма:
	ID:3
	Название: Горец
	Год: 1992
	жанр: Фантастика
	рейтинг: None
	актеры: Adrian Poul

Карточка фильма:
	ID:2
	Название: Звездный Путь
	Год: 1991
	жанр: Фантастика
	рейтинг: 7.2
	актеры: Matthias Hues

--------------------------------------------------
Боевики:
--------------------------------------------------
Карточка фильма:
	ID:1
	Название: Черная Роза
	Год: 2014
	жанр: Боевик
	рейтинг: 1.5
	актеры: Alex Nevsky,Adrian Poul,Matthias Hues

--------------------------------------------------

"""

# ИТОГ: довольно хорошо, документации, жаль, не хватает — 5/7
