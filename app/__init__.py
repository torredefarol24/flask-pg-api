from flask import Flask
from app.config.app_config import AppConfig

flaskPgApp = Flask(__name__)
flaskPgApp.config.from_object(AppConfig)

from app import routes

if __name__ == '__main__':
  flaskPgApp.run(debug=True)