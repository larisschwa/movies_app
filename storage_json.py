from istorage import IStorage
import json


class StorageJson(IStorage):
    def __init__(self, file_path):
        self.file_path = file_path

    def list_movies(self):
        with open(self.file_path, 'r') as fileobj:
            movies = json.load(fileobj)
        return movies

    def add_movie(self, title, year, rating, poster):
        with open(self.file_path, 'r') as fileobj:
            movies = json.load(fileobj)

        if title in movies:
            print(f"Movie {title} already exists.")
            return

        movies[title] = {"year": year, "rating": rating, "poster": poster}

        with open(self.file_path, 'w') as fileobj:
            json.dump(movies, fileobj)

        print(f"{title} ({year}) has been added to the list with a rating of "
              f"{rating}")

    def delete_movie(self, title):
        with open(self.file_path, 'r') as fileobj:
            movies = json.load(fileobj)

        if title in movies:
            del movies[title]
            print(f"Movie {title} successfully deleted.")
        else:
            print(f"Movie {title} doesn't exist!")

        with open(self.file_path, 'w') as fileobj:
            json.dump(movies, fileobj)

    def update_movie(self, title, rating):
        with open(self.file_path, 'r') as fileobj:
            movies = json.load(fileobj)

        if title in movies:
            movies[title]["rating"] = rating
            print(f"Rating of {title} updated to {rating}")
        else:
            print(f"Movie {title} doesn't exist!")

        with open(self.file_path, 'w') as fileobj:
            json.dump(movies, fileobj)
