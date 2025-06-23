# Use lite python official image
FROM python:3.10-slim

WORKDIR /app

RUN mkdir -p utils

COPY utils/cfg_parser.py ./utils/
COPY utils/cleaner.py ./utils/
COPY utils/inet_checker.py ./utils/
COPY utils/logo.py ./utils/
COPY utils/recomendations.py ./utils/
COPY utils/write_device_output.py ./utils/
COPY requirements.txt .
COPY main.py .
COPY settings.json .
COPY README.md .
COPY LICENSE .

RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["python", "main.py"]