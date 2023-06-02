from istorage import IStorage


class StorageJson(IStorage):
    def __init__(self, file_path):
        ...

    def list_movies(self):
        ...

    def add_movie(self, title, year, rating, poster):
        ...

    def delete_movie(self, title):
        ...

    def update_movie(self, title, notes):
        ...