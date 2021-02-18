FROM ubuntu:python3.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DEBUG 0

RUN apt update && apt upgrade -y \
    apt install -y python3-dev libmysqlclient 

WORKDIR /app

RUN pip install --upgrade pip

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt


COPY . .

CMD python manage.py runserver 0.0.0.0:$PORT