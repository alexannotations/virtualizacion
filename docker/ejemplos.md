# Ejemplos

| Comando | Descripción |
|---|---|
| `docker create -p 27017:27017 --name mongo-db-test -e MONGO_INITDB_ROOT_USERNAME=my_name -e MONGO_INITDB_ROOT_PASSWORD=password mongo` | Descarga la imagen (si no existe localmente) a partir de la imagen de *mongo:latest* y crea la capa de escritura del contenedor, pero no lo inicia. Devuelve el ID del contenedor creado. Lo nombra *mongo-db-test* , publica/mapea el puerto 27017 del host hacia el puerto 27017 interno del contenedor. Define la variable de entorno para el usuario y la contraseña para el administrador/root inicial. Detener el contenedor `docker stop` o reiniciar el servidor no borra los datos; la pérdida ocurre exclusivamente si borras el contenedor `docker rm`. |
| `docker run -it -d -p 127.0.0.1:8090:80 --name web-test nginx` | Este comando arranca un contenedor Nginx con una capa adicional de seguridad en la red (asigna una IP especifica). Con `-p 127.0.0.1:8080:80`: El puerto queda cerrado al exterior. Solo los procesos que corren dentro de tu propio equipo (localhost) pueden conectarse. Es la mejor práctica para entornos de desarrollo seguro. |
| `docker login .` | Inicia sesion en docker hub |
| `docker build -t <user_name>/<nombre_imagen>:<tag> .` | Etiquetar imagen correctamente |
| `docker push <user_name>/<nombre_imagen>:<tag>` | Subir la imagen al repositorio |
| `docker run <user_name>/<nombre_imagen>:<tag>` | Descargar imagen de dockerhub |

