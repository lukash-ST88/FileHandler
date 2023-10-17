FROM python:3.11-alpine3.17

COPY requirements.txt /requirements.txt

COPY . /FileHandler

WORKDIR /FileHandler

RUN pip install -r /requirements.txt





