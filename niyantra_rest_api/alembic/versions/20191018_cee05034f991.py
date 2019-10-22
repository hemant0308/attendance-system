"""empty message

Revision ID: cee05034f991
Revises: 
Create Date: 2019-10-18 16:17:14.973929

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cee05034f991'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    op.create_table('login_user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(25), nullable=True),
    sa.Column('password', sa.String(256), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('login_user_pkey'))
    )
    op.create_index('login_user_idx_username', 'login_user', ['username'], unique=True, mysql_length=25)


def downgrade():
    op.drop_index('login_user_idx_username', table_name='login_user')
    op.drop_table('login_user')