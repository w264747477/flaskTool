import os

import redis
class Config(object):

    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    # redis
    # REDIS_HOST='127.0.0.1'
    # REDIS_POST=6379
    # flask-session配置
    SESSION_TYPE='redis'
    # SESSION_REDIS=redis.StrictRedis(host=REDIS_HOST,port=REDIS_POST)
    SQLQLCHEMY_TRACK_MODIFICATIONS = True
    SESSION_USE_SIGNER=True
    PERMANENT_SESSION_LIFETIME=86400   #session数据有效时间
    WTF_CSRF_CHECK_DEFAULT=False
class DevelopmentConfig(Config):
    # 开发模式配置信息
    DEBUG = True
    # 数据库
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URI') or \
                              'mysql+pymysql://root:123456@127.0.0.1/authbase?charset=utf8'

    pass
class ProductConfig(Config):
    # 生产环境
    # 数据库
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URI') or \
                              'mysql+pymysql://root:wang7777qq@43.142.9.84/authbase?charset=utf8'
    SQLQLCHEMY_TRACK_MODIFICATIONS = True
    pass
config_map={
    "develop":DevelopmentConfig,
    "product":ProductConfig
}