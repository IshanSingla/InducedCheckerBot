FROM python:3.9

RUN apt update && apt upgrade -y
RUN pip3 install --upgrade pip
