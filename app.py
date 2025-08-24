<<<<<<< HEAD
from flask import Flask, jsonify, request
from database import Database
from databaseUsers import databaseUsers
from file_format import FileFormat
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from pydantic_file import register_important, add_homework_important
from pydantic import ValidationError
from databaseUsers import User

app = Flask(__name__)
db_homework = Database()
db_users = databaseUsers()
file = FileFormat()
auth = HTTPBasicAuth()

@auth.verify_password
def verify_password(username, password):
    user_data = db_users.search_user_by_username(username)
    if not user_data:
        return False
    user = User(user_data[0], user_data[1], user_data[2])
    if user.check_password(password):
        return user
    return False

@auth.error_handler
def unauthorized():
    return jsonify({"error": "Требуется аутентификация"}), 401

def check_user(username):
    current_user = auth.current_user()
    if current_user is None:
        return False
    if current_user.username == username:
        return True
    else:
        return False

@app.route('/register', methods=['POST'])
def register():
    try:
        register_important.model_validate(request.json)
    except ValidationError as e:
        return jsonify({"error": "Нужен username и password для регистрации"}), 400
    data = request.get_json()
    username = data['username']
    password = data['password']
    search_user = db_users.search_user_by_username(username) #ищет пользователя в базе
    if search_user:
        return jsonify({"error": "Пользователь уже существует"}), 409
    password_hash = generate_password_hash(password)
    registration = db_users.register_user(username, password_hash)
    if registration:
        return jsonify({"message": "Пользователь успешно зарегистрирован"}), 201
    return jsonify({"error": "Ошибка регистрации"}), 500

@app.route('/login', methods=['POST'])
def login():
    try:
        register_important.model_validate(request.json)
    except ValidationError as e:
        return jsonify({"error": "Нужен username и password для входа"}), 400
    data = request.get_json()
    username = data['username']
    password = data['password']
    user_data = db_users.search_user_by_username(username)
    if not user_data:
        return jsonify({"error": "Пользователь не найден"}), 401
    user = User(user_data[0], user_data[1], user_data[2])
    if user.check_password(password):
        return jsonify({
            "message": "Успешный вход", 
            "user_id": user.id, 
            "username": user.username
        }), 200
    else:
        return jsonify({"error": "Неверные учетные данные"}), 401

@app.route('/work', methods=['POST'])
def add_house_work():
    try:
        add_homework_important.model_validate(request.json)
    except ValidationError as e:
        return jsonify({"error": "Нужен username и housework для добавления задания"}), 400
    data = request.get_json()
    db_homework.add_homework(data['username'], data['housework'])
    return jsonify({'message': 'Задание добавлено'}), 201

@app.route('/work/<username>', methods=['GET'])
@auth.login_required
def search_by_username(username):
    if not check_user(username):
        return jsonify({"error": "Доступ запрещен. Можно просматривать только свои данные"}), 403
    
    tasks = db_homework.search_all(username)
    result = []
    for task in tasks:
        result.append({
            'id': task[0],
            'user_name': task[1],
            'house_work': task[2]
        })
    return jsonify(result), 200

@app.route('/work/<username>/<query_housework>/search_by_housework', methods=['GET'])
@auth.login_required
def search_with_username_and_housework(username, query_housework):
    if not check_user(username):
        return jsonify({"error": "Доступ запрещен. Можно просматривать только свои данные"}), 403
    tasks = db_homework.search_with_user_and_text(username, query_housework)
    result = []
    for task in tasks:
        result.append({
            'id': task[0],
            'user_name': task[1],
            'house_work': task[2]
        })
    return jsonify(result), 200


@app.route('/work/<username>/delete_all', methods=['POST'])
@auth.login_required
def delete_all_by_username(username):
    if not check_user(username):
        return jsonify({"error": "Доступ запрещен. Можно просматривать только свои данные"}), 403
    db_homework.delete_all(username)
    return jsonify({'message': 'Задания успешно удалены'}), 200


@app.route('/work/write_to_csv', methods=['POST'])
def write_to_csv_ok():
    data = request.get_json()  # читает данные
    if not data or 'lines' not in data:
        return jsonify({'error': 'Требуется lines для добавления в базу'}), 400
    lines = data['lines']
    file.write_to_csv(lines)
    return jsonify({'message': 'Задание добавлено'}), 201


@app.route('/work/write_to_xlsx', methods=['POST'])
def write_to_xlsx():
    data = request.get_json()
    if 'lines' not in data or not data:
        return jsonify({'error': 'Требуется lines для добавления в базу'}), 400
    lines = data['lines']
    file.write_to_xlsx(lines)
    return jsonify({'message': 'Задание добавлено'}), 201


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
=======
from flask import Flask, jsonify, request
from database import Database
from file_format import FileFormat
app = Flask(__name__)
db = Database()
file = FileFormat()


@app.route('/work', methods=['POST'])
def add_house_work():
    data = request.get_json()  # читает данные
    if 'user_name' not in data or 'house_work' not in data or not data:
        return jsonify(
            {'error': 'Требуется user_name и house_work для добавления в базу'}), 400
    db.add_homework(data['user_name'], data['house_work'])
    return jsonify({'message': 'Задание добавлено'}), 201


@app.route('/work/<user_name>', methods=['GET'])
def search_by_username(user_name):
    tasks = db.search_all(user_name)
    result = []
    for task in tasks:
        result.append({
            'id': task[0],
            'user_name': task[1],
            'house_work': task[2]
        })
    return jsonify(result), 200


@app.route('/work/<user_name>/<query_housework>/search_by_housework',
           methods=['GET'])
def search_with_username_and_housework(user_name, query_housework):
    tasks = db.search_with_user_and_text(user_name, query_housework)
    result = []
    for task in tasks:
        result.append({
            'id': task[0],
            'user_name': task[1],
            'house_work': task[2]
        })
    return jsonify(result), 200


@app.route('/work/<user_name>/delete_all', methods=['POST'])
def delete_all_by_username(user_name):
    db.delete_all(user_name)
    return jsonify({'message': 'Задания успешно удалены'}), 201


@app.route('/work/write_to_csv', methods=['POST'])
def write_to_csv_ok():
    data = request.get_json()  # читает данные
    if not data or 'lines' not in data:
        return jsonify({'error': 'Требуется lines для добавления в базу'}), 400
    lines = data['lines']
    file.write_to_csv(lines)
    return jsonify({'message': 'Задание добавлено'}), 201


@app.route('/work/write_to_xlsx', methods=['POST'])
def write_to_xlsx():
    data = request.get_json()
    if 'lines' not in data or not data:
        return jsonify({'error': 'Требуется lines для добавления в базу'}), 400
    lines = data['lines']
    file.write_to_xlsx(lines)
    return jsonify({'message': 'Задание добавлено'}), 201


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)

>>>>>>> a9f594b995eb050cb5db63099ae58e515d2999b4
