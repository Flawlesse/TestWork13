FROM python:3.11-slim

WORKDIR /app/backend

RUN apt-get update && apt-get install -y dos2unix netcat-traditional

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
RUN dos2unix /app/backend/entrypoint.sh
RUN chmod 777 /app/backend/entrypoint.sh

ENTRYPOINT ["/app/backend/entrypoint.sh"]
