FROM python:3.9.6

COPY requirements.txt /install/requirements.txt 
 # /install 로 옮기는 이유가 있나?
RUN python -m pip install --upgrade pip
RUN pip install -r /install/requirements.txt

WORKDIR /app

ENV LANG=ko_KR.utf8
ENV TZ=Asia/Seoul
ENV FASTAPI_ENV="docker" 
ENV FASTAPI_APP=main.py
ENV APP_ENV="local"  

# FROM base as debug
# Debug image reusing the base
# Install dev dependencies for debugging
# RUN pip install ptvsd debugpy
# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE 1
# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

ARG APP_PORT
EXPOSE ${APP_PORT}

ARG BUILD_VER
ENV BUILD_VER=${BUILD_VER}