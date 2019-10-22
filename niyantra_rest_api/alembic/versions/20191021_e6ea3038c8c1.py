"""Create table attendee

Revision ID: e6ea3038c8c1
Revises: 5512a4f42b5f
Create Date: 2019-10-21 17:09:32.390382

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e6ea3038c8c1'
down_revision = '5512a4f42b5f'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('attendee',
        sa.Column('id',sa.Integer(),nullable=False),
        sa.Column('firstname',sa.String(50),nullable=False),
        sa.Column('lastname',sa.String(50)),
        sa.PrimaryKeyConstraint('id',name=op.f('attendee_pkey'))
    )


def downgrade():
    op.drop_table('attendee')
