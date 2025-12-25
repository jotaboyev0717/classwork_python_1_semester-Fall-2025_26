movies = {
    "Inception": ["Sci-Fi", "Action"],
    "The Matrix": ["Sci-Fi", "Action"],
    "Shrek": ["Animation", "Comedy"],
    "Toy Story": ["Animation", "Family"],
    "Interstellar": ["Sci-Fi", "Drama"]
}

genre_index = {}
for title, genre_list in movies.items():
    for i in genre_list:
        if i not in genre_index:
            genre_index[i] = []
        genre_index[i].append(title)
print(genre_index)