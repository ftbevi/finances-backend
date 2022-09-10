FROM python:3.8-slim

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE 1
# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED 1

WORKDIR /server
COPY . /server

RUN apt-get update && apt-get install libpq-dev build-essential gdal-bin -y \
    && python3 -m pip install --upgrade pip \
    && python3 -m pip install -r requirements.txt

EXPOSE 6600

CMD gunicorn finances.wsgi:application --bind 0.0.0.0:6600
