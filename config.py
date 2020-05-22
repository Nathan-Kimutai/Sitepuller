class Config:
    @staticmethod
    def init_app(app):
        pass

class DevConfig(Config):
    DEBUG=True

class TestConfig(Config):
    pass

config = {
    "default":DevConfig,
    "testing":TestConfig
}
