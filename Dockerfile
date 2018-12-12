# Specify Python Version
FROM python:3.6-alpine

#Some Jazz
LABEL maintainer="Toufiq - burningraven06@gmail.com"

#Just create a working directory
WORKDIR /flask-pg-api-jwt

#Copy requirements.txt for python packages to be installed
COPY requirements.txt requirements.txt

#This is Python Specific, install python compilers, and postgres-python os-related-depencencies 
RUN apk add gcc build-base python3-dev libffi-dev postgresql-dev

# Create Python3 Virtual Environment
RUN python3 -m venv venv

#Start Virtual Environment
RUN source venv/bin/activate

# Install Package Dependencies
RUN pip install -r requirements.txt

# Copy all source files to WorkDir
COPY . . 

#These are Flask Specific commands, setup Env Var for flask app
ENV FLASK_APP flask_pg_jwt.py
ENV FLASK_ENV=development

#Expose port
EXPOSE 5000

#Start App
CMD ["flask", "run" , "--host=0.0.0.0"]
