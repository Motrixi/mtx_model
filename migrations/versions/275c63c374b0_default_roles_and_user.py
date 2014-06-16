"""Default roles and user

Revision ID: 275c63c374b0
Revises: 58edef7c6059
Create Date: 2014-06-16 13:58:16.257707

"""

# revision identifiers, used by Alembic.
revision = '275c63c374b0'
down_revision = '58edef7c6059'

from alembic import op


def upgrade():
    op.execute("INSERT INTO role VALUES (1, 'Motrixi Admin')")
    op.execute("INSERT INTO role VALUES (2, 'Agency Admin' )")
    op.execute("INSERT INTO role VALUES (3, 'Brand User'   )")
    op.execute("INSERT INTO role VALUES (4, 'Campaign User')")
    op.execute("INSERT INTO role VALUES (5, 'Report User'  )")

    op.execute("""INSERT INTO agency VALUES (1, 'Motrixi Agency',
        'http://motrixi.com', 'Admin', 1, NOW())""")

    op.execute("""INSERT INTO user (
            id, email, passhash, first_name, last_name, created, role_id,
            agency_id
        ) VALUES (
            1,
            'admin@motrixi.com',
            '7f89c67693cdfef352373717d766bd9ae9cd0400627760dbd2b6f81d55bc6fde',
            'Admin First Name',
            'Admin Last Name',
            NOW(),
            1,
            1
            )
            """)


def downgrade():
    op.execute('DELETE FROM user WHERE id = 1')
    op.execute('DELETE FROM agency WHERE id = 1')
    op.execute('DELETE FROM role')
