## 1. Exploración Interna de Contenedores

Explorar la estructura interna de una imagen o contenedor es clave para verificar dependencias, rutas y configuraciones antes de desplegar en producción.

Por defecto, cada imagen define un proceso de arranque (mediante `ENTRYPOINT` o `CMD`), como `nginx -g 'daemon off;'` o `mysqld`. Es posible sobrescribir ese comportamiento inicial ejecutando una shell interactiva:

```bash
docker run --rm -it nginx bash
```

### Desglose de Parámetros:
* `docker run`: Crea y arranca un contenedor nuevo a partir de la imagen especificada.
* `-i` (`--interactive`): Mantiene abierto el flujo `STDIN`, permitiendo interactuar mediante el teclado.
* `-t` (`--tty`): Asigna una pseudo-terminal (formato visual de consola, prompt y colores).
* `--rm`: Destruye y libera el contenedor automáticamente al salir, evitando acumular contenedores en estado `Exited`.
* `bash`: Comando/binario que sustituye el `CMD` predeterminado por una terminal interactiva.

> **Nota sobre Alpine Linux:** Las variantes minimalistas como `nginx:alpine` no incluyen `bash` instalado de fábrica. En esos casos debe usarse `/bin/sh` o `ash`:
> ```bash
> docker run --rm -it nginx:alpine sh
> ```

---

## 2. Diferencias entre pasar un comando al final y usar `--entrypoint`

La diferencia radica en qué directiva interna del `Dockerfile` se está sobrescribiendo:
* Pasar un argumento al final de `docker run` modifica únicamente **`CMD`**.
* La bandera `--entrypoint` sustituye la instrucción **`ENTRYPOINT`**.

### La Fórmula de Ejecución de Docker

$$\text{Proceso final} = \text{ENTRYPOINT} + \text{CMD}$$

* **`ENTRYPOINT`**: Binario base o ejecutable inmutable (ej. `python3`, `nginx`, `/entrypoint.sh`).
* **`CMD`**: Argumentos o subcomandos por defecto entregados al ejecutable base (ej. `app.py`, `daemon off;`).

---

### Caso 1: Pasar el comando al final (Sobrescribe solo `CMD`)

Si una imagen define:
```dockerfile
ENTRYPOINT ["python3"]
CMD ["main.py"]
```

Al ejecutar:
```bash
docker run -it --rm mi-imagen-python bash
```

Docker no abrirá una terminal; ejecutará la concatenación:
```bash
python3 bash
```
**Resultado:** Fallo inmediato (`python3: can't open file 'bash': [Errno 2] No such file or directory`).

---

### Caso 2: Usar `--entrypoint` (Sobrescribe el binario base)

Para suplantar el binario raíz y abrir una terminal:
```bash
docker run --rm -it --entrypoint bash mi-imagen-python
```

Cualquier argumento adicional tras el nombre de la imagen se entregará a la nueva shell:
```bash
docker run --rm -it --entrypoint /bin/sh mi-imagen -c "ls -la /app"
```

### Tabla Resumen: CLI vs. `--entrypoint`

| Aspecto | Argumento al final de `docker run` | Con `--entrypoint <binario>` |
| :--- | :--- | :--- |
| **Directiva que sustituye** | `CMD` | `ENTRYPOINT` |
| **Propósito** | Modificar flags o argumentos del programa. | Cambiar el binario raíz o desbloquear shells. |
| **Comportamiento si existe `ENTRYPOINT`** | Pasa el texto como parámetro al binario existente. | Anula el binario original y ejecuta el nuevo. |
| **Sintaxis** | `docker run [flags] <imagen> <comando>` | `docker run [flags] --entrypoint <binario> <imagen> [args]` |

---

## 3. Exec Form vs. Shell Form en el Dockerfile

Tanto `ENTRYPOINT` como `CMD` admiten dos tipos de notación, con consecuencias directas sobre el proceso raíz (**PID 1**), las variables de entorno y el apagado ordenado (*graceful shutdown*).

### Resumen de Notación:
* **Exec Form:** `["ejecutable", "param1", "param2"]` *(Formato JSON: corchetes y comillas dobles estrictas)*
* **Shell Form:** `ejecutable param1 param2` *(Texto plano sin corchetes)*

