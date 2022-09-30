FROM python:3.9-slim-bullseye

COPY devops/dev/requirements.txt /app/requirements.txt
ARG UNAME=user
ARG UID=1000
ARG GID=1000

RUN groupadd -g $GID -o $UNAME \
    && useradd -m -u $UID -g $GID -o -s /bin/bash $UNAME

USER $UNAME

RUN pip install --no-cache-dir -r /app/requirements.txt
ENV PATH=$PATH:/home/$UNAME/.local/bin

WORKDIR /app