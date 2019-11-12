"""empty message

Revision ID: bfd16069d316
Revises: cee05034f991
Create Date: 2019-10-18 16:17:46.151127

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bfd16069d316'
down_revision = 'cee05034f991'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('role',
        sa.Column('id',sa.Integer(), nullable=False),
        sa.Column('name',sa.String(25), nullable=False),
        sa.PrimaryKeyConstraint('id', name=op.f('role_pkey'))
        )


def downgrade():
    op.drop_table('role')