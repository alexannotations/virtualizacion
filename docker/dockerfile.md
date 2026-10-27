# Ejemplo de Archivo Dockerfile en la raíz del proyecto.

# Base de imagen: FROM <imagen_base:version>
FROM nginx:latest

# Path: Directorio de trabajo en el contenedor
WORKDIR /usr/share/nginx/html

# Copiar archivos: COPY <origen> <destino>
# Copia el archivo de configuración del paquete:
COPY comandos.md .

# ejecutar comandos, e.g. Instalar las dependencias necesarias:
RUN uname -a

# Copia los archivos de aplicación al contenedor
# Docker reutiliza la capa de npm install desde cache y el build es más rápido, cualquier cambio en el código no invalida el cache de npm install.
COPY . .

# Exponer el puerto que la aplicación usa, por ejemplo el default de nginx:
EXPOSE 80
# Nota: Nginx ya incluye por defecto el comando para iniciar el servidor
# CMD ["nginx", "-g", "daemon off;"]

# CMD no es necesario: la imagen base "nginx:latest" ya define
# su propio CMD (arranca nginx en primer plano). Si no pones
# ninguno, se usa el que trae la imagen por defecto.


# Especificar qué proceso principal debe correr el contenedor, solo puede haber un CMD en el archivo:
# Define el comando por defecto que se ejecuta cuando arrancas un contenedor con docker run, si no le pasas otro comando explícito.

# CMD ["node", "start"]

# Si el contenedor tiene ENTRYPOINT, CMD pasa a ser los argumentos por defecto de ese ENTRYPOINT, en vez de un comando independiente.
# Se puede sobreescribir al correr el contenedor
