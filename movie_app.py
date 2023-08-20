class MovieApp:
    def __init__(self, storage):
        self._storage = storage

    def _command_list_movies(self):
        movies = self._storage.list_movies()
        # Implement the logic for listing movies

    def _command_movie_stats(self):
        movies = self._storage.list_movies()
        # Implement the logic for calculating statistics

    def _generate_website(self):
        movies = self._storage.list_movies()
        # Implement the logic for generating a website

    def run(self):
        while True:
            # Print menu
            # get user command
            #execute command
