##

## Requisitos para la ejecución del programa

- Docker instalado en tu sistema.
- Servidor X11 en funcionamiento en tu máquina host.

### Instalación del servidor X11

#### En macOS:
1. Descarga e instala XQuartz desde [https://www.xquartz.org/](https://www.xquartz.org/).
2. Inicia XQuartz desde tu carpeta de aplicaciones.
3. Permite conexiones desde clientes de red:
   - Abre las preferencias de XQuartz (`XQuartz -> Preferences` en la barra de menú).
   - Ve a la pestaña "Security" y marca la opción "Allow connections from network clients".
4. En una terminal, ejecuta:
   ```bash
   xhost + 127.0.0.1

### En Linux:
X11 debería estar instalado por defecto. Solo necesitas permitir el acceso al servidor X11:
- xhost +local:docker

## Construcción de la Imagen Docker
1. Clona este repositorio o descarga los archivos necesarios, incluyendo Dockerfile, requirements.txt y detector_neumonia.py.

2. Navega al directorio donde se encuentran estos archivos y construye la imagen de Docker:
docker build -t detector_neumonia .

## Ejecución del Contenedor Docker
1. Permite el acceso al servidor X11

2. Ejecuta el contenedor de Docker, configurando la variable DISPLAY para que la aplicación gráfica se muestre en tu host:
-   docker run -it --rm \
     -e DISPLAY=$DISPLAY \
     -v /tmp/.X11-unix:/tmp/.X11-unix \
     detector_neumonia

### Implementación de Alta cohesión y bajo acomplamiento
1.	Alta cohesión:
- Clase ModelHandler: Se encarga de todas las operaciones relacionadas con el modelo de TensorFlow, incluyendo la predicción y la generación de Grad-CAM.
- Clase ImageProcessor: Maneja todas las tareas relacionadas con la lectura y preprocesamiento de imágenes.
- Clase App: Coordina la interfaz gráfica y las interacciones con ModelHandler y ImageProcessor.

2.	Bajo acoplamiento:
- 	Clases independientes: App utiliza ModelHandler e ImageProcessor a través de métodos bien definidos. App no necesita conocer los detalles internos de estas clases, solo cómo usarlas.
- 	Interacción clara: Cada clase tiene una responsabilidad específica y sus métodos se usan para realizar tareas específicas, manteniendo el acoplamiento al mínimo.


## Proyecto original realizado por:

Isabella Torres Revelo - https://github.com/isa-tr
Nicolas Diaz Salazar - https://github.com/nicolasdiazsalazar

## Proyecto modificado por :

Diego Meneses - https://github.com/diegohmenesesUAO/UAO-Neumonia

