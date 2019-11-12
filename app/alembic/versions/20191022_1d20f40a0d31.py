"""add column attandance_sheet_id to attendance

Revision ID: 1d20f40a0d31
Revises: 8996a7bfbc5e
Create Date: 2019-10-22 18:12:27.292932

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1d20f40a0d31'
down_revision = '8996a7bfbc5e'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('attendance',
                  sa.Column('attendance_sheet_id',sa.Integer(),nullable=False))
    op.create_foreign_key('attendance_to_attendance_sheet_id','attendance','attendance_sheet',['attendance_sheet_id'],['id'])


def downgrade():
    op.drop_constraint('attendance_to_attendance_sheet_id','attendance',type_='foreignkey')
    op.drop_column('attendance_sheet_id','attendance')
