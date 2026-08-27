# API CRUD de Artistas y Eventos 🎵🎤

API REST desarrollada con **Django** y **Django REST Framework** para gestionar información de artistas y sus eventos mediante operaciones CRUD.

El proyecto permite **crear, consultar, modificar y eliminar artistas y eventos** utilizando diferentes métodos HTTP. Además, implementa una relación entre ambos modelos: un artista puede tener varios eventos y cada evento pertenece a un artista.

La API puede ser probada mediante herramientas como **Thunder Client**.

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

# 🎉 Modelo Evento

El proyecto también utiliza un modelo llamado `Evento`, que permite registrar eventos asociados a un artista.

Cada evento pertenece a un artista, mientras que un artista puede tener uno o varios eventos.

| Campo         | Tipo       | Descripción                                  |
| ------------- | ---------- | -------------------------------------------- |
| `id`          | Integer    | Identificador único generado automáticamente |
| `nombre`      | String     | Nombre del evento                            |
| `tipo`        | String     | Tipo de evento                               |
| `fecha`       | Date       | Fecha en la que se realiza el evento         |
| `lugar`       | String     | Lugar donde se realiza                       |
| `descripcion` | Text       | Descripción del evento                       |
| `activo`      | Boolean    | Indica si el evento está activo              |
| `artista`     | ForeignKey | Artista responsable o asociado al evento     |

### Ejemplo de modelo

```python
class Evento(models.Model):
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50)
    fecha = models.DateField()
    lugar = models.CharField(max_length=100)
    descripcion = models.TextField()
    activo = models.BooleanField(default=True)

    artista = models.ForeignKey(
        Artista,
        on_delete=models.CASCADE,
        related_name="eventos"
    )

    def __str__(self):
        return self.nombre
```

---

# 🔗 Relación entre Artista y Evento

La API implementa una relación **uno a muchos** mediante `ForeignKey`.

```text
Artista
   │
   ├── Evento 1
   ├── Evento 2
   └── Evento 3
```

Esto significa que:

* Un **artista puede tener varios eventos**.
* Cada **evento pertenece a un solo artista**.
* Al consultar un artista, se pueden visualizar sus eventos relacionados.
* Al consultar un evento, se puede visualizar el artista asociado.

La relación se realiza mediante:

```python
artista = models.ForeignKey(
    Artista,
    on_delete=models.CASCADE,
    related_name="eventos"
)
```

El parámetro:

```python
related_name="eventos"
```

permite acceder a los eventos de un artista.

Por ejemplo:

```python
artista.eventos.all()
```

Además, al utilizar:

```python
on_delete=models.CASCADE
```

si un artista es eliminado, también se eliminarán sus eventos relacionados.

---

# 🌐 URL base

Para realizar las pruebas de forma local se utiliza:

```text
http://127.0.0.1:8000/
```

Los endpoints principales de la API son:

```text
http://127.0.0.1:8000/api/artistas/
```

```text
http://127.0.0.1:8000/api/eventos/
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

### Artistas

| Método   | Endpoint              | Función                       |
| -------- | --------------------- | ----------------------------- |
| `GET`    | `/api/artistas/`      | Obtener todos los artistas    |
| `POST`   | `/api/artistas/`      | Crear un nuevo artista        |
| `GET`    | `/api/artistas/<id>/` | Obtener un artista específico |
| `PUT`    | `/api/artistas/<id>/` | Modificar un artista          |
| `DELETE` | `/api/artistas/<id>/` | Eliminar un artista           |

### Eventos

| Método   | Endpoint             | Función                      |
| -------- | -------------------- | ---------------------------- |
| `GET`    | `/api/eventos/`      | Obtener todos los eventos    |
| `POST`   | `/api/eventos/`      | Crear un nuevo evento        |
| `GET`    | `/api/eventos/<id>/` | Obtener un evento específico |
| `PUT`    | `/api/eventos/<id>/` | Modificar un evento          |
| `DELETE` | `/api/eventos/<id>/` | Eliminar un evento           |

---

# 📖 CRUD de Artistas

## GET - Obtener todos los artistas

Permite obtener la lista completa de artistas registrados junto con sus eventos relacionados.

### Request

```text
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
        "activo": true,
        "eventos": [
            {
                "id": 1,
                "nombre": "Festival Córdoba",
                "tipo": "Festival",
                "fecha": "2026-09-15",
                "lugar": "Plaza España",
                "descripcion": "Festival de música.",
                "activo": true
            }
        ]
    }
]
```

### Código HTTP

```text
200 OK
```

---

## GET - Obtener un artista específico

Permite obtener la información de un único artista utilizando su `id`.

### Request

```text
GET /api/artistas/1/
```

URL completa:

```text
http://127.0.0.1:8000/api/artistas/1/
```

La respuesta también incluirá los eventos relacionados con ese artista.

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

## ➕ POST - Crear un artista

Permite agregar un nuevo artista a la base de datos.

### Request

```text
POST /api/artistas/
```

En Thunder Client se debe seleccionar:

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
    "descripcion": "Rapero y cantante argentino.",
    "activo": true
}
```

