# Docker Cheatsheet


## Imágenes

| Comando | Descripción |
|---|---|
| `docker build -t <nombre:tag> .` | Construye una imagen desde un Dockerfile en la carpeta actual |
| `docker build -t <nombre:tag> . --no-cache` | Construye sin usar la caché |
| `docker images` | Lista las imágenes locales |
| `docker pull <imagen>` | Descarga una imagen desde un registro |
| `docker push <imagen>` | Sube una imagen a un registro |
| `docker tag <imagen> <nuevo_nombre:tag>` | Etiqueta una imagen local |
| `docker rmi <imagen>` | Elimina una imagen |
| `docker image prune` | Elimina imágenes no utilizadas |
| `docker save -o <archivo.tar> <imagen>` | Guarda una imagen en un archivo tar |
| `docker load -i <archivo.tar>` | Carga una imagen desde un archivo tar |
| `docker history <imagen>` | Muestra el historial de capas de una imagen |
| `docker search <término>` | Busca una imagen en Docker Hub |

## Contenedores

| Comando | Descripción |
|---|---|
| `docker run --name <nombre> <imagen>` | Crea y ejecuta un contenedor a partir de una imagen y le asigna un nombre personalizado |
| `docker run -d <imagen>` | Ejecuta en segundo plano (detached) |
| `docker run -p <puerto_host>:<puerto_cont> <imagen>` | Publica un puerto del contenedor al host |
| `docker create <imagen>` | Crea un contenedor sin iniciarlo |
| `docker start <nombre/id>` | Inicia un contenedor detenido |
| `docker stop <nombre/id>` | Detiene un contenedor en ejecución |
| `docker restart <nombre/id>` | Reinicia un contenedor |
| `docker pause` / `docker unpause` | Pausa / reanuda los procesos de un contenedor |
| `docker kill <nombre/id>` | Fuerza la detención de un contenedor |
| `docker rm <nombre/id>` | Elimina un contenedor detenido (`-f` para forzar) |
| `docker rename <viejo> <nuevo>` | Renombra un contenedor |
| `docker ps` | Lista contenedores en ejecución |
| `docker ps -a` | Lista todos los contenedores (incluyendo detenidos) |

## Inspección y diagnóstico

| Comando | Descripción |
|---|---|
| `docker system df -v` | Desglose completo, incluyendo el tamaño de cada volumen |
| `docker logs <nombre/id>` | Muestra los logs de un contenedor |
| `docker logs -f <nombre/id>` | Sigue los logs en tiempo real |
| `docker exec -it <nombre/id> bash` | Abre una shell interactiva (usa `sh` si `bash` no existe) |
| `docker attach <nombre/id>` | Conecta la terminal actual a un contenedor en ejecución |
| `docker inspect <nombre/id>` | Muestra información detallada del objeto (contenedor o imagen) |
| `docker stats` | Uso de CPU, RAM y red en tiempo real de todos los contenedores |
| `docker top <nombre/id>` | Procesos en ejecución dentro de un contenedor |
| `docker diff <nombre/id>` | Cambios en el filesystem del contenedor |
| `docker port <nombre/id>` | Mapeos de puertos del contenedor |
| `docker events` | Eventos en tiempo real del daemon de Docker |
| `docker info` | Información general del sistema Docker |
| `docker version` | Versión de Docker |

## Copia e import/export

| Comando | Descripción |
|---|---|
| `docker cp <origen> <destino>` | Copia archivos entre el host y un contenedor |
| `docker export <nombre/id> > archivo.tar` | Exporta el filesystem de un contenedor a un tar |
| `docker import archivo.tar` | Crea una imagen a partir de un tar exportado |
| `docker commit <nombre/id> <nueva_imagen>` | Crea una imagen a partir de los cambios de un contenedor |

## Redes

| Comando | Descripción |
|---|---|
| `docker network ls` | Lista las redes |
| `docker network create <nombre>` | Crea una red |
| `docker network connect <red> <contenedor>` | Conecta un contenedor a una red |
| `docker network disconnect <red> <contenedor>` | Desconecta un contenedor de una red |
| `docker network inspect <red>` | Detalles de una red |
| `docker network rm <red>` | Elimina una red |

## Volúmenes

| Comando | Descripción |
|---|---|
| `docker volume create <nombre>` | Crea un volumen |
| `docker volume ls` | Lista los volúmenes |
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

## Docker Compose

| Comando | Descripción |
|---|---|
| `docker compose up -d` | Construye/crea/inicia todos los servicios en segundo plano |
| `docker compose down` | Detiene y elimina contenedores, redes y volúmenes del proyecto |
| `docker compose logs -f` | Logs unificados en tiempo real de todos los servicios |


## Referencia

https://docs.docker.com/get-started/docker_cheatsheet.pdf
