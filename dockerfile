# 用來啟動 django 後端

# syntax=docker/dockerfile:1
FROM python:3.12-bookworm
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /backend
COPY requirements.txt /backend/
RUN pip3 install -r requirements.txt
COPY . /backend/
