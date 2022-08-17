
from random import randint
from flask import Blueprint, request, jsonify
import uuid  # cria ids unicos para cada nova entrada no db


# Models
from models.MovieModel import MovieModel
# Entities
from models.entities.MovieEntity import Movie

main = Blueprint('movie_blueprint', __name__)

# LISTAR FILMES


@main.route('/')
def get_movies():
    try:
        movies = MovieModel.get_movies()
        return jsonify(movies)
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500  # Error 500

# BUSCA POR FILME


@main.route('/<id>')
def get_one_movie(id):
    try:
        movie = MovieModel.get_one_movie(id)
        if movie != None:
            return jsonify(movie)
        else:
            return jsonify({}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500  # Error 500

# ADICIONAR FILME


@main.route('/add', methods=['POST'])
def add_movie():
    try:
        title = request.json['title']
        duration = int(request.json['duration'])
        released = request.json['released']
        # id = uuid.uuid1()
        id = randint(0, 99999)
        print(id)

        movie = Movie(id, title, duration, released)
        affected_rows = MovieModel.add_movie(movie)

        if affected_rows == 1:
            return jsonify(movie.id)
        else:
            return jsonify({'message': 'Error on insert'}), 500

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500  # Error 500


# ATUALIZAR FILME


@main.route('/update/<id>', methods=['PUT'])
def update_movie(id):
    try:
        title = request.json['title']
        duration = int(request.json['duration'])
        released = request.json['released']

        movie = Movie(id, title, duration, released)
        affected_rows = MovieModel.update_movie(movie)

        if affected_rows == 1:
            return jsonify(movie.id)
        else:
            return jsonify({'message': 'No movie updated'}), 404

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500  # Error 500


@main.route('/delete/<id>', methods=['DELETE'])
def delete_movie(id):
    try:
        movie = Movie(id)

        affected_rows = MovieModel.delete_movie(movie)

        if affected_rows >= 1:
            return jsonify(movie.id)
        else:
            return jsonify({'message': 'No movie deleted'}), 404

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500  # Error 500
