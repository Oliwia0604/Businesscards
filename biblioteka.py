import random
import datetime

print("Biblioteka filmow")

class Movie:
    def __init__(self, title, year, type_of, number_of_plays):
        self.title=title
        self.year=year
        self.type_of=type_of
        self.number_of_plays=number_of_plays

    def play(self):
        self.number_of_play += 1
        return self.number_of_plays

    def __str__(self):
        return f"{self.title} ({self.year})"

class Serie(Movie):
    def __init__(self, title, year, type_of, number_of_plays, episode_number, season_number):
        super().__init__(title, year, type_of, number_of_plays)
        self.episode_number=episode_number
        self.season_number=season_number
    
    def __str__(self):
        return f"{self.title} S{self.season_number:02}E{self.episode_number:02}"

def get_movies(data):
    return filter(lambda el: type(el) == Movie, data)

def get_series(data):
    return filter(lambda el: type(el)== Serie, data)

def display(data):
    for item in data:
        print(item, item.number_of_plays)

def search(data, title):
    for item in data:
        if item.title == title:
            return item
    return None 

def run_generate_views(n, data):
    for _ in range(n):
        generate_views(data)

def generate_views(data):
    item = random.choice(data)
    number_of_plays = random.randint(1,100)
    item.number_of_plays = number_of_plays

def top_titles(data, quantity):
    return sorted(data, key=lambda item: item.number_of_plays, reverse=True)[:quantity]


if __name__ == "__main__":
    print("Biblioteka filmów")
    print("-" * 10)

    the_irishman = Movie("The Irishman", 2019, "dramat", 5000)
    pierwszy_czlowiek = Movie("Pierwszy czlowiek",2018, "dramat", 300)
    shawshank = Movie("Shawshank", 1994, "dramat", 2000)
    forrest_gump = Movie("Forrest Gump", 1994, "dramat", 1500)
    django = Movie("Django", 2013, "western", 1000)
    stranger_things = Serie("Stranger Things", 2019, "horror", 2, 4, 123)
    dom_z_papieru = Serie("Dom z papieru", 2020, "kryminal", 4, 3, 52)
    narcos = Serie("Narcos", 2017, "kryminal", 2, 3, 85)
    unorthodox = Serie("Unorthodox", 2020, "dramat", 1, 4, 32)
    breaking_bad = Serie("Breaking Bad", 2013, "kryminal", 1, 4, 48)

    movies_and_series = [the_irishman, pierwszy_czlowiek, shawshank, forrest_gump, django, stranger_things, dom_z_papieru, narcos, unorthodox, breaking_bad]

    for item in movies_and_series:
        print(item.__str__())
        print(item.play())

    print("-" * 10 + "get movies")
    movies = get_movies(movies_and_series)
    display(movies)

    print("-" * 10 + "get series")

    series = get_series(movies_and_series)
    display(series)

    print("-" * 10 + "search")


    title = "The Irishman"
    print(search(movies_and_series, title))

    print("-" * 10 + " generate views 10 times")
    run_generate_views(10, movies_and_series)
    display(movies_and_series)

    print("-" * 10 + " top titles")
    print(f"Najpopularniejsze filmy i seriale dnia {datetime.date.today().strftime('%d.%m.%Y')}")
    data = top_titles(movies_and_series, 3)
    display(data)





