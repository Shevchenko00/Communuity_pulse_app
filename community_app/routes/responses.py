from flask import Blueprint, make_response, jsonify, request

from community_app import db
from community_app.models.questions import Statistics, Questions

response_bp = Blueprint('responses', __name__, url_prefix= '/responses')



@response_bp.route('/', methods=['GET'])
def get_responses():
    """Получение агрегированной статистики ответов."""
    statistics = Statistics.query.all()
    results = [
        {
            "question_id": stat.question_id,
            "agree_count": stat.agree_count,
            "disagree_count": stat.disagree_count
        }
        for stat in statistics
    ]

    response = make_response(jsonify(results), 200)
    return response



@response_bp.route('/')
def get_all_responses():
    return "ALL RESPONSES"


@response_bp.route('/add', methods=['POST'])
def add_response():
    """Добавление нового ответа на вопрос с обновлением статистики."""
    data = request.get_json()
    if not data or 'question_id' not in data or 'is_agree' not in data:
        return jsonify({'message': "Некорректные данные"}), 400

    if not isinstance(data['is_agree'], bool):
        return jsonify({'message': "Некорректное значение is_agree"}), 400

    question = Questions.query.get(data['question_id'])
    if not question:
        return jsonify({'message': "Вопрос не найден"}), 404

    from community_app.models.response import Responses
    response = Responses(
        question_id=question.id,
        is_agree=data['is_agree']
    )
    db.session.add(response)
    db.session.commit()  # Сохранение ответа перед обновлением статистики

    # Обновление статистики
    statistic = Statistics.query.filter_by(question_id=question.id).first()
    if not statistic:
        statistic = Statistics(question_id=question.id, agree_count=0, disagree_count=0)
        db.session.add(statistic)
    if data['is_agree']:
        statistic.agree_count += 1
    else:
        statistic.disagree_count += 1

    db.session.commit()

    return jsonify({'message': f"Ответ на вопрос {question.id} добавлен"}), 201
