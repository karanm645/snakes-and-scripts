class Movie:
    def __init__(self, title, year, imdb_score, have_seen):
      self.title = title
      self.year = year
      self.imdb_score = imdb_score
      self.have_seen = have_seen
      # self refers to object we are creating - convention is to use self
      
    def nice_print(self):
      print("Title: ", self.title)
      print("Year: ", self.year)
      print("IMDB Score: ", self.imdb_score)
      print("Have I seen it?: ", self.have_seen)
      

film_1 = Movie("The Godfather", 1982, 8.5, True)
film_2 = Movie("Sarkar", 1999, 8.5, False)

# now print using the method of that class
film_2.nice_print() # this doesn't take argument because it is implicit on film_2
# equivalent to Movie.nice_print(film_2)

# we can make a list
films = [film_1, film_2]
print(films[1].title, films[1].imdb_score)

films[0].nice_print()





# class is custom made data types - abstract concept - blue print (movie)
# objects - make something outta the blue print (movie name)
# variables - attributes
# functions - methods