### Código HTTP

```text
201 Created
```

---

## ✏️ PUT - Modificar un artista

Permite actualizar la información de un artista existente.

### Request

```text
PUT /api/artistas/1/
```

En Thunder Client:

```text
Body → JSON
```

### Código HTTP

```text
200 OK
```

---

## 🗑️ DELETE - Eliminar un artista

Permite eliminar un artista de la base de datos.

### Request

```text
DELETE /api/artistas/1/
```

No es necesario enviar un Body.

### Código HTTP

```text
204 No Content
```

> Debido a la configuración `on_delete=models.CASCADE`, al eliminar un artista también se eliminarán los eventos asociados a ese artista.

---

# 🎉 CRUD de Eventos

## 📖 GET - Obtener todos los eventos

Permite obtener la lista completa de eventos registrados.

Cada evento muestra la información básica del artista relacionado.

### Request

```text
GET /api/eventos/
```

URL completa:

```text
http://127.0.0.1:8000/api/eventos/
```

### Ejemplo de respuesta

```json
[
    {
        "id": 1,
        "nombre": "Festival Córdoba",
        "tipo": "Festival",
        "fecha": "2026-09-15",
        "lugar": "Plaza España",
        "descripcion": "Festival de música.",
        "activo": true,
        "artista": {
            "id": 1,
            "nombre_artistico": "Duki"
        }
    }
]
```

### Código HTTP

```text
200 OK
```

---

## 🔎 GET - Obtener un evento específico

Permite obtener la información de un único evento utilizando su `id`.

### Request

```text
GET /api/eventos/1/
```

URL completa:

```text
http://127.0.0.1:8000/api/eventos/1/
```

### Ejemplo de respuesta

```json
{
    "id": 1,
    "nombre": "Festival Córdoba",
    "tipo": "Festival",
    "fecha": "2026-09-15",
    "lugar": "Plaza España",
    "descripcion": "Festival de música.",
    "activo": true,
    "artista": {
        "id": 1,
        "nombre_artistico": "Duki"
    }
}
```

### Código HTTP

```text
200 OK
```

Si el evento no existe:

```text
404 Not Found
```

Respuesta:

```json
{
    "error": "Evento no encontrado"
}
```

---

## ➕ POST - Crear un evento

Permite agregar un nuevo evento a la base de datos y asociarlo a un artista existente.

### Request

```text
POST /api/eventos/
```

URL completa:

```text
http://127.0.0.1:8000/api/eventos/
```

En Thunder Client se debe seleccionar:

```text
Body → JSON
```

### Ejemplo

```json
{
    "nombre": "Festival Córdoba",
    "tipo": "Festival",
    "fecha": "2026-09-15",
    "lugar": "Plaza España",
    "descripcion": "Festival de música.",
    "activo": true,
    "artista": 1
}
```

El valor:

```json
"artista": 1
```

corresponde al `id` del artista que será asociado al evento.

### Ejemplo de respuesta

Luego de crear el evento, la API devuelve el evento junto con la información del artista relacionado:

```json
{
    "id": 1,
    "nombre": "Festival Córdoba",
    "tipo": "Festival",
    "fecha": "2026-09-15",
    "lugar": "Plaza España",
    "descripcion": "Festival de música.",
    "activo": true,
    "artista": {
        "id": 1,
        "nombre_artistico": "Duki"
    }
}
```

