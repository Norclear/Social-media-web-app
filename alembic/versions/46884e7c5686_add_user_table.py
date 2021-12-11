"""add user table

Revision ID: 46884e7c5686
Revises: 9261737ad1fb
Create Date: 2021-12-11 19:16:54.693236

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql.schema import Column, UniqueConstraint


# revision identifiers, used by Alembic.
revision = '46884e7c5686'
down_revision = '9261737ad1fb'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users',
        sa.Column('id',sa.Integer(),nullable=False),
        sa.Column('email',sa.String(),nullable=False),
        sa.Column('password',sa.String(),nullable=False),
        sa.Column('created_at',sa.TIMESTAMP(timezone=True),
            server_default=sa.text('now()'),nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('email'))
    pass


def downgrade():
    op.drop_table('users')
    pass
