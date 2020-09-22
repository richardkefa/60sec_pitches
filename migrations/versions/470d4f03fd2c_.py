"""empty message

Revision ID: 470d4f03fd2c
Revises: 783bd9a67386
Create Date: 2020-09-22 23:53:57.768994

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '470d4f03fd2c'
down_revision = '783bd9a67386'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comments', sa.Column('user_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'comments', 'users', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'comments', type_='foreignkey')
    op.drop_column('comments', 'user_id')
    # ### end Alembic commands ###
