"""create table attendance_sheet

Revision ID: 8996a7bfbc5e
Revises: 0a923ce27349
Create Date: 2019-10-22 18:00:24.277554

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8996a7bfbc5e'
down_revision = '0a923ce27349'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('attendance_sheet',
        sa.Column('id',sa.Integer(),nullable=False),
        sa.Column('session_id', sa.Integer(),nullable=False),
        sa.Column('date',sa.Date(),nullable=False),
        sa.Column('created_at',sa.DateTime(),nullable=False),
        sa.Column('created_by',sa.Integer(),nullable=False),
        sa.PrimaryKeyConstraint('id',name=op.f('attendance_sheet_pkey')))
    op.create_foreign_key('attendance_sheet_to_session','attendance_sheet','session',['session_id'],['id'])
    op.create_foreign_key('attendance_sheet_to_login_user','attendance_sheet','login_user',['created_by'],['id'])

def downgrade():
    op.drop_constraint('attendance_sheet_to_session','attendance_sheet',type_='foreignkey')
    op.drop_constraint('attendance_sheet_to_login_user','attendance_sheet',type_='foreignkey')
    op.drop_table('attendance_sheet')