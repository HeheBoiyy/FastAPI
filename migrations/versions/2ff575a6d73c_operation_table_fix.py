"""Operation Table fix

Revision ID: 2ff575a6d73c
Revises: 543a808fda7b
Create Date: 2024-10-16 21:22:16.585205

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2ff575a6d73c'
down_revision: Union[str, None] = '543a808fda7b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('operation', sa.Column('id', sa.Integer(), nullable=False))
    op.add_column('operation', sa.Column('quantity', sa.String(), nullable=True))
    op.add_column('operation', sa.Column('figi', sa.String(), nullable=True))
    op.add_column('operation', sa.Column('instrument_type', sa.String(), nullable=True))
    op.add_column('operation', sa.Column('date', sa.TIMESTAMP(), nullable=True))
    op.add_column('operation', sa.Column('type', sa.String(), nullable=True))
    op.drop_column('operation', 'Id')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('operation', sa.Column('Id', sa.INTEGER(), autoincrement=True, nullable=False))
    op.drop_column('operation', 'type')
    op.drop_column('operation', 'date')
    op.drop_column('operation', 'instrument_type')
    op.drop_column('operation', 'figi')
    op.drop_column('operation', 'quantity')
    op.drop_column('operation', 'id')
    # ### end Alembic commands ###
