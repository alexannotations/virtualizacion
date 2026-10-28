# Docker Cheatsheet


## Imágenes <a id="imagenes"></a>

| Comando | Descripción |
|---|---|
| `docker build -t <nombre:tag> .` | Construir una nueva imagen de Docker a partir de un archivo de instrucciones _Dockerfile_ y empaquetarla bajo un nombre y versión específicos en la carpeta actual |
| `docker build -t <nombre:tag> . --no-cache` | Construye una imagen con `--tag` sin usar la caché |
| `docker images` | Lista las imágenes locales |
| `docker images --filter=reference='*/*:*' --filter=reference='*:*'` | Filtra la lista de imagenes locales segun el criterio `usuario/repositorio:tag` o `repositorio:tag`|
| `docker images --no-trunc` | Muestra la información completa sin recortar los identificadores ni los valores largos |
| `docker pull <imagen>:<tag>` | Descarga una imagen (remota) desde un registro |
| `docker push <imagen>` | Sube una imagen a un registro |
| `docker tag <imagen> <nuevo_nombre:tag>` | Etiqueta una imagen local |
| `docker rmi <id_imagen>` | Elimina una imagen |
| `docker image prune` | Elimina imágenes no utilizadas |
| `docker save -o <archivo.tar> <imagen>` | Guarda una imagen en un archivo tar |
| `docker load -i <archivo.tar>` | Carga una imagen desde un archivo tar |
| `docker history <imagen>` | Muestra el historial de capas de una imagen |
| `docker search <término>` | Busca una imagen en Docker Hub |


## Contenedores <a id="contenedores"></a>

| Comando | Descripción |
|---|---|
| `docker run --name <contenedor_nombre> <imagen>` | Crea y ejecuta un contenedor a partir de una imagen y le asigna un nombre personalizado |
| `docker run -d <imagen>` | Descarga una imagen (de no existir) y crea un contenedor, ejecutandolo en segundo plano (detached) |
| `docker run -p <puerto_host>:<puerto_cont> <imagen>` | Publica un puerto del contenedor al host |
| `docker create <imagen>` | Crea un contenedor sobre la imagen indicada sin iniciarlo |
| `docker create --name <nombre_contenedor> <imagen>` | Crea un contenedor sobre la `<imagen>` indicada pero con el nombre especificado en el parámetro `<nombre_contenedor>` |
| `docker start <nombre/id>` | Inicia un contenedor detenido |
| `docker stop <nombre/id>` | Detiene un contenedor en ejecución |
| `docker stop $(docker ps -q)` | Detiene todos los contenedores activos  |
| `docker restart <nombre/id>` | Reinicia un contenedor |
| `docker pause` / `docker unpause` | Pausa / reanuda los procesos de un contenedor |
| `docker kill <nombre/id>` | Fuerza la detención de un contenedor |
| `docker rm <nombre/id>` | Elimina un contenedor detenido (`-f` para forzar) |
| `docker rename <viejo> <nuevo>` | Renombra un contenedor |
| `docker ps` | Lista contenedores en ejecución |
| `docker ps -a` | Lista todos los contenedores (incluyendo detenidos) |


## Inspección y diagnóstico  <a id="inspeccion-y-diagnostico"></a>

| Comando | Descripción |
|---|---|
| `docker system df -v` | Desglose completo, incluyendo el tamaño de cada volumen |
| `docker logs <contenedor_nombre/id>` | Muestra los logs de un contenedor, el historial actual y finaliza de inmediato |
| `docker logs -f <nombre/id>` | Sigue los logs en tiempo real |
| `docker exec -it <nombre/id> bash` | Entra a un contenedor existente en ejecucion por una shell interactiva en el contenedor (usa `sh` si `bash` no existe) |
| `docker attach <nombre/id>` | Conecta la terminal actual a un contenedor en ejecución |
| `docker inspect <nombre/id>` | Muestra información detallada del objeto (contenedor o imagen) |
| `docker stats` | Uso de CPU, RAM y red en tiempo real de todos los contenedores |
| `docker top <nombre/id>` | Procesos en ejecución dentro de un contenedor |
| `docker diff <nombre/id>` | Cambios en el filesystem del contenedor |
| `docker port <nombre/id>` | Mapeos de puertos del contenedor |
| `docker events` | Eventos en tiempo real del daemon de Docker |
| `docker info` | Información general del sistema Docker |
| `docker version` | Versión de Docker |