| Característica | Exec Form (`["binario", "arg"]`) | Shell Form (`binario arg`) |
| :--- | :--- | :--- |
| **Proceso raíz (PID 1)** | La aplicación se ejecuta directamente como PID 1. | `/bin/sh -c` es el PID 1; la aplicación es un proceso hijo. |
| **Paso de señales (`SIGTERM`, `SIGINT`)** | **Directo.** Permite cierre ordenado de conexiones y transacciones. | **Bloqueado.** La shell intermedia rara vez retransmite señales, terminando en un `SIGKILL` forzado tras 10 s. |
| **Expansión de variables (`$PORT`)** | No se evalúan nativamente (se interpretan como strings literales). | Se resuelven de forma transparente en tiempo de ejecución. |
| **Interacción `ENTRYPOINT` + `CMD`** | Totalmente compatible; se concatenan limpiamente. | Incompatible; el `ENTRYPOINT` en shell form descarta cualquier `CMD`. |
| **Uso recomendado** | Estándar recomendado para producción. | Tareas puntuales o scripts rápidos de testing. |

### Ejemplo: Evaluación de Variables en Exec Form
Para combinar la gestión de señales de Exec Form con la interpolación de variables:
```dockerfile
ENV PORT=8080
CMD ["sh", "-c", "node server.js --port $PORT"]
```

---

## 4. Comparativa de Comandos del Ciclo de Vida de Docker

### Flujo de Vida y Transición de Estados

```
[Dockerfile]
      │
      ▼  (docker build)
   [Imagen]
      │
      ▼  (docker run)
[Contenedor Activo (Up)] ────────(docker exec)───────► [Shell / Debug interno]
      │
      ▼  (docker stop)
[Contenedor Detenido (Exited)]
      │
      ▼  (docker start)
[Contenedor Activo (Up)]
```

### Tabla Comparativa Integral (CLI vs. Docker Compose)

| Comando CLI | Equivalente en Compose | Nivel / Ámbito | Entrada Principal | Salida / Efecto | Estado Requerido | Propósito |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **`docker build`** | `docker compose build` | Imagen | `Dockerfile` + Contexto | Nueva imagen local | Archivos locales | Compilar runtime, código y dependencias en una imagen inmutable. |
| **`docker run`** | `docker compose up` / `run` | Contenedor vs. Stack | Imagen + Flags de red/puertos | Nuevo contenedor / servicios en ejecución | Imagen disponible | Instanciar y arrancar desde cero (resuelve puertos, volúmenes y red). |
| **`docker start`** | `docker compose start` | Contenedor | Contenedor existente (nombre/ID) | Reactivación del proceso | Estado `Exited` | Reanudar la ejecución sin modificar parámetros ni reconstruir capas. |
| **`docker exec`** | `docker compose exec <svc> <cmd>` | Contenedor | Contenedor activo + binario | Proceso secundario interno (Shell) | Estado `Up` | Depurar, inspeccionar archivos o ejecutar comandos sin reiniciar. |
| **`docker stop`** | `docker compose stop` | Contenedor vs. Stack | Contenedor activo | Proceso detenido limpiamente (`SIGTERM`) | Estado `Up` | Detener temporalmente conservando los volúmenes y capas. |
| **`docker rm`** | `docker compose down` | Contenedor vs. Stack | Contenedor detenido (o `-f`) | Espacio y namespaces liberados | Estado `Exited` (o forzado) | Eliminar contenedores y redes coordinadas. |

---

## 5. Inspección con `docker inspect`

El comando `docker inspect` devuelve información técnica de bajo nivel de contenedores o imágenes en formato JSON estructurado:

```bash
docker inspect <nombre_o_id_contenedor>
```

### Información Clave que Ofrece:
* **Estado y ciclo de vida (`State`):** Código de salida (`ExitCode`), PID del proceso en el host y timestamps de inicio/fin.
* **Redes y puertos (`NetworkSettings`):** IP interna asignada, mapeo de puertos hacia el host y gateway de la red bridge.
* **Almacenamiento (`Mounts`):** Volúmenes, bind mounts locales y permisos de lectura/escritura (`rw`).
* **Configuración de inicio (`Config`):** Variables de entorno activas, directivas `Cmd`, `Entrypoint` y directorio de trabajo (`WorkingDir`).

### Filtros Comunes con `--format`:
```bash
# Obtener la IP interna del contenedor
docker inspect --format='{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' web-example

# Ver el Entrypoint y CMD configurados
docker inspect --format='{{json .Config.Entrypoint}}' web-example
docker inspect --format='{{json .Config.Cmd}}' web-example
```