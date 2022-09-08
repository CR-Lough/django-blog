FROM python:3.8-slim

LABEL maintainer="Connor Lough"

RUN useradd -r -m -U djangouser

COPY --chown=djangouser:djangouser ./requirements.txt .
RUN pip install -r requirements.txt --no-cache-dir && \ 
    rm requirements.txt

RUN apt-get update && \
    apt-get install -y --no-install-recommends build-essential
COPY --chown=djangouser:djangouser . .

USER djangouser
WORKDIR /django_blog/mysit 

