# Utilizar una imagen base de Python 3.9
FROM python:3.9

# Establecer el directorio de trabajo
WORKDIR /home/src

# Copiar los archivos requirements.txt al contenedor
COPY requirements.txt .

# Instalar las dependencias del sistema y de Python
RUN apt-get update -y && \
    apt-get install -y --no-install-recommends \
    apt-utils build-essential libssl-dev libffi-dev python3-dev && \
    apt-get install -y curl libcurl4-openssl-dev ca-certificates && \
    update-ca-certificates && \
    python -m ensurepip --upgrade && \
    pip install --upgrade pip setuptools wheel && \
    pip install --no-cache-dir -r requirements.txt && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Copiar todos los archivos al contenedor
COPY . .

# Exponer el puerto que usa MLflow para la interfaz web
EXPOSE 5000

# Comando para ejecutar el script principal
CMD ["python", "detector_neumonia.py"]
