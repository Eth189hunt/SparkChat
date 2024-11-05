# Django template
A template for Django with React.

Includes pages for registration and login.
/account/login

# Run on see on your computer

Install docker

Clone the repo on your computer

Copy the env.dev.example to .env.dev

Have Docker and in the clone run the run commmand

docker compose up --build --remove-orphans

For the first run must migrate the database see commands to run in the container below

Then goto http://localhost:8000/

# Commands to run commands in the container

list containers names look for container name with web
docker ps
(name should be something like sparkchat-web-1)

Must be in `docker exec -it <containter_name> /bin/bash`

# Migrations
To migrate all the models to the database:
python3 manage.py migrate

To make migrations for an app:
python3 manage.py makemigrations <app_name>

To migrate models for an app:
python3 manage.py migrate <app_name>

# Production Launch Code

First copy and enter `.env` file.(use `ls -a` to check for it.)

In Djangotemplate file.
```sudo sh ./start.sh```
