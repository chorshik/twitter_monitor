FROM python:3.10.8-slim-buster

ENV PYTHONPATH=${PYTHONPATH}:${PWD} \
    POETRY_VERSION=1.3.2

WORKDIR /src
COPY /src /src
COPY pyproject.toml poetry.lock /src/

RUN pip3 install poetry==$POETRY_VERSION
RUN poetry config virtualenvs.create false
RUN poetry update before poetry install --no-interaction --no-ansi -vvv

CMD python main.py
