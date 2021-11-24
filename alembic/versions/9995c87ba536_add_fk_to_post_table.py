"""add fk to post table

Revision ID: 9995c87ba536
Revises: 4e2efd2d8b99
Create Date: 2021-11-24 17:49:02.181702

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9995c87ba536'
down_revision = '4e2efd2d8b99'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('posts_users_fk', source_table='posts', referent_table='users',
                          local_cols=['owner_id'], remote_cols=['id'], ondelete="CASCADE")
    pass


def downgrade():
    op.drop_constraint('post_users_fk', table_name='posts')
    op.drop_column('posts', 'owner_id')
    pass
