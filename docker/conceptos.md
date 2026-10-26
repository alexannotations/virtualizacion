# Docker
Plataforma de código abierto diseñada para crear, desplegar, ejecutar y gestionar aplicaciones dentro de contenedores. Los __contenedores__ son entornos ligeros y portátiles que encapsulan el código de una aplicación junto con todas sus dependencias, asegurando que se ejecuten de manera consistente en diferentes sistemas.

$$\text{Sistema Host} \supset \text{Contenedor} \supset \{\text{Capa Efímera (R/W)}, \text{Imagen (R/O)}, \text{Procesos (PID 1)}\}$$


## Contenedores

Instancia en ejecución y mutable de una imagen. Representa un entorno aislado del host con su propio árbol de procesos, sistema de archivos de escritura efímero (overlay), interfaces de red y variables de entorno.

- __Ciclo de vida__: created, running, paused, exited y removed.

- __Capa de lectura y escritura__: Cuando el contenedor arranca, Docker añade una capa ligera de escritura (container layer) sobre las capas de solo lectura de la imagen. Todos los cambios temporales (creación de ficheros de log, temporales, etc.) residen aquí hasta que el contenedor se destruye.

- [Comandos esenciales](comandos.md#contenedores):



## Imágenes

Plantilla inmutable (de solo lectura) compuesta por una secuencia de capas superpuestas que contienen el sistema base, las dependencias, configuraciones y el binario de la aplicación. Cuando tienen exactamente el mismo ID, son la misma imagen en disco (sin ocupar doble espacio), solo que etiquetada con dos nombres distintos.

- Tipos de almacenamiento y registries:

    - __Local__: Imágenes descargadas o construidas presentes en el almacenamiento local del host (`docker images`).

    - __Docker Hub__: Registro público oficial por defecto para distribuir y descargar imágenes comunitarias y oficiales (`library/node`, `library/mariadb`).

    - __Private Registries / Artifactory__: Servidores privados para almacenar artefactos de la empresa (JFrog Artifactory, AWS ECR, GCP Artifact Registry, GitHub Packages).

    - __Docker Scout__: Herramienta integrada para análisis de seguridad, inspección de dependencias (SBOM) y detección de vulnerabilidades (CVEs) en las imágenes.

    - [Comandos esenciales](comandos.md#imagenes):



## Volúmenes

Mecanismo principal para almacenar datos de forma persistente, accesibles por el OS e imagenes de docker, independiente del ciclo de vida de los contenedores. Los datos guardados en la capa del contenedor se pierden al destruirlo; los volúmenes evitan esta pérdida.

- Estrategias de almacenamiento:

    - __Named Volumes__ (`docker volume`): Gestionados directamente por Docker dentro del directorio del daemon (`/var/lib/docker/volumes/`). Es la opción recomendada para bases de datos (MariaDB, PostgreSQL, MySQL) por su rendimiento y seguridad.

    - __Bind Mounts__: Mapeo directo de un directorio o fichero del host hacia el contenedor (ej. `-v $(pwd):/app`). Ideal en desarrollo local para reflejar cambios de código en caliente sin reconstruir la imagen.

    - __tmpfs__: Almacenamiento no persistente alojado directamente en la memoria RAM del host; útil para datos sensibles o caché temporal de alto rendimiento.

    - [Comandos esenciales](comandos.md#volumenes):



## Builds

Proceso de empaquetar una aplicación dentro de una _imagen_ ejecutable mediante un fichero descriptivo llamado _Dockerfile_. Cada instrucción del _Dockerfile_ crea una capa; el resultado final es la imagen lista para correr. 

- Instrucciones clave del Dockerfile:

    - __FROM__: Define la imagen base (ej. node:22-alpine, php:8.3-fpm).

    - __WORKDIR__: Establece el directorio de trabajo relativo dentro del contenedor.

    - __COPY / ADD__: Copia ficheros del contexto local al sistema de archivos de la imagen.

    - __RUN__: Ejecuta comandos durante el proceso de construcción (instalar paquetes, compilar dependencias). Crea una nueva capa de caché.

    - __ENV / ARG__: Variables de entorno para ejecución y argumentos para la compilación respectivamente.

    - __EXPOSE__: Documenta los puertos de red en los que la aplicación escucha.

    - __ENTRYPOINT / CMD__: Especifica el ejecutable principal y sus argumentos por defecto al arrancar el contenedor.

- [Comandos esenciales ```docker build```](comandos.md#volumenes):



## Redes (Networks)

Mecanismo de aislamiento y comunicación entre contenedores o entre contenedores y el exterior.

- Drivers de red comunes:

    - __bridge__ (por defecto): Red virtual privada dentro del host. Permite resolución automática de DNS por nombre de contenedor cuando se usan redes bridge definidas por el usuario.

    - __host__: Elimina el aislamiento de red entre el contenedor y el host (usa directamente los puertos del sistema anfitrión).

    - __none__: Desactiva todo acceso a la red para el contenedor.

    - __overlay__: Red distribuida entre múltiples hosts físicos o virtuales (usado en Docker Swarm o clusters).

- [Comandos esenciales](comandos.md#redes):



## Docker Compose

Herramienta declarativa para definir y ejecutar aplicaciones Docker de múltiples contenedores mediante un archivo _docker-compose.yml_.

- Orquesta servicios complementarios (ej. frontend en Node, backend en PHP, base de datos MariaDB y servidor SMTP de pruebas como Mailpit).

- Crea de forma automática una red compartida y volúmenes declarados para intercomunicar los servicios usando sus nombres como alias de red.

- [Comandos esenciales](comandos.md#compose):







# Docker desktop

## Docker Scout
Herramienta de análisis de seguridad de imágenes. Revisa capas y dependencias en busca de CVEs, te dice qué paquetes están desactualizados y sugiere bases más seguras/livianas.


## Docker hub
Registro público (o privado) de plantillas en la nube. Aloja imágenes oficiales y permite automatizar builds desde un repo de GitHub.


## Extensions
Plugins que se agregan a Docker Desktop (o a la CLI) para añadir funcionalidad extra


## Ask Gordon (Beta)
Esta es la integración de Inteligencia Artificial Generativa dentro de Docker Desktop. "Gordon" (nombrado en honor a Gordon the Gopher, la mascota de Go, el lenguaje en que está escrito Docker) es un asistente de IA.


## Kubernetes
Permite gestionar un clúster de Kubernetes completo que se ejecuta localmente dentro de Docker Desktop.
Kubernetes (___K8s___) es el orquestador de contenedores. Esta función permite probar y desarrollar aplicaciones en un entorno Kubernetes realista sin necesidad de conectarte a un proveedor en la nube.

Por defecto, está deshabilitado, al hacer clic en _"Create cluster"_ (o habilitándolo desde _Settings > Kubernetes_), Docker Desktop descargará los componentes necesarios y arrancará un clúster K8s de un solo nodo. Una vez activo, podrás usar comandos de Kubernetes (```kubectl```) directamente en tu terminal, apuntando a este clúster local.

Es una herramienta invaluable para desarrolladores que trabajan con microservicios y se preparan para un despliegue en producción.


## Builds
Es un panel de control visual para tus construcciones de imágenes (```docker build```).
Ofrece una vista centralizada de todo el historial de las imágenes que has construido localmente.

- Historial de Builds: Lista cada vez que ejecutaste docker build.
- Debugging: Si un build falla, puedes inspeccionarlo aquí para ver exactamente en qué capa (RUN, COPY, etc.) ocurrió el error.
- Gestión de Cache: Te permite ver qué capas se reutilizaron (cache) y cuáles se reconstruyeron, ayudándote a optimizar la velocidad de tus Dockerfiles.
- Docker Build Cloud: Promociona el servicio en la nube de Docker para acelerar las compilaciones (especialmente para equipos).


## Models
Es un "Docker Hub" pero específicamente para modelos de IA (Machine Learning).

- _Docker Hub (Remoto)_: Te permite explorar, descargar (pull) y gestionar modelos de IA populares (como gpt-oss, qwen3-embedding de tu captura) que ya están empaquetados como imágenes de Docker.
- _Local_: Muestra los modelos de IA que ya tienes descargados en tu máquina.
- _Contexto_: Configurar un entorno para correr modelos de IA es notoriamente difícil (dependencias de Python, versiones de CUDA para GPUs, etc.). Esta pestaña simplifica todo: solo descargas la imagen del modelo y la ejecutas como cualquier otro contenedor.


## MCP Toolkit (Beta)
"_Model-as-a-Container Playground_" o "_Model Context Protocol_". Es un conjunto de herramientas para construir tus propias aplicaciones potenciadas por IA.

Mientras que la pestaña __Models__ te da el modelo de IA, el __MCP Toolkit__ te da las herramientas para que ese "cerebro" interactúe con el mundo.

- Catalog: Una lista de "servidores" o "herramientas" pre-construidas que tu IA puede usar.
    - Fetch (Reference): Para que la IA pueda leer contenido de una URL.
    - Slack (Archived): Para interactuar con Slack.
    - Playwright: Para que la IA pueda controlar un navegador web y "ver" o interactuar con páginas.
    - PostgreSQL: Para conectarse a una base de datos.
- My servers: Las herramientas del catálogo que has decidido instalar y ejecutar.
- Clients: Aplicaciones (como Claude Code o Codex) que puedes conectar a tus servidores para construir un flujo de trabajo de IA.
