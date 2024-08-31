import json

from repository.game_repository import GameRepository

class GameService:
    def __init__(self):
        self.repository = GameRepository()

    def register_game(self, name, photo, price, genre, launch_date, platform):
        genre_str = json.dumps(genre)
        plat_str = json.dumps(platform)
        self.repository.insert_game(name, photo, price, genre_str, launch_date, plat_str)

    def fetch_all_games(self):
        games = self.repository.get_all_games()
        return games