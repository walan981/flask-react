
from database.db import get_connection
from .entities.MovieEntity import Movie


class MovieModel():

    @classmethod  # para podermos instanciar diretamente get_movies function
    # GET THE MOVIES LIST
    def get_movies(self):
        try:
            connection = get_connection()
            movies = []  # initially creates and empty list

            # reads movies from database
            with connection.cursor() as cursor:  # Allows Python code to execute PostgreSQL command in a database session
                cursor.execute(
                    "SELECT id, title, duration, released FROM movie ORDER BY title ASC")
                resultset = cursor.fetchall()  # returns all data
            # gets the attributes for each movie
                for row in resultset:
                    movie = Movie(row[0], row[1], row[2], row[3])
                    movies.append(movie.to_JSON())

            connection.close()
            return movies
        except Exception as ex:
            raise Exception(ex)

    @classmethod  # para podermos instanciar diretamente get_movies function
    # GET AN INDIVIDUAL MOVIE
    def get_one_movie(self, id):
        try:
            connection = get_connection()

            # reads movies from database
            with connection.cursor() as cursor:  # Allows Python code to execute PostgreSQL command in a database session
                cursor.execute(
                    "SELECT id, title, duration, released FROM movie WHERE id = %s", (id,))
                row = cursor.fetchone()  # returns all data

                movie = None
                if row != None:
                    movie = Movie(row[0], row[1], row[2], row[3])
                    movie = movie.to_JSON()

            connection.close()
            return movie
        except Exception as ex:
            raise Exception(ex)

    @classmethod  # para podermos instanciar diretamente get_movies function
    # GET AN INDIVIDUAL MOVIE
    def add_movie(self, movie):
        try:
            connection = get_connection()

            # reads movies from database
            with connection.cursor() as cursor:  # Allows Python code to execute PostgreSQL command in a database session
                cursor.execute(
                    """INSERT INTO movie (id, title, duration, released) 
                    VALUES (%s, %s, %s, %s)""", (movie.id, movie.title, movie.duration, movie.released)
                )
                # contar quantas linhas sao afetadas no momento da insercao
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    @classmethod  # para podermos instanciar diretamente get_movies function
    # UPDATE MOVIE
    def update_movie(self, movie):
        try:
            connection = get_connection()

            # reads movies from database
            with connection.cursor() as cursor:  # Allows Python code to execute PostgreSQL command in a database session
                cursor.execute(
                    """UPDATE movie SET title = %s, duration = %s, released = %s
                    WHERE id = %s""", (movie.title, movie.duration, movie.released, movie.id)
                )
                # contar quantas linhas sao afetadas no momento da insercao
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    @classmethod  # para podermos instanciar diretamente get_movies function
    # DELETE MOVIE
    def delete_movie(self, movie):
        try:
            connection = get_connection()

            # reads movies from database
            with connection.cursor() as cursor:  # Allows Python code to execute PostgreSQL command in a database session
                cursor.execute(
                    """DELETE FROM movie WHERE id = %s""", (movie.id,)
                )
                # contar quantas linhas sao afetadas no momento da insercao
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
