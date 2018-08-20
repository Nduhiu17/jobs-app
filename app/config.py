import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = True
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'this-is-secret'


class ProductionConfig(Config):
    DEBUG = True


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    try:
        SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    except:
        pass
    DEVELOPMENT = True
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'jobs_test.sqlite')


config_environments = {
    'production': ProductionConfig,
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}
