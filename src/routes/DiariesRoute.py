from flask import Blueprint, jsonify, request, make_response
from src.auth.AuthDecorators import token_required

diaries = Blueprint('diaries', __name__)

@diaries.route('/', methods=["GET"])
@token_required
def get_all_diaries(user_id):
    from src.models.DiaryModel import Diary

    try:
        diary_id_list = []
        all_diaries = Diary.get_diaries_entries(user_id)
        for diary in all_diaries:
            diary_id_list.append({"id": diary.id, "date": diary.date})

        return make_response(jsonify({"diaries": diary_id_list}), 200)
    except Exception:
        return make_response(jsonify({"error": "Bad Request"}), 400)

@diaries.route('/<string:diary_id>', methods=["GET"])
@token_required
def get_specific_diary(user_id,diary_id):
    from src.models.DiaryModel import Diary

    try:
        return make_response(jsonify({"diary_info": Diary.read_diary_entry(diary_id)}), 200)
    except Exception:
        return make_response(jsonify({"error": "Check the request body"}), 400)

@diaries.route('/', methods=["POST"])
@token_required
def create_diary(user_id):
    from src.models.DiaryModel import Diary
    
    try:
        request_body = request.json
        title, notes = request_body["title"], request_body["notes"]
        return make_response(jsonify({"new_diary_id": Diary.create_diary_entry(user_id, title, notes)}), 200)
    except Exception:
        return make_response(jsonify({"error": "Check the request body"}), 400)

@diaries.route('/<string:diary_id>', methods=["PUT"])
@token_required
def update_diary(user_id,diary_id):
    from src.models.DiaryModel import Diary

    try:
        request_body = request.json
        notes = request_body["notes"]
        return make_response(jsonify({"old_diary_notes": Diary.update_diary_entry(diary_id, notes)}), 200)
    except Exception:
        return make_response(jsonify({"error": "Check the request body"}), 400)

@diaries.route('/<string:diary_id>', methods=["DELETE"])
@token_required
def delete_diary(user_id,diary_id):
    from src.models.DiaryModel import Diary

    try:
        return make_response(jsonify({"old_diary_id": Diary.delete_diary_entry(diary_id)}), 200)
    except Exception:
        return make_response(jsonify({"error": "Check the request body"}), 400)