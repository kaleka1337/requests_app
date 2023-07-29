FROM python:3.10.3-slim

WORKDIR /app

COPY . .

RUN pip install requests
CMD ["python", "main.py"]