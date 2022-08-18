
from database.db import get_connection
from .entities.CommentEntity import Comment


class CommentModel():

    @classmethod  # para podermos instanciar diretamente get_movies function
    # GET THE COMMENTS LIST
    def get_comments(self):
        try:
            connection = get_connection()
            commentsList = []  # initially creates and empty list

            # reads movies from database
            with connection.cursor() as cursor:  # Allows Python code to execute PostgreSQL command in a database session
                cursor.execute(
                    "SELECT id, username, text FROM users ORDER BY username ASC")
                resultset = cursor.fetchall()  # returns all data
            # gets the attributes for each movie
                for row in resultset:
                    comment = Comment(row[0], row[1], row[2])
                    commentsList.append(comment.to_JSON())

            connection.close()
            return commentsList
        except Exception as ex:
            raise Exception(ex)

    @classmethod  # para podermos instanciar diretamente get_movies function
    # GET AN INDIVIDUAL COMMENT
    def get_one_comment(self, id):
        try:
            connection = get_connection()

            # reads movies from database
            with connection.cursor() as cursor:  # Allows Python code to execute PostgreSQL command in a database session
                cursor.execute(
                    "SELECT id, username, text FROM users WHERE id = %s", (id,))
                row = cursor.fetchone()  # returns all data

                comment = None
                if row != None:
                    comment = Comment(row[0], row[1], row[2])
                    comment = comment.to_JSON()

            connection.close()
            return comment
        except Exception as ex:
            raise Exception(ex)

    @classmethod  # para podermos instanciar diretamente get_movies function
    # ADD COMMENTS
    def add_comment(self, newComment):
        try:
            connection = get_connection()

            # reads movies from database
            with connection.cursor() as cursor:  # Allows Python code to execute PostgreSQL command in a database session
                cursor.execute(
                    """INSERT INTO users (id, username, text) 
                    VALUES (%s, %s, %s)""", (newComment.id, newComment.username, newComment.text)
                )
                # contar quantas linhas sao afetadas no momento da insercao
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    @classmethod  # para podermos instanciar diretamente get_movies function
    # UPDATE COMMMENT
    def update_comment(self, modComment):
        try:
            connection = get_connection()

            # reads movies from database
            with connection.cursor() as cursor:  # Allows Python code to execute PostgreSQL command in a database session
                cursor.execute(
                    """UPDATE users SET text = %s
                    WHERE id = %s""", (modComment.text, modComment.id)
                )
                # contar quantas linhas sao afetadas no momento da insercao
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    @classmethod  # para podermos instanciar diretamente get_movies function
    # DELETE COMMENT
    def delete_comment(self, comment):
        try:
            connection = get_connection()

            # reads movies from database
            with connection.cursor() as cursor:  # Allows Python code to execute PostgreSQL command in a database session
                cursor.execute(
                    """DELETE FROM users WHERE id = %s""", (comment.id,)
                )
                # contar quantas linhas sao afetadas no momento da insercao
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
