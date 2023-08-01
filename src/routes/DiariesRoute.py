from flask import Blueprint, jsonify, request

diaries = Blueprint('diaries', __name__)

@diaries.route('/', methods=["GET"])
def get_diaries():
    return jsonify({"diaries":[]})

@diaries.route('/<string:diary_id>', methods=["GET"])
def get_specific_diary(diary_id):
    return jsonify({"diary_id": diary_id})

@diaries.route('/', methods=["POST"])
def create_diary():
    from src.models.DiaryModel import Diary
    
    request_body = request.form
    title, notes = request_body.get('title'), request_body.get('notes')
    return jsonify({"new_diary_id": Diary.create_diary_entry(1, title, notes)})

@diaries.route('/<string:diary_id>', methods=["PUT"])
def update_diary(diary_id):
    return jsonify({"diary_id": diary_id})

@diaries.route('/<string:diary_id>', methods=["DELETE"])
def delete_diary(diary_id):
    return jsonify({"diary_id": diary_id})