FROM python:3.11-buster

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH="${PYTHONPATH}:/src"

WORKDIR /src

COPY . /src
RUN apt-get -y update
RUN apt-get -y upgrade
RUN apt-get install -y ffmpeg
RUN python -m pip install --upgrade pip && python -m pip install --requirement requirements.txt

ENTRYPOINT python -m alembic upgrade head && python main.py