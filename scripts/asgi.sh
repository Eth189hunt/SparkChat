#!/bin/sh

./scripts/deploy-setup.sh
gunicorn --bind 0.0.0.0:8000 config.asgi -w 4 -k uvicorn.workers.UvicornWorker