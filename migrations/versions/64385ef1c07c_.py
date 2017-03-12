"""empty message

Revision ID: 64385ef1c07c
Revises: 
Create Date: 2017-03-12 07:09:49.999188

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '64385ef1c07c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('profiles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('userimage', sa.String(length=256), nullable=True),
    sa.Column('username', sa.String(length=256), nullable=True),
    sa.Column('userfname', sa.String(length=256), nullable=True),
    sa.Column('userlname', sa.String(length=256), nullable=True),
    sa.Column('userage', sa.String(length=120), nullable=True),
    sa.Column('usersex', sa.String(length=120), nullable=True),
    sa.Column('userhighscore', sa.Integer(), nullable=True),
    sa.Column('usertdollars', sa.Integer(), nullable=True),
    sa.Column('useraddon', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('profiles')
    # ### end Alembic commands ###
