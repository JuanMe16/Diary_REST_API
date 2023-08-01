from decouple import config

class Config():
    SECRET_KEY = config('SECRET_KEY')

class DevelopmentConfig(Config):
    ENV = "development"
    DEBUG = True

class ProductionConfig(Config):
    ENV = "production"
    DEBUG = False

config = {
    'development' : DevelopmentConfig,
    'production': ProductionConfig
}