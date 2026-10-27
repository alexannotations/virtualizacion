# Guía Conceptual: Anatomía de un `Dockerfile`

Un archivo `Dockerfile` es una receta de construcción declarativa que define paso a paso cómo crear una imagen personalizada de Docker. Cada instrucción genera una capa (*layer*) en la imagen final.

---

## Ejemplo Estructurado: Nginx Web Server

```dockerfile
# 1. IMAGEN BASE
# Define el sistema operativo o runtime inicial (formato: imagen:etiqueta)
FROM nginx:latest

# 2. DIRECTORIO DE TRABAJO
# Establece la ruta interna del contenedor donde se ejecutarán las instrucciones siguientes
WORKDIR /usr/share/nginx/html

# 3. EJECUCIÓN DE COMANDOS DURANTE LA CONSTRUCCIÓN (BUILD TIME)
# Útil para compilar código, instalar paquetes o diagnósticos
RUN uname -a

# 4. COPIAR ARCHIVOS ESPECÍFICOS O DE CONFIGURACIÓN
# COPY <origen_en_host> <destino_en_contenedor>
COPY comandos.md .

# 5. COPIAR ARCHIVOS DE LA APLICACIÓN
# Copia el resto del código hacia el WORKDIR actual (.)
COPY . .

# 6. DOCUMENTACIÓN DE PUERTOS
# Comunica qué puerto escucha el proceso interno (meramente informativo)
EXPOSE 80

# 7. DECLARACIÓN DE VOLUMEN INTERNO
# Avisa a Docker que esta ruta interna persistirá datos administrados
# Declara un punto de montaje en el Dockerfile
# Solo se indica la ruta interna del contenedor.
VOLUME ["/usr/share/nginx/html"]

# 8. COMANDO DE ENTRADA (OPCIONAL EN NGINX)
# Nginx ya incluye su comando por defecto en la imagen base:
# CMD ["nginx", "-g", "daemon off;"]
```

---

## Conceptos e Instrucciones

### 1. `FROM`
* **Propósito:** Especifica la imagen base sobre la cual se construye la nueva imagen.
* **Buenas prácticas:** Usa versiones fijas o versiones ligeras en producción (ej. `nginx:1.27-alpine`) en lugar de `latest`, para garantizar reproducibilidad.

### 2. `WORKDIR`
* **Propósito:** Define el directorio de trabajo actual dentro del contenedor.
* **Comportamiento:** Si el directorio no existe, Docker lo crea automáticamente. Todas las instrucciones posteriores (`RUN`, `COPY`, `CMD`) se ejecutarán relativas a esta ruta.

### 3. `COPY` y Estrategia de Caché
* **Sintaxis:** `COPY <origen_host> <destino_contenedor>`
* **Caché de capas:** Docker evalúa si los archivos copiados han cambiado. Si no hay cambios, reutiliza la capa guardada en caché.
* **Regla de oro:** Copia primero los archivos de dependencias o configuración que rara vez cambian (por ejemplo, `package.json`, configuraciones `.conf`) y al final el código fuente (`COPY . .`). Así evitas invalidar la caché en cada compilación.

### 4. `RUN` vs `CMD` vs `ENTRYPOINT`
Es común confundir estas tres directivas:

| Directiva | Cuándo se ejecuta | Propósito principal | Ejemplo común |
| :--- | :--- | :--- | :--- |
| **`RUN`** | Durante el **Build** (creación de imagen) | Modifica la imagen: instala paquetes, compila binarios, crea carpetas. | `RUN apt-get update && apt-get install -y curl` |
| **`CMD`** | Durante el **Run** (inicio del contenedor) | Proporciona el comando o argumentos por defecto al arrancar. Fácil de sobreescribir al hacer `docker run`. | `CMD ["nginx", "-g", "daemon off;"]` |
| **`ENTRYPOINT`** | Durante el **Run** (inicio del contenedor) | Define el ejecutable principal inmutable del contenedor. Los argumentos de `CMD` pasan como parámetros de `ENTRYPOINT`. | `ENTRYPOINT ["docker-entrypoint.sh"]` |

> **Nota sobre Nginx:** La imagen oficial `nginx` ya define internamente su propio `CMD ["nginx", "-g", "daemon off;"]`. No es necesario volver a escribirlo a menos que necesites parámetros especiales.

### 5. `EXPOSE`
* **Propósito:** Documenta qué puertos de red escucha el contenedor al ejecutarse.
* **Importante:** **No abre ni publica el puerto hacia la máquina anfitriona**. Solo **documenta** dentro del contenedor en qué puerto está escuchando el proceso y permite que otros contenedores en la misma red privada de Docker le hablen directamente. Para acceder desde tu máquina local sigues necesitando el flag `-p` en ejecución (ejemplo: `-p 8080:80`).

---

## Volúmenes: `VOLUME` vs `Bind Mounts`

Un punto clave de confusión al escribir un `Dockerfile`:

### En el `Dockerfile` (`VOLUME`):
* Solo acepta rutas **internas** del contenedor:
  ```dockerfile
  VOLUME ["/usr/share/nginx/html"]
  ```
* Indica a Docker que cree un **volumen anónimo administrado** si no se especifica otro al arrancar. Declara un punto de montaje en el _Dockerfile_.
* **Nunca uses `$(pwd)` ni rutas del host dentro de `VOLUME`**; Dockerfiles deben ser universales y no conocen el sistema de archivos de tu máquina anfitriona.

### En Tiempo de Ejecución (*Bind Mounts*):
* Los montajes en vivo de tu máquina local al contenedor se configuran **al ejecutar**, no al compilar:
  * **Vía Docker CLI:**
    ```bash
    docker run -d -p 8080:80 -v $(pwd):/usr/share/nginx/html nginx
    ```
  * **Vía Docker Compose (`compose.yaml`):**
    ```yaml
    services:
      web:
        image: nginx:alpine
        ports:
          - "8080:80"
        volumes:
          - .:/usr/share/nginx/html
    ```

