FROM python:3.8-buster

RUN pip install pipenv

WORKDIR /app
ADD . /app

RUN pipenv install
EXPOSE 80

CMD ["pipenv", "run", "./run.sh"]
