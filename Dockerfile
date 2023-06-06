FROM python:3.10

# set a directory for the app
WORKDIR /app

COPY requirements.txt /app/requirements.txt
COPY config.json /app/config.json

COPY startup.sh /app/startup.sh
RUN chmod +x /app/startup.sh

RUN pip install --no-cache-dir -r requirements.txt

ADD ./app /app
