FROM python:3.11.3

ADD . /wsgiproj
WORKDIR /wsgiproj

RUN pip install --upgrade pip && pip install -r requirements.txt