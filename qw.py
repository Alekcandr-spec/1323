def movies(genre):
    recommendations = {
        "драма": "'Зеленая книга', 'Сияние', 'Побег из Шоушенка', 'Форрест Гамп', 'Семь жизней'",
        "комедия": "'Суперперцы', 'Назад в будущее', 'День сурка', 'Шпионские игры', 'Друзья на всю жизнь'",
        "боевик": "'Матрица', 'Джон Уик', 'Темный рыцарь', 'Миссия невыполнима', 'Крепкий орешек'",
        "ужасы": "'Сияние', 'Проклятие', 'Заклятие', 'Оно', 'Хэллоуин'",
        "фантастика": "'Интерстеллар', 'Начало', 'Звёздные войны', 'Бегущий по лезвию', 'Аватар'"}
    if genre in recommendations:
        return recommendations[genre]
    else:
        return "Неизвестный жанр."
def books(genre):
    recommendations = {
        "фантастика": "'1984' Джорджа Оруэлла, 'Фаренгейт 451' Рэя Брэдбери, 'Дюна' Фрэнка Герберта",
        "роман": "'Гордость и предубеждение' Джейн Остин, 'Мастер и Маргарита' Михаила Булгакова",
        "приключения": "'Остров сокровищ' Роберта Льюиса Стивенсона, 'Три мушкетера' Александра Дюма",
        "триллер": "'Исчезнувшая' Гиллиан Флинн, 'Девушка с татуировкой дракона' Стига Ларссона",
        "поэзия": "произведения Александра Блока, Анны Ахматовой, Сергея Есенина"}
    if genre in recommendations:
        return recommendations[genre]
    else:
        return "Неизвестный жанр."
