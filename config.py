
#it has the SQLALCHEMY_DATABASE_URI attribute set to the database URL, which we define for the connection to the database.
# we can define other configuration according to the server requirement
import os

class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # @staticmethod
    # def init_app(app):
    #     pass

class DevelopmentConfig(Config):
    DEBUG = True
    # Set your static database URL here
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:abhi2903@localhost:3306/flaskdatabase?charset=utf8mb4'



config = {
    "development": DevelopmentConfig,
    "default": DevelopmentConfig
}