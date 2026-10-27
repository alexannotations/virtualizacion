Diferentes formas de ejecutar esta app de ejemplo
Consultar el endpoint: `curl http://127.0.0.1:5000/getmyinfo`


# Contenedor con Docker directo

Aisla las dependencias en una imagen autónoma sin necesidad de instalar Python ni librerías en el host.

- Crear un archivo [_Dockerfile_](Dockerfile) en la misma carpeta:

- Asegurar tu [_requirements.txt_](requirements.txt):

- Construir la imagen y levantar el contenedor:

```bash
# Construir (o reconstruir) la imagen
docker build -t test-flask-api:1.0 .

# Ejecutar el contenedor
docker run -d --name mi-api-flask -p 5000:5000 test-flask-api:1.0
```


---


# Orquestado con Docker Compose
Ideal si esta API se va a conectar con una base de datos o integrarla en un flujo de despliegue continuo.

- Crea un archivo _docker-compose.yml_:

```YAML
services:
  api:
    build: .
    container_name: flask-api
    ports:
      - "5000:5000"
    environment:
      - FLASK_ENV=production
    restart: unless-stopped
```

- Ejecuta:

```Bash
docker compose up -d
```


---


# Ejecutar en entorno virtual

Python crea una instalación aislada con su propio intérprete, su propio pip y sus propias librerías sin afectar al Python global del sistema operativo.

- Crear y activar el entorno virtual:

```Bash
python3 -m venv venv

source venv/bin/activate

# o
source venv/bin/activate.fish
```

- Instalar dependencias:

    ```Bash
    python -m pip install flask flask-cors
    ```

- Ejecutar el servidor de desarrollo:

    - Directamente con Python:

    ```Bash
    python app.py
    ```

    - O utilizando el CLI nativo de Flask (con recarga automática ante cambios de código):

    ```Bash
    flask --app app run --debug --host=0.0.0.0 --port=5000
    ```

- Para salir de un entorno virtual de Python, ejecuta:

```Shell
deactivate
```


---


# Ejecutar con un servidor WSGI de producción (Gunicorn)

El servidor integrado de Flask es monoproceso y solo sirve para desarrollo local. En producción, se debe ejecutar detrás de un servidor WSGI como Gunicorn.

- Instalar Gunicorn en tu entorno:

```Bash
pip -m install gunicorn
```

- Lanzar la aplicación:

```Bash
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

`-w 4`: Inicia 4 procesos trabajadores concurrentes (regla general: `2 * CPUs + 1`).

`-b 0.0.0.0:5000`: Escucha en todas las interfaces de red en el puerto _5000_.

`app:app`: Refiere al archivo _app.py_ y a la instancia `app = Flask(__name__)`.


---


