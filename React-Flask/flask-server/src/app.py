from flask import Flask
from flask_cors import CORS

from config import config


# Routes (need __init__.py)
from routes import Movie


app = Flask(__name__)
# como rodar servidor partindo de outras URL`s
CORS(app, resources={"*": {"origins": "http://localhost:3000"}})


def page_not_found(error):  # defining custom error response
    return "<h1>Page not Found :((((((</h1>", 404


if __name__ == '__main__':
    # Development configs
    app.config.from_object(config['development'])

    # Blueprints
    # url address to enter the movie route:
    app.register_blueprint(Movie.main, url_prefix='/api/movies')

    # Error Handler
    app.register_error_handler(404, page_not_found)
    app.run()
