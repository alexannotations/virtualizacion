# Docker Nginx con Bind Mount

Levanta un servidor web Nginx en segundo plano utilizando el directorio local actual (`pwd`) _Print Working Directory_ como raíz de los archivos web servidos, mapeando el puerto `8080` del host al puerto `80` del contenedor.


```bash
docker run -it --rm -d \
  -p 8080:80 \
  -v $(pwd):/usr/share/nginx/html \
  --name web-example \
  nginx
```



| Parámetro | Significado | Función en este comando |
| :--- | :--- | :--- |
| `docker run` | Crear y arrancar | Instrucción base para crear y ejecutar un contenedor a partir de una imagen. |
| `-i` (`--interactive`) | Modo interactivo | Mantiene abierto `STDIN` aunque no esté conectado. |
| `-t` (`--tty`) | Pseudo-TTY | Asigna una terminal virtual (*Nota: combinado con `-d` suele ser redundante para Nginx, pero no genera error*). |
| `--rm` | Auto-remoción | Elimina automáticamente el contenedor del disco cuando se detiene (`docker stop web-example`). Evita acumular contenedores huérfanos. |
| `-d` (`--detach`) | Segundo plano | Ejecuta el contenedor en segundo plano (modo demonio) liberando la terminal. |
| `-p 8080:80` | Port forwarding | Mapeo de puertos en formato `host:contenedor`. Hace que el tráfico a `http://localhost:8080` llegue al puerto `80` interno de Nginx. |
| `-v $(pwd):/usr/share/nginx/html` | Bind Mount | Monta la ruta actual del host (`$(pwd)`) dentro del directorio predeterminado donde Nginx busca los archivos estáticos (`/usr/share/nginx/html`). El contenedor lee directamente la carpeta indicada por `pwd` |
| `--name web-example` | Nombre personalizado | Asigna un identificador legible (`web-example`) en lugar de un nombre aleatorio para facilitar comandos posteriores (`docker logs`, `docker stop`). |
| `nginx` | Imagen base | Imagen oficial lista para usar de Docker Hub a utilizar (por defecto etiqueta `:latest` al no especificar tag). |





## Bind Mount (`-v`)

- **Ruta Host:** `$(pwd)` expande el directorio de trabajo actual.
- **Ruta Contenedor:** `/usr/share/nginx/html` es el Document Root predeterminado de Nginx.
- **Efecto de desarrollo en vivo:** Cualquier cambio, creación o eliminación de archivos (`index.html`, CSS, JS) en tu carpeta local se refleja inmediatamente en el navegador sin reconstruir la imagen ni reiniciar el contenedor.

La sintaxis de `-v <origen>:<destino>` distingue entre dos tipos de montajes según cómo empieza el `<origen>`:

_Ruta absoluta_ (empieza por / en Linux/macOS o C:\ en Windows):
Docker sabe que es un Bind Mount hacia un directorio de tu máquina anfitriona.

_Nombre sin ruta_ (ejemplo: `-v mi_volumen:/datos`):
Docker asume que estás haciendo referencia a un Volumen Administrado de Docker (_Named Volume_) que cumple las reglas de nomenclatura de volúmenes, no a una carpeta de tu sistema de archivos.



## Comandos útiles complementarios

```bash
# Probar en el navegador o terminal
curl http://localhost:8080

# Ver logs del servidor
docker logs -f web-example

# Detener el contenedor (se eliminará solo gracias a --rm)
docker stop web-example

# Entrar a la terminal interactiva del contenedor que está en ejecución
docker exec -it web-example sh
```
