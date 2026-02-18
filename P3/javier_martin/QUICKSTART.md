# 🚀 Guía Rápida - Ticket Management API

## ⚡ Inicio Rápido con Docker

```bash
# 1. Navegar al directorio del proyecto
cd P3/javier_martin

# 2. Copiar archivo de configuración
cp .env.example .env

# 3. Levantar todos los servicios
docker-compose up --build

# 4. Acceder a la documentación
# http://localhost:8000/docs
```

¡Listo! La API está funcionando con PostgreSQL.

---

## 📋 Comandos Esenciales

### Docker Compose

```bash
# Levantar servicios
docker-compose up --build

# Levantar en background
docker-compose up -d

# Ver logs en tiempo real
docker-compose logs -f

# Ver logs solo de la API
docker-compose logs -f api

# Detener servicios
docker-compose down

# Detener y eliminar volúmenes (borra la BD)
docker-compose down -v

# Reiniciar un servicio específico
docker-compose restart api
```

### Con Makefile

```bash
# Ver todos los comandos disponibles
make help

# Instalar dependencias localmente
make install

# Ejecutar en modo desarrollo
make run

# Ejecutar tests
make test

# Tests con cobertura
make test-cov

# Levantar con Docker
make docker-up

# Detener Docker
make docker-down

# Ver logs
make docker-logs

# Ejecutar migraciones
make migrate

# Crear nueva migración
make migration msg="descripción del cambio"

# Limpiar archivos temporales
make clean
```

### Desarrollo Local (sin Docker)

```bash
# 1. Crear entorno virtual
python3.11 -m venv venv

# 2. Activar entorno virtual
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate   # Windows

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Configurar variables de entorno
cp .env.example .env
# Editar .env con: DATABASE_URL=sqlite:///./tickets.db

# 5. Ejecutar migraciones
alembic upgrade head

# 6. Iniciar aplicación
uvicorn app.main:app --reload
```

---

## 🧪 Testing

```bash
# Ejecutar todos los tests
pytest

# Tests con detalles
pytest -v

# Tests con cobertura
pytest --cov=app --cov-report=html

# Test específico
pytest tests/test_tickets.py::test_create_ticket

# Ver reporte de cobertura
open htmlcov/index.html  # Mac
xdg-open htmlcov/index.html  # Linux
```

---

## 🗄️ Base de Datos

### Migraciones con Alembic

```bash
# Ver estado actual
alembic current

# Ver historial
alembic history

# Crear migración automática
alembic revision --autogenerate -m "descripción"

# Aplicar todas las migraciones
alembic upgrade head

# Revertir última migración
alembic downgrade -1

# Revertir todas las migraciones
alembic downgrade base
```

### Acceder a PostgreSQL

```bash
# Con Docker Compose
docker-compose exec db psql -U user -d ticketdb

# Comandos útiles de PostgreSQL:
# \dt                  - Listar tablas
# \d users             - Describir tabla users
# \d tickets           - Describir tabla tickets
# SELECT * FROM users; - Ver todos los usuarios
# \q                   - Salir
```

---

## 🌐 Endpoints de la API

### Base URL
```
http://localhost:8000
```

### Documentación
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

### Users

```bash
# Listar usuarios
curl http://localhost:8000/users/

# Obtener usuario por ID
curl http://localhost:8000/users/1

# Crear usuario
curl -X POST http://localhost:8000/users/ \
  -H "Content-Type: application/json" \
  -d '{"name": "John Doe", "email": "john@example.com"}'

# Actualizar usuario
curl -X PUT http://localhost:8000/users/1 \
  -H "Content-Type: application/json" \
  -d '{"name": "John Smith"}'

# Eliminar usuario
curl -X DELETE http://localhost:8000/users/1
```

### Tickets

```bash
# Listar tickets
curl http://localhost:8000/tickets/

# Filtrar tickets por autor
curl http://localhost:8000/tickets/?author_id=1

# Obtener ticket por ID
curl http://localhost:8000/tickets/1

# Crear ticket
curl -X POST http://localhost:8000/tickets/ \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Bug en login",
    "description": "No puedo iniciar sesión",
    "tags": ["bug", "urgent"],
    "author_id": 1
  }'

# Actualizar ticket
curl -X PUT http://localhost:8000/tickets/1 \
  -H "Content-Type: application/json" \
  -d '{"title": "Bug en login - RESUELTO"}'

# Eliminar ticket
curl -X DELETE http://localhost:8000/tickets/1
```

