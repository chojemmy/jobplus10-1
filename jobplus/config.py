class BaseConfig(object):
    '''配置基类'''
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRT_KEY = 'chenanming'
    INDEX_PER_PAGE = 9
    ADMIN_PER_PAGE = 15

class DevelopmentConfig(BaseConfig):
    '''开发环境'''
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqldb://root@localhost:3306/jobplus?charset=utf8'

class ProductionConfig(BaseConfig):
    '''生产环境'''
    pass

class TestingConfig(app):
    pass

configs = {
        'development': DevelopmentConfig,
        'production': ProductionConfig,
        'testing': TestingConfig
        }

