import json
import sqlite3

class GameRepository:
    def __init__(self, db_path='games.db'):
        self.db_path = db_path
        self.conn = sqlite3.connect(self.db_path, check_same_thread=False)
        self.conn.row_factory = sqlite3.Row
        self.create_table()

    def create_table(self):
        # Verifica se a tabela existe antes de tentar criar
        cursor = self.conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='games'")
        if not cursor.fetchone():
            self.conn.execute('''CREATE TABLE games (
                                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    name TEXT NOT NULL,
                                    photo TEXT,
                                    price REAL,
                                    genre TEXT NOT NULL,
                                    launch_date TEXT,
                                    platform TEXT
                                )''')
            self.conn.commit()

    def insert_game(self, name, photo, price, genre, launch_date, platform):
        self.conn.execute('INSERT INTO games (name, photo, price, genre, launch_date, platform) VALUES (?, ?, ?, ?, ?, ?)',
                          (name, photo, price, genre, launch_date, platform))
        self.conn.commit()

    def get_all_games(self):
        cursor = self.conn.execute("SELECT * FROM games")
        games = cursor.fetchall()

        # Converte as strings JSON de volta para listas
        result = []
        for game in games:
            game_dict = dict(game)
            game_dict['genre'] = json.loads(game_dict['genre'])
            game_dict['platform'] = json.loads(game_dict['platform'])
            result.append(game_dict)

        return result

    def close_connection(self):
        self.conn.close()
