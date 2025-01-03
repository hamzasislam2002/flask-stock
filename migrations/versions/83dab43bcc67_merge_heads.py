"""Merge heads

Revision ID: 83dab43bcc67
Revises: 031c22a22f8e, e462e4622f98
Create Date: 2025-01-03 12:10:00.805252

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '83dab43bcc67'
down_revision = ('031c22a22f8e', 'e462e4622f98')
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('password_hashed', sa.String(128), nullable=False),
    sa.PrimaryKeyConstraint('id'))


def downgrade():
    op.drop_table('users')
