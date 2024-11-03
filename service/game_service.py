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

    def delete_game(self, game_id):
        return self.repository.delete_game(game_id)

    def update_game(self, game_id, name=None, photo=None, price=None, genre=None, launch_date=None, platform=None):

        genre_str = json.dumps(genre) if genre else None
        plat_str = json.dumps(platform) if platform else None

        return self.repository.update_game(game_id, name, photo, price, genre_str, launch_date, plat_str)