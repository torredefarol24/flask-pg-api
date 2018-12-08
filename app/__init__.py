from flask import Flask
from app.config.app_config import AppConfig
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt

flaskPgJwtApp = Flask(__name__)
flaskPgJwtApp.config.from_object(AppConfig)

db = SQLAlchemy(flaskPgJwtApp)
migrate = Migrate(flaskPgJwtApp, db)
bcrypt = Bcrypt(flaskPgJwtApp)


from app import routes, models

if __name__ == '__main__':
  flaskPgJwtApp.run()