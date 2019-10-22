"""create table attendance

Revision ID: d69500c3db39
Revises: e6ea3038c8c1
Create Date: 2019-10-22 12:11:39.267479

"""
from alembic import op
import sqlalchemy as sa
from niyantra_rest_api.models import AttendanceStatus

# revision identifiers, used by Alembic.
revision = 'd69500c3db39'
down_revision = 'e6ea3038c8c1'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('attendance',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('attendee_id', sa.Integer(), nullable=False),
        sa.Column('date', sa.Date(), nullable=False),
        sa.Column('status', sa.Enum(AttendanceStatus)),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint('id',name=op.f('attendance_pkey'))
    )
    op.create_foreign_key('attendance_to_attendee_fk','attendance','attendee',['attendee_id'],['id'])

def downgrade():
    op.drop_constraint('attendance_to_attendee_fk')
    op.drop_table('attendance')
