# 🎫 Ticket Management API

API REST completa para gestión de tickets y usuarios siguiendo principios de **Clean Architecture**.

## 📋 Tabla de Contenidos

- [Características](#características)
- [Arquitectura](#arquitectura)
- [Stack Tecnológico](#stack-tecnológico)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Instalación y Ejecución](#instalación-y-ejecución)
- [API Endpoints](#api-endpoints)
- [Testing](#testing)
- [Migraciones de Base de Datos](#migraciones-de-base-de-datos)
- [Variables de Entorno](#variables-de-entorno)

## ✨ Características

- ✅ API CRUD completa para Users y Tickets
- ✅ Clean Architecture con separación de capas
- ✅ Validación de datos con Pydantic V2
- ✅ Base de datos PostgreSQL con SQLAlchemy 2.0
- ✅ Migraciones con Alembic
- ✅ Documentación automática con OpenAPI/Swagger
- ✅ Tests de integración con pytest
- ✅ Dockerización con multi-stage build
- ✅ Docker Compose con PostgreSQL
- ✅ Type hints completos (PEP8)

## 🏗️ Arquitectura

El proyecto sigue **Clean Architecture** con las siguientes capas:

```
┌─────────────────────────────────────┐
│         Routers (API Layer)         │  ← FastAPI Endpoints
├─────────────────────────────────────┤
│        Services (Business Logic)    │  ← Lógica de negocio
├─────────────────────────────────────┤
│     Repositories (Data Access)      │  ← Acceso a datos
├─────────────────────────────────────┤
│         Models (Database)           │  ← SQLAlchemy Models
└─────────────────────────────────────┘
```

## 🛠️ Stack Tecnológico

- **Runtime**: Python 3.11
- **Framework**: FastAPI 0.109.0
- **ORM**: SQLAlchemy 2.0.25
- **Validación**: Pydantic V2
- **Base de datos**: PostgreSQL 15 / SQLite (desarrollo)
- **Migraciones**: Alembic 1.13.1
- **Testing**: pytest 7.4.4 + httpx
- **Servidor**: Uvicorn
- **Contenedores**: Docker + Docker Compose

## 📁 Estructura del Proyecto

```
P3/javier_martin/
├── app/
│   ├── __init__.py
│   ├── main.py              # Aplicación FastAPI principal
│   ├── config.py            # Configuración de la aplicación
│   ├── database.py          # Configuración de SQLAlchemy
│   ├── models/              # Modelos de base de datos
│   │   ├── __init__.py
│   │   ├── user.py
│   │   └── ticket.py
│   ├── schemas/             # Esquemas Pydantic
│   │   ├── __init__.py
│   │   ├── user.py
│   │   └── ticket.py
│   ├── repositories/        # Capa de acceso a datos
│   │   ├── __init__.py
│   │   ├── user_repository.py
│   │   └── ticket_repository.py
│   ├── services/            # Lógica de negocio
│   │   ├── __init__.py
│   │   ├── user_service.py
│   │   └── ticket_service.py
│   └── routers/             # Endpoints de la API
│       ├── __init__.py
│       ├── users.py
│       └── tickets.py
├── tests/                   # Suite de tests
│   ├── __init__.py
│   ├── conftest.py
│   ├── test_users.py
│   └── test_tickets.py
├── alembic/                 # Migraciones de base de datos
│   ├── env.py
│   ├── script.py.mako
│   └── versions/
├── .env.example             # Ejemplo de variables de entorno
├── .gitignore
├── .dockerignore
├── alembic.ini              # Configuración de Alembic
├── requirements.txt         # Dependencias de Python
├── Dockerfile               # Docker multi-stage
├── docker-compose.yml       # Orquestación de contenedores
└── README.md                # Este archivo
```

## 🚀 Instalación y Ejecución

### Opción 1: Con Docker Compose (Recomendado)

#### Paso 1: Clonar el repositorio o navegar al directorio
```bash
cd P3/javier_martin
```

#### Paso 2: Crear archivo de variables de entorno
```bash
cp .env.example .env
```

Editar `.env` si es necesario:
```env
# PostgreSQL Database
POSTGRES_USER=user
POSTGRES_PASSWORD=password
POSTGRES_DB=ticketdb
POSTGRES_PORT=5432

# API Configuration
API_PORT=8000
DEBUG=True
```

#### Paso 3: Levantar los servicios con Docker Compose
```bash
docker-compose up --build
```

Este comando:
1. Construye la imagen Docker de la API (multi-stage)
2. Levanta el contenedor de PostgreSQL
3. Espera a que PostgreSQL esté listo
4. Ejecuta las migraciones de Alembic
5. Inicia la API en modo desarrollo

#### Paso 4: Acceder a la aplicación

- **API**: http://localhost:8000
- **Documentación Swagger**: http://localhost:8000/docs
- **Documentación ReDoc**: http://localhost:8000/redoc
- **Health Check**: http://localhost:8000/health

#### Detener los servicios
```bash
docker-compose down
```

#### Detener y eliminar volúmenes (borrar datos)
```bash
docker-compose down -v
```

### Opción 2: Instalación Local (Desarrollo)

#### Requisitos previos
- Python 3.11+
- PostgreSQL 15+ (o usar SQLite para desarrollo)

#### Paso 1: Crear entorno virtual
```bash
python3.11 -m venv venv
source venv/bin/activate  # En Linux/Mac
# venv\Scripts\activate   # En Windows
```

#### Paso 2: Instalar dependencias
```bash
pip install -r requirements.txt
```

#### Paso 3: Configurar variables de entorno
```bash
cp .env.example .env
```

Para desarrollo local con SQLite, editar `.env`:
```env
DATABASE_URL=sqlite:///./tickets.db
API_HOST=0.0.0.0
API_PORT=8000
DEBUG=True
```

#### Paso 4: Ejecutar migraciones
```bash
alembic upgrade head
```

#### Paso 5: Iniciar la aplicación
```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

O usando Python directamente:
```bash
python -m app.main
```

## 📡 API Endpoints

### Users

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/users/` | Obtener todos los usuarios |
| GET | `/users/{user_id}` | Obtener usuario por ID |
| POST | `/users/` | Crear nuevo usuario |
| PUT | `/users/{user_id}` | Actualizar usuario |
| DELETE | `/users/{user_id}` | Eliminar usuario |

### Tickets

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/tickets/` | Obtener todos los tickets |
| GET | `/tickets/?author_id={id}` | Obtener tickets por autor |
| GET | `/tickets/{ticket_id}` | Obtener ticket por ID |
| POST | `/tickets/` | Crear nuevo ticket |
| PUT | `/tickets/{ticket_id}` | Actualizar ticket |
| DELETE | `/tickets/{ticket_id}` | Eliminar ticket |

### Ejemplos de uso

#### Crear un usuario
```bash
curl -X POST "http://localhost:8000/users/" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "John Doe",
    "email": "john.doe@example.com"
  }'
```

#### Crear un ticket
```bash
curl -X POST "http://localhost:8000/tickets/" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Bug en login",
    "description": "Los usuarios no pueden iniciar sesión",
    "tags": ["bug", "urgent", "login"],
    "author_id": 1
  }'
```

#### Obtener todos los tickets
```bash
curl -X GET "http://localhost:8000/tickets/"
```

#### Obtener tickets de un usuario específico
```bash
curl -X GET "http://localhost:8000/tickets/?author_id=1"
```

## 🧪 Testing

### Ejecutar todos los tests
```bash
pytest
```

### Ejecutar tests con cobertura
```bash
pytest --cov=app --cov-report=html
```

### Ejecutar tests específicos
```bash
# Tests de usuarios
pytest tests/test_users.py

# Tests de tickets
pytest tests/test_tickets.py

# Test específico
pytest tests/test_tickets.py::test_create_ticket -v
```

### Ver reporte de cobertura
```bash
pytest --cov=app --cov-report=term-missing
```

Los tests incluyen:
- ✅ Creación de usuarios y tickets
- ✅ Obtención por ID
- ✅ Actualización de entidades
- ✅ Eliminación de entidades
- ✅ Validación de errores (404, 400)
- ✅ Filtrado de tickets por autor
- ✅ Validación de emails duplicados
- ✅ Validación de autores inexistentes

## 🗄️ Migraciones de Base de Datos

### Crear una nueva migración
```bash
alembic revision --autogenerate -m "Descripción del cambio"
```

### Aplicar migraciones
```bash
# Aplicar todas las migraciones pendientes
alembic upgrade head

# Aplicar hasta una revisión específica
alembic upgrade <revision_id>
```

### Revertir migraciones
```bash
# Revertir última migración
alembic downgrade -1

# Revertir todas las migraciones
alembic downgrade base
```

### Ver historial de migraciones
```bash
alembic history

# Ver migración actual
alembic current
```

## 🔐 Variables de Entorno

| Variable | Descripción | Valor por defecto |
|----------|-------------|-------------------|
| `DATABASE_URL` | URL de conexión a la base de datos | `sqlite:///./tickets.db` |
| `API_HOST` | Host de la API | `0.0.0.0` |
| `API_PORT` | Puerto de la API | `8000` |
| `DEBUG` | Modo debug | `True` |
| `POSTGRES_USER` | Usuario de PostgreSQL | `user` |
| `POSTGRES_PASSWORD` | Contraseña de PostgreSQL | `password` |
| `POSTGRES_DB` | Nombre de la base de datos | `ticketdb` |
| `POSTGRES_PORT` | Puerto de PostgreSQL | `5432` |

## 📊 Modelos de Datos

### User
```python
{
  "id": int,              # ID único (auto-generado)
  "name": str,            # Nombre completo
  "email": str            # Email único
}
```

### Ticket
```python
{
  "id": int,              # ID único (auto-generado)
  "title": str,           # Título del ticket
  "description": str,     # Descripción detallada
  "tags": List[str],      # Lista de palabras clave
  "created_at": datetime, # Fecha de creación (auto-generada)
  "author_id": int        # ID del usuario autor
}
```

## 🐳 Docker

### Construir la imagen
```bash
docker build -t ticket-api .
```

### Ejecutar contenedor individual
```bash
docker run -p 8000:8000 \
  -e DATABASE_URL=sqlite:///./tickets.db \
  ticket-api
```

### Ver logs de Docker Compose
```bash
# Todos los servicios
docker-compose logs -f

# Solo la API
docker-compose logs -f api

# Solo PostgreSQL
docker-compose logs -f db
```

### Acceder al contenedor
```bash
# API
docker-compose exec api /bin/sh

# PostgreSQL
docker-compose exec db psql -U user -d ticketdb
```

## 📝 Estándares de Código

- ✅ **Type Hints**: Todos los parámetros y retornos están tipados
- ✅ **PEP8**: Código formateado según PEP8
- ✅ **Docstrings**: Todas las funciones y clases documentadas
- ✅ **Clean Architecture**: Separación clara de responsabilidades
- ✅ **SOLID Principles**: Código mantenible y escalable

## 🤝 Contribución

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT.

## 👤 Autor

**Javier Martín**

---

## 🎯 Próximos Pasos

- [ ] Implementar autenticación JWT
- [ ] Añadir sistema de roles y permisos
- [ ] Implementar paginación avanzada
- [ ] Añadir búsqueda full-text en tickets
- [ ] Implementar WebSockets para notificaciones en tiempo real
- [ ] Añadir exportación de tickets a PDF
- [ ] Implementar sistema de comentarios en tickets
- [ ] Añadir logging estructurado (ELK Stack)
- [ ] Implementar rate limiting
- [ ] Añadir métricas con Prometheus

---

**¡Gracias por usar Ticket Management API!** 🚀
