"""Add column updated_at, updated_by to attendance and attendance_sheet

Revision ID: f5b1e98c5097
Revises: 1d20f40a0d31
Create Date: 2019-10-23 16:38:42.849578

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f5b1e98c5097'
down_revision = '1d20f40a0d31'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('attendance',
        sa.Column('updated_by',sa.Integer()))
    op.add_column('attendance',
        sa.Column('updated_at',sa.DateTime()))
    op.create_foreign_key('attendance_to_login_user_update','attendance','login_user',['updated_by'],['id'])
    op.add_column('attendance_sheet',
        sa.Column('updated_by',sa.Integer()))
    op.add_column('attendance_sheet',
        sa.Column('updated_at',sa.DateTime()))
    op.create_foreign_key('attendance_sheet_to_login_user_update','attendance_sheet','login_user',['updated_by'],['id'])

def downgrade():
    op.drop_constraint('attendance_to_login_user','attendance',type_='foreignkey')
    op.drop_column('updated_by','attendance')
    op.drop_column('updated_at','attendance')
    op.drop_constraint('attendance_sheet_to_login_user','attendance',type_='foreignkey')
    op.drop_column('updated_by','attendance_sheet')
    op.drop_column('updated_at','attendance_sheet')
