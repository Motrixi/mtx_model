from peewee import *
import peewee as pw
import sys

sys.path.append('../')

import settings

database = pw.MySQLDatabase(
                    settings.DB_NAME,
                    **{
                        'user'  : settings.DB_USER,
                        'passwd': settings.DB_PASSWD,
                        'port'  : 3306,
                        'host'  : settings.DB_HOST
                    })

class UnknownFieldType(object):
    pass

class BaseModel(Model):
    class Meta:
        database = database

class Agency(BaseModel):
    account_balance = FloatField(null=True)
    agency_name = CharField(max_length=255, null=True)
    agency_type = CharField(max_length=10, null=True)
    id = BigIntegerField()
    suspended = BooleanField(null=True)  # bit
    url_postback = CharField(max_length=2048, null=True)

    class Meta:
        db_table = 'agency'

class Brand(BaseModel):
    agency = BigIntegerField(null=True, db_column='agency_id')
    brand_name = CharField(max_length=255, null=True)
    id = BigIntegerField()
    url_postback = CharField(max_length=2048, null=True)

    class Meta:
        db_table = 'brand'

class Campaign(BaseModel):
    brand = BigIntegerField(null=True, db_column='brand_id')
    budget_daily = FloatField(null=True)
    budget_total = FloatField(null=True)
    campaign_name = CharField(max_length=255, null=True)
    date_end = DateTimeField(null=True)
    date_start = DateTimeField(null=True)
    id = BigIntegerField()
    impression_daily = BigIntegerField(null=True)
    impression_total = BigIntegerField(null=True)
    state = CharField(max_length=9, null=True)

    class Meta:
        db_table = 'campaign'


class Flight(BaseModel):
    allow_block = TextField(null=True)
    allow_block_factor = CharField(max_length=5, null=True)
    bid_amount = FloatField(null=True)
    bid_type = CharField(max_length=5, null=True)
    budget_daily = FloatField(null=True)
    budget_total = FloatField(null=True)
    campaign = BigIntegerField(null=True, db_column='campaign_id')
    cap = BigIntegerField(null=True)
    cap_on = IntegerField(null=True)
    conversion_value = BigIntegerField(null=True)
    date_end = DateTimeField(null=True)
    date_start = DateTimeField(null=True)
    day_parting = IntegerField(null=True)
    delivery_pace = CharField(max_length=15, null=True)
    demo_age = CharField(max_length=45, null=True)
    demo_children = CharField(max_length=45, null=True)
    demo_edu = CharField(max_length=45, null=True)
    demo_ethnicity = CharField(max_length=1024, null=True)
    demo_gender = CharField(max_length=3, null=True)
    demo_hhi = FloatField(null=True)
    demo_language = CharField(max_length=1024, null=True)
    demo_pets = CharField(max_length=45, null=True)
    demo_relationship = CharField(max_length=45, null=True)
    demo_vehicle = CharField(max_length=45, null=True)
    dp_1 = CharField(max_length=255, null=True)
    dp_2 = CharField(max_length=255, null=True)
    dp_3 = CharField(max_length=255, null=True)
    dp_4 = CharField(max_length=255, null=True)
    dp_5 = CharField(max_length=255, null=True)
    dp_6 = CharField(max_length=255, null=True)
    dp_7 = CharField(max_length=255, null=True)
    exchanges = CharField(max_length=1024, null=True)
    flight_name = CharField(max_length=255, null=True)
    geo_country = CharField(max_length=1024, null=True)
    geo_dma = TextField(null=True)
    geo_state = CharField(max_length=1024, null=True)
    geo_zip = TextField(null=True)
    id = BigIntegerField()
    impression_daily = BigIntegerField(null=True)
    impression_total = BigIntegerField(null=True)
    intent = CharField(max_length=1024, null=True)
    lat_long = CharField(max_length=1024, null=True)
    pixel = TextField(null=True)
    pixel_type = CharField(max_length=6, null=True)
    radius = FloatField(null=True)
    segment_clickers = IntegerField(null=True)
    segment_converters = IntegerField(null=True)
    state = CharField(max_length=9, null=True)
    target_carrier = CharField(max_length=1024, null=True)
    target_category = CharField(max_length=1024, null=True)
    target_environment = CharField(max_length=255, null=True)
    target_name = CharField(max_length=255, null=True)
    target_os = CharField(max_length=1024, null=True)
    target_toggle = IntegerField(null=True)
    
    def get_exchanges(self):
        return [ex.strip() for ex in self.exchanges.split(',')]

    class Meta:
        db_table = 'flight'

class Creative(BaseModel):
    ad_tag = TextField(null=True)
    creative_height = IntegerField(null=True)
    creative_name = CharField(max_length=255, null=True)
    creative_width = IntegerField(null=True)
    domain_destination = CharField(max_length=255, null=True)
    #flight = BigIntegerField(null=True, db_column='flight_id')
    flight = ForeignKeyField(Flight, 
         db_column='flight_id', related_name='creatives')
    id = BigIntegerField()
    url_destination = CharField(max_length=2048, null=True)
    url_icon = CharField(max_length=2048, null=True)
    url_image = CharField(max_length=2048, null=True)
    url_image_preview = CharField(max_length=2048, null=True)
    url_imp = CharField(max_length=2048, null=True)
    url_media = CharField(max_length=2048, null=True)
    url_postback = CharField(max_length=2048, null=True)
    state = CharField(max_length=9, null=True)
    
    class Meta:
        db_table = 'creative'

class Exchange(BaseModel):
    id = BigIntegerField(primary_key=True)
    name = CharField(max_length=20, null=False)

    class Meta:
        db_table = 'exchange'

if __name__ == '__main__' :
    print Creative.select().get()
    print Flight.select().get()
    print Campaign.select().get()
