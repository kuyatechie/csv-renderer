FROM python:3.7.2-slim

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN apt-get update && \
    apt-get install gcc libsasl2-dev python-dev libldap2-dev libssl-dev -y && \
    pip install --no-cache-dir --default-timeout 120 --trusted-host pypi.python.org -r requirements.txt

COPY . .

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8002"]
