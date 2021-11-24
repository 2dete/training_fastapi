"""add content to post table

Revision ID: 19f2174a83ce
Revises: c68c9116ae0c
Create Date: 2021-11-24 17:32:13.047190

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '19f2174a83ce'
down_revision = 'c68c9116ae0c'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts", sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_table('posts', 'content')
    pass
