movies = [
    "And Now for Something Completely Different",
    "Monty Python and the Holy Grail",
    "Monty Python's Life of Brian",
    "Monty Python Live at the Hollywood Bowl",
    "Monty Python's The Meaning of Life",
    "Monty Python Live (Mostly)",
]
year = [1971, 1975, 1979, 1982, 1983, 2014]
names = ["John", "Eric", "Michael", "Graham", "Terry", "TerryG"]

# create list that creates movies and year
print(list(zip(movies, year)))

# give me a dict('movies': year) for each movies, year in zip(movies, year)
#for loop
new_dict = {}
for movie, yr in zip(movies, year):
  new_dict[movie] = yr 
print(new_dict)

new_dict = {movie: yr for movie, yr in zip(movies, year)}
print(new_dict)

# we only want movies before 1983 and has only python in it
new_dict = {movie: yr for movie, yr in zip(movies, year) if yr < 1983 and movie.startswith("Monty")}
print(new_dict)

#movies that each person liked
n1 = [[name + "s favorite movie was: " + movie + " from " + str(yr)] for name, movie, yr in zip(names, movies, year) if yr < 1981]
print(n1)