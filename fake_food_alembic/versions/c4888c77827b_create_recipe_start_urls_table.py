"""Create Recipe Start URLs table

Revision ID: c4888c77827b
Revises: 
Create Date: 2018-01-03 10:08:53.921999

"""
from alembic import op
import sqlalchemy as sa
from datetime import datetime


# revision identifiers, used by Alembic.
revision = 'c4888c77827b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'start_urls',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(100)),
        sa.Column('url', sa.String(1000)),
        sa.Column('url_hash', sa.String(1000)),
        sa.Column('date', sa.DateTime, default=datetime.utcnow()),
        sa.Column('is_recipe', sa.Unicode(200)),
        sa.Column('s_id', sa.Integer)

    )

    op.create_table(
        'recipes',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(100)),
        sa.Column('url', sa.String(1000)),
        sa.Column('url_hash', sa.String(1000)),
        sa.Column('date_collected', sa.DateTime, default=datetime.utcnow()),
        sa.Column('date_published', sa.DateTime),
        sa.Column('ingredients', sa.String(1000)),
        sa.Column('method', sa.String(2000)
    )


def downgrade():
    pass

