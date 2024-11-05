# Django template
A template for Django with React.

Includes pages for registration and login.
/account/login

# Run on see on your computer

Install docker

Clone the repo on your computer

Have Docker and in the clone run the run commmand

docker compose up --build --remove-orphans

Then goto http://localhost:8000/

# Commands to run commands in the container

list containers names look for web
docker ps

Must be in `docker exec -it <containter_name> /bin/bash`

# Production Launch Code

First copy and enter `.env` file.(use `ls -a` to check for it.)

In Djangotemplate file.
```sudo sh ./start.sh```
