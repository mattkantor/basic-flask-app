"""empty message

Revision ID: 5737e3542c9
Revises: 4c087f9202a
Create Date: 2018-08-04 12:35:49.685550

"""

# revision identifiers, used by Alembic.
revision = '5737e3542c9'
down_revision = '4c087f9202a'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('about', sa.Text(), nullable=True))
    op.add_column('users', sa.Column('geolocation', sa.String(), nullable=True))

    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###

    op.drop_column('users', 'geolocation')
    op.drop_column('users', 'about')
    ### end Alembic commands ###
