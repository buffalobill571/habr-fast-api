"""destroy

Revision ID: bce87f21d30c
Revises: beaa35fab64b
Create Date: 2020-03-06 10:36:22.187338

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bce87f21d30c'
down_revision = 'beaa35fab64b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('post_user_id_fkey', 'post', type_='foreignkey')
    op.drop_column('post', 'user_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('post_user_id_fkey', 'post', 'user', ['user_id'], ['id'])
    # ### end Alembic commands ###
