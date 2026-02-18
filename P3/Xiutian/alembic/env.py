import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from dotenv import load_dotenv
load_dotenv()

from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context


config = context.config
# Set sqlalchemy.url desde .env
config.set_main_option("sqlalchemy.url", os.getenv("DATABASE_URL"))

# Configuración de logging
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Importar tus modelos
from app.models.user import Base as UserBase
from app.models.ticket import Base as TicketBase

# Metadata para autogenerate
target_metadata = UserBase.metadata

# --------------------------
def run_migrations_offline():
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url, target_metadata=target_metadata, literal_binds=True, dialect_opts={"paramstyle": "named"}
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
