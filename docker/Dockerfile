FROM python:3.9

SHELL ["/bin/bash", "-c"]

WORKDIR /code/app

COPY ./requirements.txt /code/requirements.txt

RUN pip install --upgrade pip && pip install --no-cache-dir --upgrade -r /code/requirements.txt