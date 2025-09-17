FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN apt-get update && apt-get install -y dos2unix netcat-traditional

COPY . .
RUN dos2unix /django_app/entrypoint.sh
RUN chmod 777 /django_app/entrypoint.sh

ENTRYPOINT ["/app/entrypoint.sh"]
