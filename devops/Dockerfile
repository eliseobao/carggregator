FROM python:3.9-slim-bullseye
ARG UNAME=user

COPY devops/requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r /app/requirements.txt

RUN apt update && apt install git -y && \
    pip install git+https://github.com/jayzeng/scrapy-elasticsearch.git

ENV PATH=$PATH:/home/$UNAME/.local/bin

WORKDIR /app
