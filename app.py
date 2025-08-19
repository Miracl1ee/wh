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

