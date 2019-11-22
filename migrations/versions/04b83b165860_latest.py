"""latest

Revision ID: 04b83b165860
Revises: baa2a0dee614
Create Date: 2019-11-15 14:20:27.923937

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '04b83b165860'
down_revision = 'baa2a0dee614'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key('fk_ticket_name_num', 'ticket', 'flight', ['flight_num', 'airline_name'], ['flight_num', 'airline_name'])
    op.create_foreign_key(None, 'ticket', 'booking_agent', ['booking_agent_ID'], ['booking_agent_id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'ticket', type_='foreignkey')
    op.drop_constraint('fk_ticket_name_num', 'ticket', type_='foreignkey')
    # ### end Alembic commands ###
