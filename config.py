import os

class Config:

    #Location of the database with authentication   
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://neal:Wneal9.@localhost/pitch'

    #SECRET_KEY=os.environ.get('SECRET_KEY')
    SECRET_KEY = 'S9WnSR256m52VgJTzgAv5AqfQXewgQ'
    
    UPLOADED_PHOTOS_DEST ='app/static/photos'

    #Email configs
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    SUBJECT_PREFIX = 'Pitch It Up!'
    SENDER_EMAIL = 'neal.waga@student.moringaschool.com'

    @staticmethod
    def init_app(app):
        pass


class ProdConfig(Config):
    '''
    Production configuration child class
    Args:
        Config: The parent configuration class with general configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    #pass


class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://neal:Wneal9.@localhost/pitch'

class DevConfig(Config):
    '''
    Development configuration child class
    Args;
        Config: The parent configuration class with general configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://neal:Wneal9.@localhost/pitch'

    DEBUG = True

config_options = {
    'development':DevConfig,
    'production':ProdConfig,
    'test':TestConfig
}