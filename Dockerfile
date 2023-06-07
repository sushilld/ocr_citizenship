# Base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

RUN apt-get update && apt-get install -y jq

COPY ./requirements.txt /app

RUN pip install --no-cache-dir -r requirements.txt

# Copy the app files to the container
ADD ./app /app

EXPOSE 8501

COPY ./config.sh /app

RUN chmod +x ./config.sh

CMD ["./config.sh"]