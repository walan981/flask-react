from distutils.debug import DEBUG
from decouple import config
# Decouple helps you to organize your settings so that you can change parameters without having to redeploy your app.


class Config:
    SECRET_KEY = config('SECRET_KEY')  # reading from file .env


class DevelopmentConfig(Config):
    DEBUG = True  # server automatically restarts from each change


config = {  # creates a dictionary
    'development': DevelopmentConfig
}
