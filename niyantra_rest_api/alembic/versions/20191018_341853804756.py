"""empty message

Revision ID: 341853804756
Revises: bfd16069d316
Create Date: 2019-10-18 16:20:29.653714

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '341853804756'
down_revision = 'bfd16069d316'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('user_role',
        sa.Column('id',sa.Integer(),nullable=False),
        sa.Column('user_id', sa.Integer(),nullable=False),
        sa.Column('role_id', sa.Integer(),nullable=False),
        sa.PrimaryKeyConstraint('id', name=op.f('user_role_pkey'))
        )
    op.create_foreign_key('user_role_to_user_fk','user_role','login_user',['user_id'],['id'])
    op.create_foreign_key('user_role_to_role_fk','user_role','role',['role_id'],['id'])

def downgrade():
    op.drop_constraint('user_role_to_user_fk','user_role',type_='foreignkey')
    op.drop_constraint('user_role_to_role_fk','user_role',type_='foreignkey')
    op.drop_table('user_role')