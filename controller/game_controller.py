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

@game_controller.route('/update-game', methods=['GET'])
def update_game_form():
    return render_template('update_game.html')

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

@game_controller.route('/update-game/<int:game_id>', methods=['PUT'])
def update_game(game_id):
    data = request.get_json()

    name = data.get('name')
    photo = data.get('photo')
    price = data.get('price')
    genre = data.get('genre')
    launch_date = data.get('launch_date')
    platform = data.get('platform')

    success = game_service.update_game(
        game_id=game_id,
        name=name,
        photo=photo,
        price=price,
        genre=genre,
        launch_date=launch_date,
        platform=platform
    )

    if success:
        return jsonify({"message": "Jogo atualizado com sucesso!"}), 200
    else:
        return jsonify({"message": "Jogo não encontrado ou nenhum campo para atualizar!"}), 404

    @game_controller.route('/search-games', methods=['GET'])
    def search_games():
        game_name = request.args.get('name', '').lower()
        if not game_name:
            return jsonify([])

        filtered_games = [game for game in games if game_name in game['name'].lower()]
        return jsonify(filtered_games)