FROM python:3.10

ENV PYTHONUNBUFFERED 1

WORKDIR /app

ADD . /app

RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt
