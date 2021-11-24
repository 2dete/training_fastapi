"""add last few columns to post table

Revision ID: eb952df21f95
Revises: 9995c87ba536
Create Date: 2021-11-24 17:58:13.036760

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'eb952df21f95'
down_revision = '9995c87ba536'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column(
        'published', sa.Boolean(), nullable=False, server_default='TRUE'
    ))
    op.add_column('posts', sa.Column(
        'created_at', sa.TIMESTAMP(timezone=True), nullable=False,server_default=sa.text('NOW()')
    ))
    pass


def downgrade():
    op.drop_column('post', 'published')
    op.drop_column('posts', 'created_at')
    pass
