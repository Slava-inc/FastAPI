"""map_object_mod1

Revision ID: ae8114855e58
Revises: 136a2550779d
Create Date: 2024-08-20 15:47:08.211522

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ae8114855e58'
down_revision: Union[str, None] = '136a2550779d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('map_object')
    op.create_table('map_object',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('title', sa.VARCHAR(), nullable=False),
    sa.Column('other_titles', sa.VARCHAR(), nullable=True),
    sa.Column('connect', sa.VARCHAR(), nullable=True),
    sa.Column('add_time', sa.DateTime(), nullable=False),
    sa.Column('user_id', sa.INTEGER(), nullable=True),
    sa.Column('coords', sa.VARCHAR(), nullable=False),  
    sa.Column('level', sa.VARCHAR(), nullable=True),
    sa.Column('images', sa.BINARY(), nullable=True)  
    ) 
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('map_object')
    op.create_table('map_object',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('title', sa.VARCHAR(), nullable=False),
    sa.Column('other_titles', sa.VARCHAR(), nullable=True),
    sa.Column('connect', sa.VARCHAR(), nullable=True),
    sa.Column('add_time', sa.DATETIME(), nullable=False),
    sa.Column('user', sa.BLOB(), nullable=True),
    sa.Column('coords', sa.BLOB(), nullable=True),
    sa.Column('level', sa.BLOB(), nullable=False),
    sa.Column('images', sa.NUMERIC(), nullable=True)
    )
    # ### end Alembic commands ###
