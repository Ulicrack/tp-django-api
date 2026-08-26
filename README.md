# API CRUD de Artistas 🎵

API REST desarrollada con **Django** y **Django REST Framework** para gestionar información de artistas mediante operaciones CRUD.

El proyecto permite **crear, consultar, modificar y eliminar artistas** utilizando diferentes métodos HTTP y puede ser probado mediante herramientas como **Thunder Client**.

---

## 🚀 Tecnologías utilizadas

* **Python 3**
* **Django**
* **Django REST Framework**
* **SQLite**
* **Thunder Client** para realizar pruebas de la API

---

## 📁 Estructura principal del proyecto

```text
tp_django_api/
│
├── manage.py
│
├── api/
│   ├── migrations/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
│
├── tp_django_api/
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
└── README.md
```

---

# 🎤 Modelo Artista

El proyecto utiliza un modelo llamado `Artista`, que contiene los siguientes campos:

| Campo              | Tipo    | Descripción                                  |
| ------------------ | ------- | -------------------------------------------- |
| `id`               | Integer | Identificador único generado automáticamente |
| `nombre`           | String  | Nombre real del artista                      |
| `nombre_artistico` | String  | Nombre artístico                             |
| `tipo`             | String  | Tipo de artista o creador                    |
| `genero`           | String  | Género musical o categoría                   |
| `edad`             | Integer | Edad del artista                             |
| `ciudad`           | String  | Ciudad de origen                             |
| `descripcion`      | Text    | Descripción del artista                      |
| `activo`           | Boolean | Indica si el artista está activo             |

### Ejemplo de modelo

```python
class Artista(models.Model):
    nombre = models.CharField(max_length=100)
    nombre_artistico = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50)
    genero = models.CharField(max_length=50)
    edad = models.IntegerField()
    ciudad = models.CharField(max_length=100)
    descripcion = models.TextField()
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre_artistico
```

---

# 🌐 URL base

Para realizar las pruebas de forma local se utiliza:

```text
http://127.0.0.1:8000
```

La API de artistas se encuentra en:

```text
http://127.0.0.1:8000/api/artistas/
```

> **Importante:** las URLs utilizan una `/` al final.

---

# 🔄 Métodos CRUD

La API implementa las cuatro operaciones principales de un CRUD:

* **Create** → Crear
* **Read** → Leer
* **Update** → Actualizar
* **Delete** → Eliminar

## Endpoints disponibles

| Método   | Endpoint              | Función                       |
| -------- | --------------------- | ----------------------------- |
| `GET`    | `/api/artistas/`      | Obtener todos los artistas    |
| `POST`   | `/api/artistas/`      | Crear un nuevo artista        |
| `GET`    | `/api/artistas/<id>/` | Obtener un artista específico |
| `PUT`    | `/api/artistas/<id>/` | Modificar un artista          |
| `DELETE` | `/api/artistas/<id>/` | Eliminar un artista           |

---

# 📖 GET - Obtener todos los artistas

Permite obtener la lista completa de artistas registrados.

### Request

```http
GET /api/artistas/
```

URL completa:

```text
http://127.0.0.1:8000/api/artistas/
```

### Ejemplo de respuesta

```json
[
    {
        "id": 1,
        "nombre": "Mauro Ezequiel Lombardo Quiroga",
        "nombre_artistico": "Duki",
        "tipo": "Solista",
        "genero": "Trap",
        "edad": 29,
        "ciudad": "Buenos Aires",
        "descripcion": "Rapero y cantante argentino.",
        "activo": true
    }
]
```

### Código HTTP

```text
200 OK
```

---

# 🔎 GET - Obtener un artista específico

Permite obtener la información de un único artista utilizando su `id`.

### Request

```http
GET /api/artistas/1/
```

URL completa:

```text
http://127.0.0.1:8000/api/artistas/1/
```

### Ejemplo de respuesta

```json
{
    "id": 1,
    "nombre": "Mauro Ezequiel Lombardo Quiroga",
    "nombre_artistico": "Duki",
    "tipo": "Solista",
    "genero": "Trap",
    "edad": 29,
    "ciudad": "Buenos Aires",
    "descripcion": "Rapero y cantante argentino.",
    "activo": true
}
```

### Código HTTP

```text
200 OK
```

Si el artista no existe:

```text
404 Not Found
```

Respuesta:

```json
{
    "error": "Artista no encontrado"
}
```

---

# ➕ POST - Crear un artista

Permite agregar un nuevo artista a la base de datos.

### Request

```http
POST /api/artistas/
```

URL completa:

```text
http://127.0.0.1:8000/api/artistas/
```

En Thunder Client se debe seleccionar:

```text
Body → JSON
```

### Ejemplo: Duki

```json
{
    "nombre": "Mauro Ezequiel Lombardo Quiroga",
    "nombre_artistico": "Duki",
    "tipo": "Solista",
    "genero": "Trap",
    "edad": 29,
    "ciudad": "Buenos Aires",
    "descripcion": "Rapero y cantante argentino.",
    "activo": true
}
```

### Ejemplo: Spreen

```json
{
    "nombre": "Iván Raúl Buhajeruk",
    "nombre_artistico": "Spreen",
    "tipo": "Streamer",
    "genero": "Contenido digital",
    "edad": 25,
    "ciudad": "Santa Fe",
    "descripcion": "Streamer y creador de contenido argentino.",
    "activo": true
}
```

