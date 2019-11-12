"""Add fullname column to login_user

Revision ID: 5512a4f42b5f
Revises: 0c50f8529b9e
Create Date: 2019-10-21 16:26:31.378648

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5512a4f42b5f'
down_revision = '0c50f8529b9e'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('login_user',sa.Column('fullname', sa.String(50), nullable=False))

def downgrade():
    pass
