FROM python:3.6 

MAINTAINER yanix "smirnovskoe@gmail.com"

RUN python3-pip
RUN mkdir -p /usr/src/app

WORKDIR /usr/src/app

COPY . /usr/src/app

RUN pip3 install -r requirements.txt