---

## 🏗️ Estructura del Proyecto

```
P3/javier_martin/
├── app/                      # Código de la aplicación
│   ├── models/              # Modelos de base de datos (SQLAlchemy)
│   ├── schemas/             # Esquemas Pydantic (validación)
│   ├── repositories/        # Capa de acceso a datos
│   ├── services/            # Lógica de negocio
│   ├── routers/             # Endpoints de la API
│   ├── main.py              # Aplicación FastAPI principal
│   ├── config.py            # Configuración
│   └── database.py          # Setup de la base de datos
├── tests/                   # Suite de tests
├── alembic/                 # Migraciones de BD
├── docker-compose.yml       # Orquestación de contenedores
├── Dockerfile               # Imagen Docker multi-stage
├── requirements.txt         # Dependencias Python
├── Makefile                 # Comandos automatizados
└── README.md                # Documentación completa
```

---

## 🔧 Solución de Problemas

### La API no inicia

```bash
# Verificar logs
docker-compose logs api

# Verificar que PostgreSQL esté corriendo
docker-compose ps

# Reiniciar servicios
docker-compose restart
```

### Error de base de datos

```bash
# Revisar conexión a PostgreSQL
docker-compose logs db

# Verificar variables de entorno
cat .env

# Recrear base de datos
docker-compose down -v
docker-compose up --build
```

### Puertos ocupados

```bash
# Cambiar puerto de la API
# Editar .env: API_PORT=8001

# Cambiar puerto de PostgreSQL
# Editar .env: POSTGRES_PORT=5433

# Aplicar cambios
docker-compose down
docker-compose up
```

### Tests fallan

```bash
# Limpiar cache
make clean

# Reinstalar dependencias
pip install -r requirements.txt

# Ejecutar tests con más información
pytest -vv --tb=short
```

---

## 📊 Verificación de Salud

```bash
# Health check de la API
curl http://localhost:8000/health

# Verificar endpoint raíz
curl http://localhost:8000/

# Ver versión de Python en el contenedor
docker-compose exec api python --version

# Ver paquetes instalados
docker-compose exec api pip list
```

---

## 🎯 Flujo de Trabajo Típico

### 1. Desarrollo de una nueva feature

```bash
# 1. Crear rama
git checkout -b feature/nueva-funcionalidad

# 2. Modificar código
# ...

# 3. Crear migración si hay cambios en modelos
make migration msg="añadir campo X"

# 4. Ejecutar tests
make test

# 5. Verificar que todo funciona
make run
# Probar en http://localhost:8000/docs

# 6. Commit y push
git add .
git commit -m "feat: añadir nueva funcionalidad"
git push
```

### 2. Despliegue con Docker

```bash
# 1. Asegurar que .env está configurado
cat .env

# 2. Levantar servicios
docker-compose up --build -d

# 3. Verificar salud
curl http://localhost:8000/health

# 4. Ver logs
docker-compose logs -f
```

### 3. Debugging

```bash
# 1. Ver logs en tiempo real
docker-compose logs -f api

# 2. Acceder al contenedor
docker-compose exec api /bin/sh

# 3. Verificar variables de entorno
docker-compose exec api env

# 4. Ejecutar comandos de Python
docker-compose exec api python -c "from app.database import engine; print(engine.url)"
```

---

## 📚 Recursos

- **Documentación Swagger**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc
- **FastAPI Docs**: https://fastapi.tiangolo.com/
- **SQLAlchemy 2.0**: https://docs.sqlalchemy.org/
- **Pydantic V2**: https://docs.pydantic.dev/
- **Alembic**: https://alembic.sqlalchemy.org/

---

## ✅ Checklist de Verificación

- [ ] Docker y Docker Compose instalados
- [ ] Python 3.11 instalado (para desarrollo local)
- [ ] Archivo `.env` configurado
- [ ] Puerto 8000 disponible
- [ ] Puerto 5432 disponible (PostgreSQL)

---

**¡Listo para desarrollar!** 🎉
