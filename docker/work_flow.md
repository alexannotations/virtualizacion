# Flujo de trabajo


## Introducir aplicaciones dentro de contenedores.

Para portabilidad y/o rápido despliegue podemos guardar aplicaciones en forma de plantillas para que así su instalación, peso y rendimiento sea mucho más eficiente. A este proceso se le conoce como _Dockerizar una aplicación_.

_Ejemplo de como hacer la dockerización:_

- Crea un archivo llamado _Dockerfile_ sin extensión. Dentro del archivo se le indica a Docker las acciones que debe hacer al momento de crear la imagen.

    - ```FROM <image>```: Este comando indica que se debe crear un contenedor basado en la imagen indicada.

- Despues de indicar la imagen con la que se va a crear el contenedor, se debe copiar el código fuente de la aplicación a la raíz del contenedor o en cualquier carpeta que consideremos conveniente.

    - `RUN mkdir -p /home/app`: Ejecuta el comando `mkdir` con el argumento `-p`, creación recursiva de rutas intermedias y tolerancia a directorios existentes parents.

    - `COPY . /home/app`: El comando copia desde la raíz de la ruta actual hacia la estructura de carpetas previamente creadas.

        > *Se usa COPY en lugar de RUN, la instrucción de RUN permite ejecutar instrucciones del SO Linux del contenedor, pero COPY permite acceder al sistema de archivos del equipo anfitrión para tomar esos archivos y después colocarlos dentro del contenedor.*

    - `EXPOSE 3000`: La aplicación a copiar en nuestro contenedor es un servidor realizado en express, se debe indicar a Docker que dicho servidor se mantendrá escuchando peticiones.

    - `CMD [”node” , ”/home/app/index.js”]`: Despues de crear la imagen, la estructura de archivos y copiado los archivos de la aplicación, se debe ejecutar el comando que correrá el contenedor resultante, en este caso es `CMD [”node” , ”/home/app/index.js”]`. El comando le indica a Docker que debe ejecutar el archivo _index.js_ con el comando `node`. El archivo resultante sería el siguiente: 

        ```Dockerfile
        FROM node:18

        RUN mkdir -p /home/app

        COPY . /home/app

        EXPOSE 3000

        CMD ["node", "/home/app/index.js"]
        ```





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





## Agrupar contenedores o asociarlos a la misma red

Una app y el manejador de base de datos pueden estar en contenedores distintos, pero no necesariamente se podrán comunicar entre si (aislados). Pueden tener comunicación hacia afuera de la red de su mismo contenedor gracias al mapeo de sus puertos, pero eso no quiere decir que entre los mismos contenedores se puedan comunicar. Para resolver esto se requiere agrupar los contenedores que necesitamos tengan comunicación entre si.*

Cuando varios contenedores de docker dentro de una misma red interna de docker necesitan comunicarse entre si, el nombre del dominio correspondiente a cada contenedor es el nombre con el cual este creado dichos contenedores.

Por ejemplo; cuando una app funciona en un contenedor y el manejador de BD MongoDB en otro contenedor en la misma red de contenedores, la forma en la que se debe hacer referencia en el URI para acceder a la BD debe ser, el nombre del contenedor que hace referencia a mongodb en vez de localhost, en este caso seria de esta forma:

```jsx
    {
        "mongodb://user:password@nombre_contenedorhost:27017/";
    }

```





## [Dockerfile](Dockerfile)



## Docker Compose


