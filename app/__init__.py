from flask import Flask
from app.config.app_config import AppConfig
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_restful import Api

app = Flask(__name__)
app.config.from_object(AppConfig)

db = SQLAlchemy(app)
migrate = Migrate(app, db)
bcrypt = Bcrypt(app)
api = Api(app)

from app import routes, models
# from app import resources

if __name__ == '__main__':
  app.run()