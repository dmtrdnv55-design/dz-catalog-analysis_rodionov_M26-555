import math

movies = [
    {
        "title": "The Dune Chronicles",
        "year": 2021,
        "genres": {"sci-fi", "drama"},
        "rating": 8.6,
        "duration_min": 155,
        "actors": ["T. Chalamet", "R. Ferguson", "O. Isaac"],
    },
    {
        "title": "Kitchen Stories",
        "year": 2019,
        "genres": {"comedy", "drama"},
        "rating": 7.1,
        "duration_min": 98,
        "actors": ["A. Novak", "M. Ferguson"],
    },
    {
        "title": "silent hours",
        "year": 2016,
        "genres": {"thriller", "drama"},
        "rating": 6.4,
        "duration_min": 112,
        "actors": ["J. Bloom", "K. Lee"],
    },
    {
        "title": "Comet Racers",
        "year": 2023,
        "genres": {"sci-fi", "action"},
        "rating": 5.9,
        "duration_min": 101,
        "actors": ["O. Isaac", "P. Diaz"],
    },
    {
        "title": "The Last Bakery",
        "year": 2014,
        "genres": {"comedy"},
        "rating": 7.8,
        "duration_min": 89,
        "actors": ["A. Novak", "T. Chalamet"],
    },
    {
        "title": "midnight in oslo",
        "year": 2020,
        "genres": {"thriller", "mystery"},
        "rating": 8.9,
        "duration_min": 124,
        "actors": ["K. Lee", "R. Ferguson"],
    },
    {
        "title": "Garden of Static",
        "year": 2022,
        "genres": {"drama"},
        "rating": 4.8,
        "duration_min": 137,
        "actors": ["P. Diaz", "J. Bloom"],
    },
    {
        "title": "The Quiet Algorithm",
        "year": 2024,
        "genres": {"sci-fi", "drama"},
        "rating": 9.2,
        "duration_min": 118,
        "actors": ["M. Ferguson", "O. Isaac"],
    },
    {
        "title": "Two Left Shoes",
        "year": 2011,
        "genres": {"comedy"},
        "rating": 6.0,
        "duration_min": 95,
        "actors": ["A. Novak", "K. Lee"],
    },
    {
        "title": "Red Harbor",
        "year": 2018,
        "genres": {"action", "thriller"},
        "rating": 7.3,
        "duration_min": 129,
        "actors": ["P. Diaz", "T. Chalamet"],
    },
]


def average_rating(movies):
    movies_count = len(movies)
    sum_rating = 0
    for movie in movies:
        sum_rating += movie["rating"]
    mean_rating = sum_rating / movies_count
    return round(mean_rating, 1)


def catalog_age_stats(movies, current_year=2026):
    movies_count = len(movies)
    first_movie_age = current_year - movies[0]["year"]
    max_age = first_movie_age
    min_age = first_movie_age
    sum_age = first_movie_age
    for movie in movies[1:]:
        age = current_year - movie["year"]
        sum_age += age
        if age > max_age:
            max_age = age
        elif age < min_age:
            min_age = age
    mean_age = math.ceil(sum_age / movies_count)
    t = (max_age, min_age, mean_age)
    return t


def duration_in_hours(minutes):
    hours = minutes // 60
    minute = minutes % 60
    formatted = f"{hours}ч {minute}м"
    return formatted


def rating_tier(rating):
    if rating >= 9:
        rating_category = "шедевр"
    elif 7 <= rating < 9:
        rating_category = "хорошо"
    else:
        rating_category = "средне" if 5 <= rating < 7 else "слабо"
    return rating_category


def decade_label(year):
    match year:
        case _ if year > 2020:
            year_category = "новые"
        case _ if 2015 <= year <= 2020:
            year_category = "недавние"
        case _:
            year_category = "старые"
    return year_category


for movie in movies:
    if "comedy" in movie["genres"]:
        continue
    print(movie["title"])

index = 0
while index < len(movies):
    if movies[index]["rating"] > 9:
        found_film = movies[index]["title"]
        break
    index += 1
else:
    found_film = "Шедевров не найдено"


def count_long_movies(movies, threshold=120):
    long_movies = 0
    for movie in movies:
        if movie["duration_min"] > threshold:
            long_movies += 1
    return long_movies
