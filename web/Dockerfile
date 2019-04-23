FROM python:3.7.2-slim

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN apt-get update gcc && apt-get install gcc && pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8002"]
