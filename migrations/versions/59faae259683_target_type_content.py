"""Target Type content

Revision ID: 59faae259683
Revises: 597bf4cfb0ca
Create Date: 2014-06-19 17:54:06.782816

"""

# revision identifiers, used by Alembic.
revision = '59faae259683'
down_revision = '597bf4cfb0ca'

from alembic import op

from src import general_lookup


def upgrade():
    rows = [
        {'id': 1, 'name': 'BehaviorSegment', 'table': 'behavior_sergment'},
        {'id': 2, 'name': 'Category', 'table': 'category'},
        {'id': 3, 'name': 'DemoAgeBracket', 'table': 'demo_age_bracket'},
        {'id': 4, 'name': 'DemoGender', 'table': 'demo_gender'},
        {'id': 5, 'name': 'DemoLanguage', 'table': 'demo_language'},
        {'id': 6, 'name': 'DeviceEnvironment', 'table': 'device_environment'},
        {'id': 7, 'name': 'DevicePlatform', 'table': 'device_platform'},
        {'id': 8, 'name': 'DeviceType', 'table': 'device_type'},
        {'id': 9, 'name': 'Exchange', 'table': 'exchange'},
        {'id': 10, 'name': 'GeoCountry', 'table': 'geo_country'},
        {'id': 11, 'name': 'GeoMetro', 'table': 'geo_metro'},
        {'id': 12, 'name': 'GeoRegion', 'table': 'geo_region'},
        {'id': 13, 'name': 'Site', 'table': 'site'},
        ]
    op.bulk_insert(general_lookup.TargetType.__table__, rows)


def downgrade():
    op.execute('DELETE FROM %s' % (general_lookup.TargetType.__tablename__))