## Copia e import/export  <a id="copia-import-export"></a>

| Comando | Descripción |
|---|---|
| `docker cp <origen> <destino>` | Copia archivos entre el host y un contenedor |
| `docker export <nombre/id> > archivo.tar` | Exporta el filesystem de un contenedor a un tar |
| `docker import archivo.tar` | Crea una imagen a partir de un tar exportado |
| `docker commit <nombre/id> <nueva_imagen>` | Crea una imagen a partir de los cambios de un contenedor |


## Redes <a id="redes"></a>

| Comando | Descripción |
|---|---|
| `docker network ls` | Lista las redes de contenedores existentes |
| `docker network create <nombre_red>` | Crea una red de contenedores |
| `docker network connect <red> <contenedor>` | Conecta un contenedor a una red |
| `docker network disconnect <red> <contenedor>` | Desconecta un contenedor de una red |
| `docker network inspect <red>` | Detalles de una red |
| `docker network rm <red>` | Elimina una red |


## Volúmenes <a id="volumenes"></a>

| Comando | Descripción |
|---|---|
| `docker volume create <nombre>` | Crea un volumen persistente |
| `docker volume ls` | Lista los volúmenes |
| `docker run -v <volumen>:<ruta_contenedor> <imagen>` | Monta (conecta) un volumen persistente en una ruta interna del contenedor |
| `docker run --mount source=<volumen>,target=<ruta_contenedor> <imagen>` | Alternativa explícita a `-v` para montar el volumen |
| `docker run -v $(pwd)/datos:/var/lib/mysql mysql` __o__ <br> `docker run --mount type=bind,source="$(pwd)/datos",target=/var/lib/mysql mysql` | (_Bind mount_) Monta un directorio local de la máquina host en el contenedor.<br> *`$(pwd)` resuelve la ruta absoluta de la carpeta donde estas en tu terminal  **+**  `/datos`*  y<br>  *`/var/lib/mysql` es la ruta interna dentro del contenedor donde MySQL almacena sus tablas y registros* |
| `docker volume inspect <nombre>` | Detalles de un volumen |
| `docker volume rm <nombre>` | Elimina un volumen |


## Registro (login)

| Comando | Descripción |
|---|---|
| `docker login` | Inicia sesión en un registro |
| `docker logout` | Cierra sesión de un registro |


## Limpieza del sistema

| Comando | Descripción |
|---|---|
| `docker system prune` | Elimina contenedores detenidos, redes sin uso e imágenes sin etiquetar |
| `docker system prune -a` | Igual que arriba, incluyendo imágenes no asociadas a un contenedor activo |
| `docker container prune` | Elimina todos los contenedores detenidos |
| `docker image prune` | Elimina imágenes sin uso |
| `docker volume prune` | Borra permanentemente los datos de cualquier volumen que no esté referenciado por al menos un contenedor (activo o detenido). Antes de correrlo, confirma con ```docker volume ls -f dangling=true``` cuáles se van a borrar. |


## Docker Compose <a id="compose"></a>

| Comando | Descripción |
|---|---|
| `docker compose up -d` | Construye/crea/inicia todos los servicios en segundo plano definidos en el archivo _docker-compose.yml_ |
| `docker compose -f <archivo> up` | Inicia los servicios utilizando un archivo Compose con nombre o ruta personalizada, en lugar del predeterminado _docker-compose.yml_ |
| `docker compose down` | Detiene y elimina contenedores y redes creadas por el proyecto (Conserva los volúmenes con nombre (named volumes), montajes vinculados (bind mounts) y las imágenes descargadas/construidas) |
| `docker compose down -v` | Detiene y elimina contenedores, redes y volúmenes asociados al proyecto.
| `docker compose logs -f` | Logs unificados en tiempo real de todos los servicios definidos en el _docker-compose.yml_ |
| `docker compose logs -f <servicio>` | Sigue los logs en tiempo real unicamente del servicio indicado |

El flag `-f` (follow) funciona igual que `tail -f`: mantiene la terminal abierta transmitiendo nuevos logs en tiempo real hasta pulsar _Ctrl + C_.

## Referencia

https://docs.docker.com/get-started/docker_cheatsheet.pdf
