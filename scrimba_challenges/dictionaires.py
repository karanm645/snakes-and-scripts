movie = {
  'title' : 'Jumanji',
  'year' : 1979,
  'cast' : ['John', 'The Rock', 'Kevin Hart', 'Terrence']
}
# movie['title'] = "jumanji 21" # this is how you change values
# movie['budget'] = 239029302 # this adds key value pair
# print(movie.get("title")) # .get --> if there is error, it will say none

# # this is how you update
# movie.update({'title' : 'Bad Santa', 'year' : 1991, 'cast' : ["kevin", 'john', 'lyle'], 'budget' : 208932083203982032})
# delete
# del movie['year']
#pop
# year = movie.pop('year')
print(movie)
# print(year)
# length
print(len(movie))
#print keys, values etc
print(movie.keys())
# tuple results
print(movie.items())

#you can use a for loop to print key and values
for key, value in movie.items():
  print(key, value)