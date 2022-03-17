star_wars_movies = [
    ["The Phantom Menace", "Attack of the Clones", "Revenge of the Sith"],
    ["A New Hope", "The Empire Strikes Back", "Return of the Jedi"],
    ["The Force Awakens", "The Last Jedi", "The Rise of Skywalker"],
]

trilogy = int(input("Please enter the number of the Star Wars trilogy (1,2 or 3): "))
film = int(input("Please enter the number of a film in the trilogy (1,2 or 3): "))

print("You selected", star_wars_movies[trilogy - 1][film - 1])
