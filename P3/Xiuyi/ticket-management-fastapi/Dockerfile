FROM python:3.9-slim AS base

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY ./src ./src

EXPOSE 8000

CMD ["uvicorn", "ticket_management.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]