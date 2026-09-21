# Docker
Crear, desplegar, ejecutar y gestionar aplicaciones dentro de contenedores. Los __contenedores__ son entornos ligeros y portátiles que encapsulan el código de una aplicación junto con todas sus dependencias, asegurando que se ejecuten de manera consistente en diferentes sistemas.

## Contenedores
Instancia en ejecución de una imagen. Es la imagen con su propio sistema de archivos y procesos, aislado del host.


## Imagenes
Plantilla de solo lectura con el código, dependencias y configuración de una app.
- Local (descargadas)
- Hub   (remotas)
- Artifactory (colecciones docker scout)


## Volumenes
Almacenamiento persistente accesibles por el OS e imagenes de docker, fuera del ciclo de vida del contenedor.


## Builds
Proceso de construir una imagen a partir de un Dockerfile (docker build). Cada instrucción del Dockerfile crea una capa; el resultado final es la imagen lista para correr. 





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
