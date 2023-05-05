# pull official base image
FROM python:3.11-slim

# set environment variables
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# set timezone
ENV TZ="Europe/Moscow"

RUN pip3 install poetry
RUN poetry config virtualenvs.create false

# create directory
ENV APP_HOME=/home/api/backend
RUN mkdir -p $APP_HOME
RUN mkdir -p $APP_HOME/assets/media
RUN mkdir -p $APP_HOME/assets/static
WORKDIR $APP_HOME

# Install dependencies
COPY poetry.lock pyproject.toml ./
RUN poetry install

# copy project
COPY . .

# create appuser
RUN addgroup --system appgroup && adduser --system appuser && adduser appuser appgroup

# chown all the files to the appuser
RUN chown -R appuser:appgroup $APP_HOME

# change to the appuser
USER appuser
