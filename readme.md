## Flask API (PG)

- API : Flask 
- Authentication - JWT
- Python - v3.7
- Database - PostgreSQL
- ORM - SQLAlchemy


## Run App Locally

- Setup DB Info
```sh
$ cd flask-pg-api
$ touch app/config/db_info.py

# Update db_info.py

PGDB_LOCALHOST_URI = <YOUR_PGDB_URI>
PGDB_DOCKER_URI = ""
```

- Update **app/config/app_config.py**
```sh
# Change Line 6
SQLALCHEMY_DATABASE_URI = PGDB_DOCKER_URI

#to
SQLALCHEMY_DATABASE_URI = PGDB_LOCALHOST_URI

#Remember, the URI Format is
# <DB_TYPE>://<DB_USERNAME>:<DB_PASSWORD>@<DB_HOST>:<DB_PORT>/<DB_NAME>
```

- Create your Virtual Environment
```sh
$ cd flask-pg-api
$ python3 -m venv <YOUR_ENV_NAME>

# Start your virtual environment
$ source <YOUR_ENV_NAME>/bin/activate
```

- Install Package Dependencies
```sh
$ cd flask-pg-api

# After starting the virtual environment
$ pip install requirements.txt
```

- Start App
```sh
$ cd flask-pg-api
$ export FLASK_APP=flask_pg_jwt.py
$ flask run
```
