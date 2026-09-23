FROM python:3.12-slim

# Dependencias del sistema necesarias para mysqlclient
RUN apt-get update && apt-get install -y \
    default-libmysqlclient-dev \
    pkg-config \
    gcc \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# El código real se monta como volumen (ver docker-compose.yml),
# así que los cambios que hagas se reflejan sin reconstruir la imagen.
