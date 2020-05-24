import os

base_dir = os.path.abspath(os.path.dirname(__file__))

class Config:
    """
    This is the base configuration class
    """
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        pass

class DevConfig(Config):
    """
    Development Configuration class
    """
    DEBUG=True
    SQLALCHEMY_DATABASE_URI = None # Later I will add a database uri perferably MySQL

class TestConfig(Config):
    TESTING = True
    DEBUG = True

config = {
    "default":DevConfig,
    "testing":TestConfig
}
