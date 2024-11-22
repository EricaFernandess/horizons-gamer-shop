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

    def delete_game(self, game_id):
        cursor = self.conn.cursor()
        cursor.execute('DELETE FROM games WHERE id = ?', (game_id,))
        self.conn.commit()

        return cursor.rowcount > 0  # Retorna True se uma linha foi deletada, caso contrário False

    def update_game(self, game_id, name=None, photo=None, price=None, genre=None, launch_date=None, platform=None):
        cursor = self.conn.cursor()

        # Cria uma query dinâmica para atualizar apenas os campos fornecidos
        fields = []
        values = []

        if name is not None:
            fields.append("name = ?")
            values.append(name)
        if photo is not None:
            fields.append("photo = ?")
            values.append(photo)
        if price is not None:
            fields.append("price = ?")
            values.append(price)
        if genre is not None:
            fields.append("genre = ?")
            values.append(json.dumps(genre))  # Converte lista para JSON string
        if launch_date is not None:
            fields.append("launch_date = ?")
            values.append(launch_date)
        if platform is not None:
            fields.append("platform = ?")
            values.append(json.dumps(platform))  # Converte lista para JSON string

        if not fields:
            return False  # Nenhum campo para atualizar

        # Monta a query de atualização com os campos dinâmicos
        query = f"UPDATE games SET {', '.join(fields)} WHERE id = ?"
        values.append(game_id)

        cursor.execute(query, values)
        self.conn.commit()

        return cursor.rowcount > 0

    def get_game_by_name(self, name):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM games WHERE name LIKE ?", (f"%{name}%",))
        games = cursor.fetchall()

        result = []
        for game in games:
            game_dict = dict(game)
            game_dict['genre'] = json.loads(game_dict['genre'])
            game_dict['platform'] = json.loads(game_dict['platform'])
            result.append(game_dict)

        return result

    def close_connection(self):
        self.conn.close()
