class Actor:
    def __init__(self, fullname, age):
        self.fullname = fullname
        self.age = age
        self.films: list['FilmCard'] = []

    def add_films(self, film: 'FilmCard'):
        if film not in self.films:
            self.films += [film]

    def __str__(self):
        return f"Имя: {self.fullname}: возраст{self.age}: фильмы: {', '.join(x.get_name() for x in self.films)}"

    def get_name(self):
        return self.fullname


class FilmCard:
    def __init__(self, id_, name, genre, year, rating: float | None = None):
        self.id = id_
        self.name = name
        self.genre = genre
        self.year = year
        self.rating = rating
        self.actors: list['Actor'] = []

    def add_actors(self, actor: 'Actor'):
        self.actors += [actor]
        actor.add_films(self)
        return self

    def get_name(self):
        return self.name

    def get_genre(self):
        return self.genre

    def __str__(self):
        return f"Карточка фильма:\n\t" \
               f"ID:{self.id}\n\t" \
               f"Название: {self.name}\n" \
               f"\tГод: {self.year}\n\t" \
               f"жанр: {self.genre}\n\t" \
               f"рейтинг: {self.rating}\n\t" \
               f"актеры: {','.join(x.get_name() for x in self.actors)}\n\n"


class FilmFactory:
    def __init__(self):
        self.id = 0

    def create_film(self, name, genre, year, rating: float | None = None):
        self.id += 1
        return FilmCard(self.id, name, genre, year, rating)


class FilmSorter:
    @staticmethod
    def fantastic(*films):
        return f"Фантастика:\n{'-'*50}\n{''.join([str(x) for x in films if x.get_genre() == 'Фантастика'])}{'-'*50}"

    @staticmethod
    def action_movie(*films):
        return f"Боевики:\n{'-'*50}\n{''.join([str(x) for x in films if x.get_genre() == 'Боевик'])}{'-'*50}"


actor1 = Actor("Alex Nevsky", 1971)
actor2 = Actor("Adrian Poul", 1959)
actor3 = Actor("Matthias Hues", 1959)
actor4 = Actor("Mark Daсasсos", 1964)

ff = FilmFactory()
black_rose = ff.create_film("Черная Роза", "Боевик", 2014, 1.5).add_actors(actor1).add_actors(actor2).add_actors(actor3)
star_track_6 = ff.create_film("Звездный Путь", "Фантастика", 1991, 7.2).add_actors(actor3)
highlander = ff.create_film("Горец", "Фантастика", 1992).add_actors(actor2)

# print(black_rose)
# print(star_track_6)
fs = FilmSorter()
fantas = fs.fantastic(black_rose, highlander, star_track_6)
print(fantas)

action=fs.action_movie(black_rose, highlander, star_track_6)
print(action)
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