# syntax=docker/dockerfile:1
FROM python:3.10-slim-bullseye

COPY . /src
COPY requirements.txt ./
RUN pip3 install -r requirements.txt
 
CMD python3 /src/core/webcam.py