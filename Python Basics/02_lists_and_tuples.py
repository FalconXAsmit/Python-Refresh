# Lists :- Lists are changeable, meaning you can add, remove, or change items after the list has been created.
favourite_games = ["Persona 5 Royal", "Palworld", "Valorant", "The Witcher 3", "Hades"]
first_game = favourite_games[0]  # Accessing the first item in the list which is "Persona 5 Royal"
print("First Game:", first_game, " ", type(first_game))

last_game = favourite_games[-1]  # Accessing the last item in the list which is "Hades"
print("Last Game:", last_game, " ", type(last_game))

middle_games = favourite_games[1:4]  # Accessing a slice of the list from index 1 to 3
print("Middle Games:", middle_games, " ", type(middle_games))

# Adding a new game to the list
favourite_games.append("Cyberpunk 2077")  # Adds "Cyberpunk 2077" to the end of the list
print("Updated Favourite Games:", favourite_games, " ", type(favourite_games))

# Removing a game from the list
favourite_games.remove("Valorant")  # Removes "Valorant" from the list
print("After Removing Valorant:", favourite_games, " ", type(favourite_games))

# Popping the last game from the list
favourite_games.pop()  # Removes the last item from the list
print("After Popping Last Game:", favourite_games, " ", type(favourite_games))

favourite_games.sort()  # Sorts the list in alphabetical order
print("Sorted Favourite Games:", favourite_games, " ", type(favourite_games))

# Tuples :- Tuples are immutable, meaning once they are created, their items cannot be changed.
favourite_movies = ("Inception", "The Matrix", "Interstellar", "The Dark Knight", "Pulp Fiction")
first_movie = favourite_movies[0]  # Accessing the first item in the tuple which is "Inception"
print("First Movie:", first_movie, " ", type(first_movie))

last_movie = favourite_movies[-1]  # Accessing the last item in the tuple which is "Pulp Fiction"
print("Last Movie:", last_movie, " ", type(last_movie))

# BUT, you cannot change them. This next line will cause an error if you uncomment it.
# primary_colors[0] = "Crimson" # This would raise a TypeError