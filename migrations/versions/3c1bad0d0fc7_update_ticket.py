"""update ticket

Revision ID: 3c1bad0d0fc7
Revises: 04073e8541b1
Create Date: 2019-11-17 15:47:39.019864

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3c1bad0d0fc7'
down_revision = '04073e8541b1'
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
    sa.PrimaryKeyConstraint('ticket_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('ticket')
    # ### end Alembic commands ###
