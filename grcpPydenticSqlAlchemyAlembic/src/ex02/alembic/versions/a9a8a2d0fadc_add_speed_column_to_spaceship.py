"""add speed column to spaceship

Revision ID: a9a8a2d0fadc
Revises: 
Create Date: 2024-02-08 01:14:45.871817

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a9a8a2d0fadc'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('spaceship', sa.Column('speed', sa.Float))


def downgrade() -> None:
    op.drop_column('spaceship', 'speed')


