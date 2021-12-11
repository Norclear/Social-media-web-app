"""add content column to post table

Revision ID: 9261737ad1fb
Revises: 94ffc0b032ef
Create Date: 2021-12-11 15:05:35.817924

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9261737ad1fb'
down_revision = '94ffc0b032ef'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts',sa.Column('content',sa.String(),nullable=False))
    pass


def downgrade():
    op.drop_column('posts','content')
    pass
