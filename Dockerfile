FROM python:3.5-alpine

RUN apk update
RUN apk add bash
RUN pip install --upgrade pip
RUN pip install Flask flask-login

ADD code /code

EXPOSE 5000

ENTRYPOINT ["python", "/code/web.py"]
