## Flask API (PG)

- API : Flask 
- Authentication - JWT
- Python - v3.6
- Database - PostgreSQL 10.6
- ORM - SQLAlchemy

## Run Docker Container

- Pull App Image
```sh
$ cd flask-pg-api
$ docker pull burningraven06/flask-pg-jwt:d7
```

- Start Postgres Image
```sh
$ docker pull postgres:10.6
$ docker run --name <POSTGRES_INSTANCE> -e POSTGRES_PASSWORD=test1212 -p 5432:5432 -d postgres:10.6 
```

- Start App Image
```sh
$ docker run --name <APP_INSTANCE_NAME> --link <POSTGRES_INSTANCE>:postgres -p 5000:5000 -d burningraven06/flask-pg-jwt:d7
```

## Run App Locally

- Setup DB Info JWT Info
```sh
$ cd flask-pg-api
$ touch app/config/db_info.py
$ touch app/config/jwt_info.py
```

- Update **app/config/db_info.py**
```sh
PGDB_LOCALHOST_URI = <YOUR_PGDB_URI>
PGDB_DOCKER_COMPOSE_URI = ""
PGDB_DOCKER_LOCAL_URI = ""

#Remember, the URI Format is
# <DB_TYPE>://<DB_USERNAME>:<DB_PASSWORD>@<DB_HOST>:<DB_PORT>/<DB_NAME>
```

- Update **app/config/jwt_info.py**
```sh
JWT_TOKEN_SECRET = <YOUR_TOKEN_SECRET>
```

- Update **app/config/app_config.py**
```sh
# Change Line 6
SQLALCHEMY_DATABASE_URI = PGDB_DOCKER_COMPOSE_URI

#to
SQLALCHEMY_DATABASE_URI = PGDB_LOCALHOST_URI

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
$ pip install -r requirements.txt
```

- Start App (Prod Mode)
```sh
$ cd flask-pg-api
$ export FLASK_APP=flask_pg_jwt.py
$ flask run
```

- Start App (Debug Mode)
```sh
$ cd flask-pg-api
$ export FLASK_APP=flask_pg_jwt.py
$ export FLASK_ENV=development
$ flask run