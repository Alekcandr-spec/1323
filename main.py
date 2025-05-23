from qw import movies, books
from we import music
print("Добро пожаловать в Советчик по Фильмам/Книгам/Музыке!")
category = input("Выберите категорию (фильмы/книги/музыка/стоп): ").lower()
while category != 'стоп':
    if category == "фильмы":
        genre = input("Жанр (драма/комедия/боевик/ужасы/фантастика): ").lower()
        print("Рекомендуем:", movies(genre))
    elif category == "книги":
        genre = input("Жанр (фантастика/роман/приключения/триллер/поэзия): ").lower()
        print("Рекомендуем:", books(genre))
    elif category == "музыка":
        genre = input("Жанр (рок/поп/джаз/классическая/электронная): ").lower()
        print("Рекомендуем:", music(genre))
    else:
        print("Неизвестная категория.")
    category = input("Выберите категорию (фильмы/книги/музыка/стоп): ").lower()
print("Спасибо! До свидания!")
