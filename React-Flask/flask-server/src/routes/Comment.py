
from random import randint
from flask import Blueprint, request, jsonify
import uuid  # cria ids unicos para cada nova entrada no db


# Models
from models.CommentModel import CommentModel
# Entities
from models.entities.CommentEntity import Comment

main = Blueprint('comment_blueprint', __name__)

# LISTAR COMENTARIOS


@main.route('/')
def get_comments():
    try:
        comments = CommentModel.get_comments()
        return jsonify(comments)
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500  # Error 500

# BUSCA POR COMENTARIO


@main.route('/<id>')
def get_one_comment(id):
    try:
        comment = CommentModel.get_one_comment(id)
        if comment != None:
            return jsonify(comment)
        else:
            return jsonify({}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500  # Error 500

# ADICIONAR COMENTARIO


@main.route('/add', methods=['POST'])
def add_comment():
    try:
        username = request.json['username']
        # duration = int(request.json['duration'])
        commentText = request.json['text']
        # id = uuid.uuid1()
        id = randint(0, 99999)
        print(id)

        comment = Comment(id, username, commentText)
        affected_rows = CommentModel.add_comment(comment)

        if affected_rows == 1:
            return jsonify(comment.id)
        else:
            return jsonify({'message': 'Error on insert'}), 500

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500  # Error 500


# ATUALIZAR FILME


@main.route('/update/<id>', methods=['PUT'])
def update_comment(id):
    try:
        # username = request.json['username']
        # duration = int(request.json['duration'])
        commentText = request.json['text']

        comment = Comment(id, None, commentText)
        affected_rows = CommentModel.update_comment(comment)

        if affected_rows == 1:
            return jsonify(comment.id)
        else:
            return jsonify({'message': 'No movie updated'}), 404

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500  # Error 500


@main.route('/delete/<id>', methods=['DELETE'])
def delete_comment(id):
    try:
        comment = Comment(id)

        affected_rows = CommentModel.delete_comment(comment)

        if affected_rows >= 1:
            return jsonify(comment.id)
        else:
            return jsonify({'message': 'No movie deleted'}), 404

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500  # Error 500
