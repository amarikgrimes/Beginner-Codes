for number in range(10):
  print(number)

fav_movies = ["coraline", "crazy rich asians","prizoner of azkaban"]
print("\n")
print(fav_movies[2])
print("\n")
print(len(fav_movies))
print("\n")
fav_movies.append("nightmare before christmas")

print(len(fav_movies))
print("\n")
print(fav_movies)

fav_movies.insert(1,"missing")
print("\n")
print(fav_movies)

del(fav_movies[0])
del(fav_movies[0])
del(fav_movies[0])
del(fav_movies[0])
print("\n")
print(fav_movies)

for movies in fav_movies:
  print(movies)

for number in range(40):
  print((number +1) * 2)
