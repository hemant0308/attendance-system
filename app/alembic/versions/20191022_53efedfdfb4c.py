"""create table session

Revision ID: 53efedfdfb4c
Revises: d69500c3db39
Create Date: 2019-10-22 17:13:22.372194

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '53efedfdfb4c'
down_revision = 'd69500c3db39'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('session',
        sa.Column('id',sa.Integer(),nullable=False),
        sa.Column('start',sa.Time(),nullable=False),
        sa.Column('end',sa.Time(),nullable=False),
        sa.PrimaryKeyConstraint('id',name=op.f('session_pkey')))

def downgrade():
    op.drop_table('session')
