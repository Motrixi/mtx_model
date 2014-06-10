"""First User

Revision ID: 13db793fd487
Revises: 52a13b05a9
Create Date: 2014-06-09 23:29:14.634172

"""

# revision identifiers, used by Alembic.
revision = '13db793fd487'
down_revision = '52a13b05a9'

from alembic import op


def upgrade():
    op.execute("""INSERT INTO user (
            id, email, passhash, first_name, last_name, created, role_id
        ) VALUES (
            1,
            'admin@motrixi.com',
            '7f89c67693cdfef352373717d766bd9ae9cd0400627760dbd2b6f81d55bc6fde',
            'Admin First Name',
            'Admin Last Name',
            NOW(),
            1
            )
            """)


def downgrade():
    op.execute("delete from user where id = 1")
