"""images

Revision ID: 9c0331b0b0c2
Revises: 9f6130afd20f
Create Date: 2024-08-22 11:47:10.981473

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import sqlite

# revision identifiers, used by Alembic.
revision: str = '9c0331b0b0c2'
down_revision: Union[str, None] = '9f6130afd20f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table("images",
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR()),
    sa.Column('file', sa.BINARY())
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
   op.drop_table('images')
    # ### end Alembic commands ###
