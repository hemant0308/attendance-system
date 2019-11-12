"""Create table section

Revision ID: 3b1aa9e6bba0
Revises: f31f2901e57e
Create Date: 2019-10-24 12:26:46.661059

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3b1aa9e6bba0'
down_revision = 'f31f2901e57e'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('section',
        sa.Column('id',sa.Integer(),nullable=False),
        sa.Column('name',sa.String(50),nullable=False),
        sa.PrimaryKeyConstraint('id',name=op.f('section_pkey')))
    op.create_table('section_session',
        sa.Column('id',sa.Integer(),nullable=False),
        sa.Column('section_id',sa.Integer(),nullable=False),
        sa.Column('start',sa.Time(),nullable=False),
        sa.Column('end',sa.Time(),nullable=False),
        sa.PrimaryKeyConstraint('id',name=op.f('section_session_pkey')))
    op.create_foreign_key('section_session_to_section_fkey','section_session','section',['section_id'],['id'])
    op.drop_constraint('attendance_sheet_to_session','attendance_sheet',type_='foreignkey')
    op.drop_column('attendance_sheet','session_id')
    op.add_column('attendance_sheet',sa.Column('section_session_id',sa.Integer(),nullable=False))
    op.create_foreign_key('attendance_sheet_to_section_session_fkey','attendance_sheet','section_session',['section_session_id'],['id'])

def downgrade():
    op.drop_table('section')