### Código HTTP

```text
201 Created
```

---

## ✏️ PUT - Modificar un evento

Permite actualizar la información de un evento existente.

También es posible cambiar el artista asociado al evento enviando otro `id`.

### Request

```text
PUT /api/eventos/1/
```

En Thunder Client:

```text
Body → JSON
```

### Ejemplo

```json
{
    "nombre": "Festival Córdoba 2026",
    "tipo": "Festival",
    "fecha": "2026-10-20",
    "lugar": "Córdoba",
    "descripcion": "Festival actualizado.",
    "activo": true,
    "artista": 1
}
```

### Código HTTP

```text
200 OK
```

---

## 🗑️ DELETE - Eliminar un evento

Permite eliminar un evento específico.

### Request

```text
DELETE /api/eventos/1/
```

URL completa:

```text
http://127.0.0.1:8000/api/eventos/1/
```

No es necesario enviar un Body.

### Código HTTP

```text
204 No Content
```

Una vez realizada la operación, el evento queda eliminado de la base de datos.

---

# ⚠️ Códigos de respuesta HTTP

La API utiliza diferentes códigos HTTP para indicar el resultado de cada operación.

| Código                   | Significado                                                      |
| ------------------------ | ---------------------------------------------------------------- |
| `200 OK`                 | La solicitud se realizó correctamente                            |
| `201 Created`            | Se creó correctamente un nuevo recurso                           |
| `204 No Content`         | La operación se realizó correctamente sin contenido de respuesta |
| `400 Bad Request`        | Los datos enviados no son válidos                                |
| `404 Not Found`          | El artista o evento solicitado no existe                         |
| `405 Method Not Allowed` | El método HTTP utilizado no está permitido para ese endpoint     |

---

# 🧪 Pruebas con Thunder Client

Para probar la API se utilizó **Thunder Client**, una extensión de Visual Studio Code que permite realizar solicitudes HTTP.

## Artistas

```text
GET
http://127.0.0.1:8000/api/artistas/
```

```text
POST
http://127.0.0.1:8000/api/artistas/
```

```text
GET
http://127.0.0.1:8000/api/artistas/1/
```

```text
PUT
http://127.0.0.1:8000/api/artistas/1/
```

```text
DELETE
http://127.0.0.1:8000/api/artistas/1/
```

## Eventos

```text
GET
http://127.0.0.1:8000/api/eventos/
```

```text
POST
http://127.0.0.1:8000/api/eventos/
```

```text
GET
http://127.0.0.1:8000/api/eventos/1/
```

```text
PUT
http://127.0.0.1:8000/api/eventos/1/
```

```text
DELETE
http://127.0.0.1:8000/api/eventos/1/
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

Las APIs estarán disponibles en:

```text
http://127.0.0.1:8000/api/artistas/
```

y:

```text
http://127.0.0.1:8000/api/eventos/
```

---

# 🗄️ Base de datos y migraciones

El proyecto utiliza **SQLite** como sistema de base de datos.

Django se encarga de crear y administrar las tablas correspondientes a los modelos `Artista` y `Evento` mediante el sistema de migraciones.

Cada vez que se realizan cambios en los modelos, se deben crear y aplicar las migraciones.

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

La API permite administrar **artistas y eventos** mediante operaciones CRUD:

```text
CREATE  → POST
READ    → GET
UPDATE  → PUT
DELETE  → DELETE
```

## Principales endpoints

### Artistas

```text
GET     /api/artistas/
POST    /api/artistas/
GET     /api/artistas/<id>/
PUT     /api/artistas/<id>/
DELETE  /api/artistas/<id>/
```

### Eventos

```text
GET     /api/eventos/
POST    /api/eventos/
GET     /api/eventos/<id>/
PUT     /api/eventos/<id>/
DELETE  /api/eventos/<id>/
```

La API fue desarrollada utilizando **Django + Django REST Framework**, implementando una estructura REST capaz de gestionar artistas y eventos relacionados entre sí mediante una relación **uno a muchos**.
