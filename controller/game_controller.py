from flask import Blueprint, request, jsonify, render_template
from service.game_service import GameService

game_controller = Blueprint('game_controller', __name__)
game_service = GameService()

@game_controller.route('/')
def index():
    return render_template('index.html')

@game_controller.route('/add-game')
def add_game():
    return render_template('add_game.html')

@game_controller.route('/register-game', methods=['POST'])
def register_game():
    data = request.get_json()

    game_service.register_game(
        name=data['name'],
        photo=data['photo'],
        price=data['price'],
        genre=data['genre'],
        launch_date=data['launch_date'],
        platform=data['platform']
    )

    response = {
        'message': 'Dados recebidos e salvos com sucesso!',
        'received_data': data
    }

    return jsonify(response), 201

@game_controller.route('/games', methods=['GET'])
def get_games():
    games = game_service.fetch_all_games()
    return jsonify(games), 200


@game_controller.route('/delete-game/<int:game_id>', methods=['DELETE'])
def delete_game(game_id):
    result = game_service.delete_game(game_id)

    if result:
        return jsonify({'message': f'Jogo com ID {game_id} deletado com sucesso!'}), 200
    else:
        return jsonify({'error': f'Jogo com ID {game_id} não encontrado.'}), 404