### Ejemplo: Luck Ra

```json
{
    "nombre": "Juan Facundo Almenara Ordóñez",
    "nombre_artistico": "Luck Ra",
    "tipo": "Solista",
    "genero": "Cuarteto",
    "edad": 27,
    "ciudad": "Córdoba",
    "descripcion": "Cantante y compositor argentino.",
    "activo": true
}
```

### Ejemplo de respuesta

```json
{
    "id": 1,
    "nombre": "Mauro Ezequiel Lombardo Quiroga",
    "nombre_artistico": "Duki",
    "tipo": "Solista",
    "genero": "Trap",
    "edad": 29,
    "ciudad": "Buenos Aires",
    "descripcion": "Rapero y cantante argentino.",
    "activo": true
}
```

### Código HTTP

```text
201 Created
```

---

# ✏️ PUT - Modificar un artista

Permite actualizar la información de un artista existente.

### Request

```http
PUT /api/artistas/1/
```

URL completa:

```text
http://127.0.0.1:8000/api/artistas/1/
```

En Thunder Client:

```text
Body → JSON
```

### Ejemplo

```json
{
    "nombre": "Mauro Ezequiel Lombardo Quiroga",
    "nombre_artistico": "Duki",
    "tipo": "Solista",
    "genero": "Trap",
    "edad": 29,
    "ciudad": "Buenos Aires",
    "descripcion": "Rapero y cantante argentino reconocido por su trayectoria dentro de la escena urbana.",
    "activo": true
}
```

### Ejemplo de respuesta

```json
{
    "id": 1,
    "nombre": "Mauro Ezequiel Lombardo Quiroga",
    "nombre_artistico": "Duki",
    "tipo": "Solista",
    "genero": "Trap",
    "edad": 29,
    "ciudad": "Buenos Aires",
    "descripcion": "Rapero y cantante argentino reconocido por su trayectoria dentro de la escena urbana.",
    "activo": true
}
```

### Código HTTP

```text
200 OK
```

Si el artista no existe:

```text
404 Not Found
```

---

# 🗑️ DELETE - Eliminar un artista

Permite eliminar un artista de la base de datos.

### Request

```http
DELETE /api/artistas/1/
```

URL completa:

```text
http://127.0.0.1:8000/api/artistas/1/
```

No es necesario enviar un Body.

### Código HTTP

```text
204 No Content
```

Una vez realizada la operación, el artista queda eliminado de la base de datos.

---

# ⚠️ Códigos de respuesta HTTP

La API utiliza diferentes códigos HTTP para indicar el resultado de cada operación.

| Código                   | Significado                                                      |
| ------------------------ | ---------------------------------------------------------------- |
| `200 OK`                 | La solicitud se realizó correctamente                            |
| `201 Created`            | Se creó correctamente un nuevo recurso                           |
| `204 No Content`         | La operación se realizó correctamente sin contenido de respuesta |
| `400 Bad Request`        | Los datos enviados no son válidos                                |
| `404 Not Found`          | El artista solicitado no existe                                  |
| `405 Method Not Allowed` | El método HTTP utilizado no está permitido para ese endpoint     |

---

# 🧪 Pruebas con Thunder Client

Para probar la API se utilizó **Thunder Client**, una extensión de Visual Studio Code que permite realizar solicitudes HTTP.

Ejemplos de solicitudes:

### Listar artistas

```text
GET
http://127.0.0.1:8000/api/artistas/
```

### Crear artista

```text
POST
http://127.0.0.1:8000/api/artistas/
```

### Obtener un artista

```text
GET
http://127.0.0.1:8000/api/artistas/1/
```

### Modificar un artista

```text
PUT
http://127.0.0.1:8000/api/artistas/1/
```

### Eliminar un artista

```text
DELETE
http://127.0.0.1:8000/api/artistas/1/
```

---

# ▶️ Ejecución del proyecto

Para ejecutar el proyecto localmente, primero se debe activar el entorno virtual.

En Linux:

```bash
source .venv/bin/activate
```

Luego se inicia el servidor de Django:

```bash
python manage.py runserver
```

El servidor estará disponible en:

```text
http://127.0.0.1:8000/
```

La API estará disponible en:

```text
http://127.0.0.1:8000/api/artistas/
```

---

# 🗄️ Base de datos

El proyecto utiliza **SQLite** como sistema de base de datos.

Django se encarga de crear y administrar la tabla correspondiente al modelo `Artista` mediante el sistema de migraciones.

Para crear las migraciones:

```bash
python manage.py makemigrations
```

Para aplicarlas:

```bash
python manage.py migrate
```

---

# 📌 Resumen

La API permite administrar artistas mediante operaciones CRUD:

```text
CREATE  → POST
READ    → GET
UPDATE  → PUT
DELETE  → DELETE
```

Los principales endpoints son:

```text
GET     /api/artistas/
POST    /api/artistas/
GET     /api/artistas/<id>/
PUT     /api/artistas/<id>/
DELETE  /api/artistas/<id>/
```

El proyecto fue desarrollado utilizando **Django + Django REST Framework**, implementando una API REST capaz de gestionar los datos de artistas de manera estructurada.