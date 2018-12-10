from app.config.db_info import PGDB_DOCKER_URI, PGDB_LOCALHOST_URI
from app.config.jwt_info import JWT_TOKEN_SECRET
from datetime import timedelta

class AppConfig(object):
  SQLALCHEMY_DATABASE_URI = PGDB_DOCKER_URI
  # SQLALCHEMY_DATABASE_URI = PGDB_LOCALHOST_URI
  SQLALCHEMY_TRACK_MODIFICATIONS = False
  JWT_SECRET_KEY = JWT_TOKEN_SECRET
  JWT_ACCESS_TOKEN_EXPIRES = timedelta(days=1)

