# Ejemplos

| Comando | Descripción |
|---|---|
| `docker create -p 27017:27017 --name mongo-db-test -e MONGO_INITDB_ROOT_USERNAME=my_name -e MONGO_INITDB_ROOT_PASSWORD=password mongo` | Descarga la imagen (si no existe localmente) a partir de la imagen de *mongo:latest* y crea la capa de escritura del contenedor, pero no lo inicia. Devuelve el ID del contenedor creado. Lo nombra *mongo-db-test* , publica/mapea el puerto 27017 del host hacia el puerto 27017 interno del contenedor. Define la variable de entorno para el usuario y la contraseña para el administrador/root inicial. Detener el contenedor `docker stop` o reiniciar el servidor no borra los datos; la pérdida ocurre exclusivamente si borras el contenedor `docker rm`. |




