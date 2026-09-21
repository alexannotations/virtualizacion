# Flujo de trabajo

## Transformar un __Dockerfile__ en un __Docker container__

- _Dockerfile_: Es el punto inicial del proceso, el archivo crea una imagen.

- _Image_: ejecutar el comando ```docker build -t <nombre:tag> <path_to_Dockerfile>```, (una sola vez) ejecuta las instrucciones del _Dockerfile_ (RUN, COPY, ADD, etc.) y va creando capas con el resultado. Al final obtienes una ___Docker image___ ya armada. Si se modifica el _Dockerfile_, debe volver a hacer ```docker build``` para que los cambios se reflejen en una nueva imagen.

- _Container_: con el comando ```docker run```, (arranca) se despliega la _imagen_ ya construida creando un ___Docker container___ **nuevo** cada vez (```docker run``` = ```docker create``` + ```docker start```). Ejecuta el proceso definido en _CMD_ o _ENTRYPOINT_, es lo único que corre en cada _run_.


    En el ejemplo
    ```bash
    # Construye una imagen con <name>:<tag> desde un Dockerfile en la carpeta actual
    docker build -t mi-image-nginx:test .

    # Crea y ejecuta un contenedor con una sesión interactiva, borra automáticamente el contenedor (no la imagen) en cuanto termine de ejecutarse, mapeando puertos <host_destino>:<docker_port> a partir de una imagen <docker-image-name> y le asigna un nombre personalizado <docker-container-name>
    docker run -it --rm -p 8080:80 --name container-app1 mi-image-nginx:test

    curl http://localhost:8080
    ```



## [Dockerfile](Dockerfile)



## Docker Compose


