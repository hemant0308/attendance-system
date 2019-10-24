"""Add created_at column to attendance

Revision ID: f31f2901e57e
Revises: f5b1e98c5097
Create Date: 2019-10-23 21:34:48.415274

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f31f2901e57e'
down_revision = 'f5b1e98c5097'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('attendance',
    sa.Column('created_by',sa.Integer()))
    op.create_foreign_key('attendance_to_login_user_created_by','attendance','login_user',['created_by'],['id'])

def downgrade():
    op.drop_constraint('attendance_to_login_user_created_by','attendance',type_='foreignkey')
    op.drop_column('created_by','attendance')
