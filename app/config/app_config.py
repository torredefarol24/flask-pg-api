from app.config.db_info import PGDB_DOCKER_URI, PGDB_LOCALHOST_URI
from datetime import timedelta

class AppConfig(object):
  SQLALCHEMY_DATABASE_URI = PGDB_DOCKER_URI
  SQLALCHEMY_TRACK_MODIFICATIONS = False
  JWT_SECRET_KEY="wow"
  JWT_ACCESS_TOKEN_EXPIRES = timedelta(days=1)

