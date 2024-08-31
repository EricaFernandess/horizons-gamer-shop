from flask import Flask
from controller.game_controller import game_controller

app: Flask = Flask(__name__)

app.register_blueprint(game_controller)

if __name__ == '__main__':
    app.run(debug=True)