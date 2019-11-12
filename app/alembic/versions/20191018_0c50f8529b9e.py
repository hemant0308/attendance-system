"""Create table login attempts

Revision ID: 0c50f8529b9e
Revises: 341853804756
Create Date: 2019-10-18 16:54:22.319978

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0c50f8529b9e'
down_revision = '341853804756'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('login_attempt',
        sa.Column('id',sa.Integer(),nullable=False),
        sa.Column('username',sa.String(25),nullable=False),
        sa.Column('is_success',sa.Integer(),nullable=False),
        sa.PrimaryKeyConstraint('id',name=op.f('login_attempt_pkey'))
    )

def downgrade():
    op.drop_table('login_attempt')