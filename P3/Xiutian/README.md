# Ticket Management API

## Requisitos
- Python 3.11
- FastAPI
- Pydantic V2
- SQLAlchemy 2.0
- Alembic
- Docker, docker-compose
- PostgreSQL

## Guía de ejecución

1. Copia `.env.example` a `.env` y ajusta las variables si es necesario.
2. Construye y levanta el entorno:

```bash
docker-compose up --build
```

3. Accede a la documentación interactiva en [http://localhost:8000/docs](http://localhost:8000/docs)

## Estructura del proyecto

- `app/`: Código fuente (modelos, esquemas, servicios, rutas)
- `tests/`: Pruebas con pytest y httpx
- `alembic/`: Migraciones de base de datos

## Migraciones

```bash
docker-compose exec api alembic upgrade head
```

## Tests

```bash
docker-compose exec api pytest
```
