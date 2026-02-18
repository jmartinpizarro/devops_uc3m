"""
Initial migration: create users and tickets tables
"""
from alembic import op
import sqlalchemy as sa

revision = '20260218_01'   # Identificador único de esta migración
down_revision = None        # Ninguna migración anterior
branch_labels = None
depends_on = None

def upgrade():
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True, index=True),
        sa.Column('name', sa.String, nullable=False),
        sa.Column('email', sa.String, unique=True, nullable=False)
    )
    op.create_table(
        'tickets',
        sa.Column('id', sa.Integer, primary_key=True, index=True),
        sa.Column('author_id', sa.Integer, sa.ForeignKey('users.id'), nullable=False),
        sa.Column('created_at', sa.DateTime, nullable=False),
        sa.Column('title', sa.String, nullable=False),
        sa.Column('description', sa.String, nullable=False),
        sa.Column('tags', sa.String)
    )

def downgrade():
    op.drop_table('tickets')
    op.drop_table('users')
