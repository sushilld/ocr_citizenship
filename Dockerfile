# Base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

RUN pip install --upgrade pip

COPY ./requirements.txt /app

RUN pip install --no-cache-dir -r requirements.txt

# Copy the app files to the container
ADD ./app /app

EXPOSE 8501

# Set the entrypoint command
CMD ["streamlit", "run", "app.py","--"]