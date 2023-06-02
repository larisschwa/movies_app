import random
import json
import movie_storage


def load_movie_data():
    """loads data from json file"""
    with open('data.json') as f:
        movies = json.load(f)
    return movies


def menu_options():
    """list menu options"""
    print("***Movies Database***")
    print("\n0. Exit")
    print("1. List movies")
    print("2. Add movie")
    print("3. Delete movie")
    print("4. Update movie")
    print("5. Stats")
    print("6. Random movie")
    print("7. Search movies")
    print("8. Movies sorted by rating")
    print("9. Generate website\n")


def movie_stats(movies):
    """show movie stats"""
    movies = load_movie_data()
    num_movies = len(movies)
    total_rating = sum(float(data["rating"]) for data in movies.values())
    avg_rating = total_rating / num_movies

    # median
    ratings = [float(movie['rating']) for movie in movies.values()]
    sorted_ratings = sorted(ratings)
    n = len(sorted_ratings)
    mid = n // 2
    if n % 2 == 0:
        median_rating = (sorted_ratings[mid - 1] + sorted_ratings[mid]) / 2
    else:
        median_rating = sorted_ratings[mid]

    # best and worst
    best_movie = None
    worst_movie = None
    for movie, data in movies.items():
        rating = float(data['rating'])
        if best_movie is None or rating > float(movies[best_movie]['rating']):
            best_movie = movie
        if worst_movie is None or rating < float(movies[worst_movie]['rating']):
            worst_movie = movie

    print(f"Average rating: {avg_rating:.2f}")
    print(f"Median rating: {median_rating:.1f}")
    print(f"Best movie: {best_movie} ({movies[best_movie]['rating']:.1f})")
    print(f"Worst movie: {worst_movie} ({movies[worst_movie]['rating']:.1f})")


def random_movie(movies):
    """generate random movie"""
    movies = load_movie_data()
    movie = random.choice(list(movies.keys()))
    rating = movies[movie]['rating']
    print(f"Your movie for tonight: {movie}, it's rated {rating}")


def movie_search(movies):
    """search database for movie by name"""
    movies = load_movie_data()
    query = input("Enter a part of a movie name: ").lower()
    matches = []
    for movie, data in movies.items():
        if query in movie.lower():
            matches.append((movie, data['rating']))
    if len(matches) == 0:
        print("No matches found.")
    else:
        for movie, rating in matches:
            print(f"{movie}: {rating}")


def sort_movies(movies):
    """sort movies by rating in descending order"""
    movies = load_movie_data()
    sorted_movies = sorted(movies.items(),
                           key=lambda x: float(x[1]['rating']), reverse=True)
    for movie, data in sorted_movies:
        print(f"{movie}: {data['rating']}")


def press_enter():
    """informs user to press enter to continue"""
    input("\nPress enter to continue")


def generate_website(template_title):
    """generates website based on html and css templates
    and compiled information"""
    template_content = """
    <html>
    <head>
        <title>{title}</title>
        <link rel="stylesheet" href="style.css"/>
    </head>
    <body>
    <div class="list-movies-title">
        <h1>{title}</h1>
    </div>
    <div>
        <ol class="movie-grid">
            {movie_grid}
        </ol>
    </div>
    </body>
    </html>
    """

    # Read movie data from the JSON file
    with open('data.json') as f:
        movies = json.load(f)

    # Generate the movie grid HTML content
    movie_grid = ""
    for title, data in movies.items():
        poster_url = data.get('poster_url', '')
        year = data.get('year', '')

        movie_html = """
        <li>
            <div class="movie">
                <img class="movie-poster" src="{poster_url}"/>
                <div class="movie-title">{title}</div>
                <div class="movie-year">{year}</div>
            </div>
        </li>
        """.format(poster_url=poster_url, title=title,
                   year=year)
        movie_grid += movie_html

    # Replace the placeholders with the provided values
    modified_content = template_content.format(title=template_title,
                                               movie_grid=movie_grid)

    output_file = "index.html"

    # Write the modified HTML content to the output file
    with open(output_file, "w") as f:
        f.write(modified_content)

    print("Website was generated successfully.")


def main():
    """load data from json file, list menu options
    implements functions based on user input"""
    movies = load_movie_data()
    while True:
        menu_options()
        choice = input("Enter your choice: " "\n")

        if choice == "1":
            movies = movie_storage.list_movies()
            press_enter()
        elif choice == "2":
            movies = movie_storage.add_movie()
            press_enter()
        elif choice == "3":
            movies = movie_storage.delete_movie()
            press_enter()
        elif choice == "4":
            movie_storage.update_movie()
            press_enter()
        elif choice == "5":
            movie_stats(movies)
            press_enter()
        elif choice == "6":
            random_movie(movies)
            press_enter()
        elif choice == "7":
            movie_search(movies)
            press_enter()
        elif choice == "8":
            sort_movies(movies)
            press_enter()
        elif choice == "9":
            generate_website("My Movie App")
        elif choice == "0":
            print("Bye!")
            break

        print("\n")


if __name__ == "__main__":
    main()
