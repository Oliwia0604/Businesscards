print("Biblioteka filmow")

class Movies:
    def __init__(self, movie_title, movie_released, movie_genre, movie_number_of_plays):
        self.movie_title=movie_title
        self.movie_released=movie_released
        self.movie_genre=movie_genre
        self.movie_number_of_plays=movie_number_of_plays

a=Movies("The Irishman","2019", "dramat", "5000")
b=Movies("Pierwszy czlowiek","2018", "dramat", "300")
c=Movies("Shawshank", "1994", "dramat", "2000")
d=Movies("Forrest Gump", "1994", "dramat", "1500")
e=Movies("Django", "2013", "western", "1000")

Movies=[a, b, c, d, e]




class series:
    def __init__(self, series_title, series_released, series_genre, episode_number, season_number, series_number_of_plays):
        self.series_title=series_title
        self.series_released=series_released
        self.series_genre=series_genre
        self.episode_number=episode_number
        self.season_number=season_number
        self.series_number_of_plays=series_number_of_plays

f=series("Stranger Things","2019", "Horror", "S02", "E04", "123")
g=series("Dom z papieru", "2020", "Kryminal", "S04", "E03", "52")
h=series("Narcos", "2017", "Kryminal", "S02", "E03", "85")
i=series("Unorthodox", "2020", "Dramat", "S01", "E04", "32")
j=series("Breaking Bad", "2013", "Kryminal", "S01", "E04", "48")

series=[f, g, h, i, j]

for movie in movies:
        print(f"{movie_title} ({movie_released})")
    

for series in series:
        print(f"{film_series} {episode_number}{season_number}"



#def play(movies, series): 
 #   self.number_of_plays += 1
    

