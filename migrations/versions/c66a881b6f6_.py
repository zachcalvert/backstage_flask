"""empty message

Revision ID: c66a881b6f6
Revises: None
Create Date: 2015-06-05 16:41:19.376481

"""

# revision identifiers, used by Alembic.
revision = 'c66a881b6f6'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('calculation',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('last_requested', sa.DateTime(), nullable=True),
    sa.Column('number', sa.Integer(), nullable=True),
    sa.Column('value', sa.Integer(), nullable=True),
    sa.Column('occurrences', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('calculation')
    ### end Alembic commands ###