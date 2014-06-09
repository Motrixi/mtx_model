"""Default Roles

Revision ID: 52a13b05a9
Revises: 2ee7ff4f1eb4
Create Date: 2014-06-09 22:13:56.446053

"""

# revision identifiers, used by Alembic.
revision = '52a13b05a9'
down_revision = '2ee7ff4f1eb4'

from alembic import op


def upgrade():
    op.execute("INSERT INTO role VALUES (1, 'Motrixi Admin')")
    op.execute("INSERT INTO role VALUES (2, 'Agency Admin' )")
    op.execute("INSERT INTO role VALUES (3, 'Brand User'   )")
    op.execute("INSERT INTO role VALUES (4, 'Campaign User')")
    op.execute("INSERT INTO role VALUES (5, 'Report User'  )")


def downgrade():
    op.execute("delete from role")
