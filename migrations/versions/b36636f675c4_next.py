"""next

Revision ID: b36636f675c4
Revises: c9d86a774978
Create Date: 2019-10-04 19:22:09.435863

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b36636f675c4'
down_revision = 'c9d86a774978'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('customer', sa.Column('confirmed', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('customer', 'confirmed')
    # ### end Alembic commands ###