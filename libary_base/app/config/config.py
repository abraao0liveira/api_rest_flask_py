import os

class Config:
  SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'mysql+pymysql://abraao0liveira:SkyP1ll%40r_384@localhost:3306/libary')
  SQLALCHEMY_TRACK_MODIFICATIONS = False
  SECRET_KEY = os.getenv('SECRET_KEY', 'mysecretkey')
