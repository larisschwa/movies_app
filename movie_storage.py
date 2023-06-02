import requests
import json


def list_movies():
    """
    returns a dictionary of dictionaries that contains the movies information
    in the database.
    the function loads the information from the json file and returns the data.
    """

    with open('data.json', 'r') as fileobj:
        movies = json.load(fileobj)

    print(len(movies), "movies in total")
    for title, data in movies.items():
        print(f"{title} ({data['year']}): {data['rating']}")

    return movies


def add_movie():
    """
    adds a movie to the movies database
    """
    # get the data from the json file
    with open('data.json', 'r') as fileobj:
        movies = json.load(fileobj)

    # get user input
    title = input("Enter new movie name: ")
    if title in movies:
        print(f"Movie {title} already exists.")
        return

    # search the movie in the OMDb API
    try:
        response = requests.get(
            f"http://www.omdbapi.com/?t={title}&apikey=5eeb20d")
        movie_data = response.json()

        # check if movie not found
        if movie_data.get("Response") == "False":
            print(f"Movie {title} not found.")
            return

        # extract required parameters
        year = movie_data.get("Year")
        rating = float(movie_data.get("imdbRating"))
        poster_url = movie_data.get("Poster")

        movies[title] = {"year": year, "rating": rating,
                         "poster_url": poster_url}

        # add the movie and save the data to the json file
        with open('data.json', 'w') as file:
            json.dump(movies, file)

        print(
            f"{title} ({year}) has been added to the list with a rating of "
            f"{rating}")
    except requests.exceptions.RequestException as e:
        print("An error occurred while accessing the API:", e)


def delete_movie():
    """
    Updates a movie from the movies database.
    Loads the information from the JSON file, updates the movie,
    and saves it. The function doesn't need to validate the input.
    """

    # load the json file
    with open('data.json', 'r') as fileobj:
        movies = json.load(fileobj)

    # get input from user and delete info
    title = input("Enter movie name to delete: ")
    if title in movies:
        del movies[title]
        print(f"Movie {title} successfully deleted.")
    else:
        print(f"Movie {title} doesn't exist!")

    # save the updated data to the json file
    with open('data.json', 'w') as file:
        json.dump(movies, file)


def update_movie():
    """
    Updates a movie from the movies database.
    Loads the information from the data.JSON file, updates the movie,
    and saves it. The function doesn't need to validate the input.
    """
    # get the data from the json file
    with open('data.json', 'r') as fileobj:
        movies = json.load(fileobj)

    title = input("Enter movie name: ")
    if title in movies:
        new_rating = float(input("Enter the new rating: "))
        movies[title]["rating"] = new_rating
    else:
        print(f"{title} doesn't exist!")

    # save the updated data to the json file
    with open('data.json', 'w') as file:
        json.dump(movies, file)
