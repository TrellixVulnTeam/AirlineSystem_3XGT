"""update settup

Revision ID: a1cd1792974c
Revises: 68ad01d2256f
Create Date: 2019-11-18 15:36:57.717683

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a1cd1792974c'
down_revision = '68ad01d2256f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('ticket',
    sa.Column('ticket_id', sa.Integer(), nullable=False),
    sa.Column('customer_email', sa.String(length=64), nullable=False),
    sa.Column('airline_name', sa.String(length=64), nullable=False),
    sa.Column('flight_num', sa.String(length=64), nullable=False),
    sa.Column('date_purchased', sa.DateTime(), nullable=True),
    sa.Column('booking_agent_ID', sa.String(length=64), nullable=True),
    sa.ForeignKeyConstraint(['booking_agent_ID'], ['booking_agent.booking_agent_id'], ),
    sa.ForeignKeyConstraint(['customer_email'], ['customer.email'], ),
    sa.ForeignKeyConstraint(['flight_num', 'airline_name'], ['flight.flight_num', 'flight.airline_name'], name='fk_ticket_name_num'),
    sa.PrimaryKeyConstraint('ticket_id', 'airline_name', 'flight_num')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('ticket')
    # ### end Alembic commands ###
