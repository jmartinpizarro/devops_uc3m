.PHONY: help install run test clean docker-build docker-up docker-down migrate migration lint format

help: ## Mostrar este mensaje de ayuda
	@echo "Comandos disponibles:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2}'

install: ## Instalar dependencias en entorno virtual
	python3.11 -m venv venv
	. venv/bin/activate && pip install --upgrade pip
	. venv/bin/activate && pip install -r requirements.txt
	cp .env.example .env

run: ## Ejecutar la aplicación en modo desarrollo
	uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

run-prod: ## Ejecutar la aplicación en modo producción
	uvicorn app.main:app --host 0.0.0.0 --port 8000 --workers 4

test: ## Ejecutar tests con pytest
	pytest -v

test-cov: ## Ejecutar tests con reporte de cobertura
	pytest --cov=app --cov-report=html --cov-report=term-missing

test-watch: ## Ejecutar tests en modo watch
	pytest-watch

clean: ## Limpiar archivos temporales y cache
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	find . -type d -name "*.egg-info" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".pytest_cache" -exec rm -rf {} + 2>/dev/null || true
	rm -rf htmlcov/
	rm -rf .coverage
	rm -rf test.db
	rm -rf tickets.db

docker-build: ## Construir imagen Docker
	docker-compose build

docker-up: ## Levantar servicios con Docker Compose
	docker-compose up --build

docker-down: ## Detener servicios Docker Compose
	docker-compose down

docker-clean: ## Detener servicios y eliminar volúmenes
	docker-compose down -v

docker-logs: ## Ver logs de Docker Compose
	docker-compose logs -f

migrate: ## Ejecutar migraciones de base de datos
	alembic upgrade head

migration: ## Crear nueva migración (uso: make migration msg="descripcion")
	alembic revision --autogenerate -m "$(msg)"

migrate-rollback: ## Revertir última migración
	alembic downgrade -1

migrate-history: ## Ver historial de migraciones
	alembic history

db-shell: ## Acceder a shell de PostgreSQL
	docker-compose exec db psql -U user -d ticketdb

api-shell: ## Acceder a shell del contenedor API
	docker-compose exec api /bin/sh

lint: ## Verificar código con flake8
	flake8 app tests --max-line-length=120 --exclude=venv,alembic

format: ## Formatear código con black
	black app tests --line-length=120

type-check: ## Verificar tipos con mypy
	mypy app --ignore-missing-imports

dev-setup: ## Configuración completa para desarrollo
	./setup.sh

requirements: ## Actualizar requirements.txt
	pip freeze > requirements.txt

health: ## Verificar salud de la API
	curl http://localhost:8000/health

docs: ## Abrir documentación de la API
	@echo "Abriendo documentación en http://localhost:8000/docs"
	@which xdg-open > /dev/null && xdg-open http://localhost:8000/docs || open http://localhost:8000/docs || echo "Por favor abre http://localhost:8000/docs en tu navegador"
