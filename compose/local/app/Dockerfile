FROM python:3.7-slim-buster

RUN apt-get update && apt-get install -y \
    curl apt-utils apt-transport-https debconf-utils gcc build-essential g++\
    && rm -rf /var/lib/apt/lists/*

COPY ./requirements /requirements
ARG requirements=requirements/production.txt
RUN pip install --no-cache-dir -r $requirements

COPY ./compose/local/app/start /start
RUN sed -i 's/\r//' /start
RUN chmod +x /start

COPY ./app /app
WORKDIR /app/

ENV PYTHONPATH=/app
EXPOSE 80
EXPOSE 8888
