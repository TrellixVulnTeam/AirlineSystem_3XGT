"""long

Revision ID: 38e5c75db7d6
Revises: d3e71ad0e997
Create Date: 2019-10-14 15:14:14.773005

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '38e5c75db7d6'
down_revision = 'd3e71ad0e997'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('airline_stock', sa.Column('id', sa.Integer(), nullable=False))
    op.create_unique_constraint(None, 'airline_stock', ['id'])
    op.create_foreign_key(None, 'flight', 'airline_stock', ['airplane_id'], ['unique_id'])
    op.create_foreign_key(None, 'flight', 'airline_stock', ['airplane_model'], ['model'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'flight', type_='foreignkey')
    op.drop_constraint(None, 'flight', type_='foreignkey')
    op.drop_constraint(None, 'airline_stock', type_='unique')
    op.drop_column('airline_stock', 'id')
    # ### end Alembic commands ###