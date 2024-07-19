# Utilizar la imagen base de Python 3.9
FROM python:3.9-slim-buster

# Instalar dependencias del sistema necesarias para SSL y OpenCV
RUN apt-get update -y && \
    apt-get install -y --no-install-recommends \
    apt-utils \
    build-essential \
    libssl-dev \
    libffi-dev \
    libbz2-dev \
    libreadline-dev \
    libsqlite3-dev \
    libgl1-mesa-glx \
    libcurl4-openssl-dev \
    libxml2-dev \
    libxslt1-dev \
    zlib1g-dev \
    curl \
    ca-certificates \
    python3-tk \
    tk-dev \
    xvfb && \
    apt-get clean

# Crear y establecer el directorio de trabajo
WORKDIR /home/src

# Copiar el archivo requirements.txt primero y instalar dependencias de Python
COPY requirements.txt .

# Actualizar pip y setuptools
RUN python -m ensurepip --upgrade && \
    pip install --upgrade pip setuptools && \
    pip install certifi

# Verificar instalación de SSL
RUN python -c "import ssl; print(ssl.OPENSSL_VERSION)"

# Instalar las dependencias de Python desde requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copiar todos los archivos al contenedor
COPY . .

# Limpiar el cache de apt
RUN apt-get clean

# Configurar y ejecutar `xvfb` antes de ejecutar el script principal, deshabilitar advertencias de TensorFlow
CMD ["sh", "-c", "Xvfb :99 -screen 0 1024x768x24 & export DISPLAY=:99 && export TF_CPP_MIN_LOG_LEVEL=2 && export CUDA_VISIBLE_DEVICES=-1 && python detector_neumonia.py"]
