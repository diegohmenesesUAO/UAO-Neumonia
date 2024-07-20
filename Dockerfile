# Usa una imagen base de Python
FROM python:3.9-slim

# Instala las dependencias del sistema necesarias para Tkinter y otras bibliotecas
RUN apt-get update && apt-get install -y \
    python3-tk \
    libgl1-mesa-glx \
    libglib2.0-0 \
    libxrender1 \
    libxext6 \
    libsm6 \
    libx11-xcb1 \
    libxcomposite1 \
    libxcursor1 \
    libxdamage1 \
    libxfixes3 \
    libxi6 \
    libxrandr2 \
    libxtst6 \
    xauth \
    x11-apps \
    && rm -rf /var/lib/apt/lists/*

# Establece el directorio de trabajo
WORKDIR /app

# Copia el archivo requirements.txt y el archivo Python en el contenedor
COPY requirements.txt .
COPY detector_neumonia.py .
COPY model /app/model

# Instala las dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto del código de la aplicación en el contenedor
COPY . .

# Establece el comando para ejecutar la aplicación
CMD ["python", "detector_neumonia.py"]
