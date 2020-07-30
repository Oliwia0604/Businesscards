print("Biblioteka filmow")

class Films:
    def __init__(self, film_title, film_released, film_genre, number_of_plays):
        self.film_title=film_title
        self.film_released=film_released
        self.film_genre=film_genre
        self.number_of_plays=number_of_plays

a=Films("The Irishman","2019", "dramat", "5000")
b=Films("Pierwszy czlowiek","2018", "dramat", "300")
c=Films("Shawshank", "1994", "dramat", "2000")
d=Films("Forrest Gump", "1994", "dramat", "1500")
e=Films("Django", "2013", "western", "1000")

Films=[a, b, c, d, e]


class series:
    def __init__(self, series_title, series_released, series_genre, episode_number, season_number, number_of_plays):
        self.series_title=series_title
        self.series_released=series_released
        self.series_genre=series_genre
        self.episode_number=episode_number
        self.season_number=season_number
        self.number_of_plays=number_of_plays

f=series("Stranger Things","2019", "Horror", "S02", "E04", "123")
g=series("Dom z papieru", "2020", "Kryminal", "S04", "E03", "52")
h=series("Narcos", "2017", "Kryminal", "S02", "E03", "85")
i=series("Unorthodox", "2020", "Dramat", "S01", "E04", "32")
j=series("Breaking Bad", "2013", "Kryminal", "S01", "E04", "48")

series=[f, g, h, i, j]

for films in films:
    print(f"{film_title} ({film_released})")

for series in series:
    print(f"{film_series} {episode_number}{season_number}"



#def play(self): 
  #  self.number_of_plays += 1

   