#!/bin/bash

# Script de inicialización del proyecto
# Este script configura el entorno local para desarrollo

set -e

echo "🚀 Iniciando configuración del proyecto Ticket Management API..."

# Verificar Python 3.11
if ! command -v python3.11 &> /dev/null; then
    echo "❌ Error: Python 3.11 no está instalado"
    echo "Por favor instala Python 3.11 antes de continuar"
    exit 1
fi

echo "✅ Python 3.11 detectado"

# Crear entorno virtual
if [ ! -d "venv" ]; then
    echo "📦 Creando entorno virtual..."
    python3.11 -m venv venv
    echo "✅ Entorno virtual creado"
else
    echo "✅ Entorno virtual ya existe"
fi

# Activar entorno virtual
echo "🔧 Activando entorno virtual..."
source venv/bin/activate

# Actualizar pip
echo "📥 Actualizando pip..."
pip install --upgrade pip

# Instalar dependencias
echo "📥 Instalando dependencias..."
pip install -r requirements.txt

# Crear archivo .env si no existe
if [ ! -f ".env" ]; then
    echo "⚙️  Creando archivo .env..."
    cp .env.example .env
    echo "✅ Archivo .env creado. Por favor, revisa y ajusta las configuraciones."
else
    echo "✅ Archivo .env ya existe"
fi

# Crear directorio para base de datos SQLite
mkdir -p data

echo ""
echo "✨ ¡Configuración completada!"
echo ""
echo "📋 Próximos pasos:"
echo "   1. Activar el entorno virtual: source venv/bin/activate"
echo "   2. Ejecutar migraciones: alembic upgrade head"
echo "   3. Iniciar la aplicación: uvicorn app.main:app --reload"
echo ""
echo "🐳 O usa Docker Compose:"
echo "   docker-compose up --build"
echo ""
echo "📖 Documentación: http://localhost:8000/docs"
echo ""
