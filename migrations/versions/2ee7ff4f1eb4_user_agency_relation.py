"""User Agency relation

Revision ID: 2ee7ff4f1eb4
Revises: 28dd231a45a9
Create Date: 2014-06-09 16:29:26.938135

"""

# revision identifiers, used by Alembic.
revision = '2ee7ff4f1eb4'
down_revision = '28dd231a45a9'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.add_column('user', sa.Column('agency_id', sa.Integer(), nullable=True))
    op.create_foreign_key('fk_agency_user', 'user', 'agency', ['agency_id'],
                          ['id'])


def downgrade():
    op.drop_constraint('fk_agency_user', 'user', 'foreignkey')
    op.drop_column('user', 'agency_id')
