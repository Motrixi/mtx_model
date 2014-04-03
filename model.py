from peewee import *
import peewee as pw
import sys
import datetime
import re

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
    #campaign = BigIntegerField(null=True, db_column='campaign_id')
    campaign = ForeignKeyField(Campaign,
                               db_column='campaign_id', related_name='flights')
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
    demo_gender = CharField(max_length=45, null=True)
    demo_hhi = CharField(max_length=45, null=True)
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
    markdown_margin = FloatField(null=True)
    markup_multiplier = FloatField(null=True)
    campaign_category = CharField(max_length=255, null=True)
    
    def get_exchanges(self):
        if self.exchanges :
            return [ex.strip() for ex in self.exchanges.split(',')]
        else :
            return []

    def get_languages(self):
        if self.exchanges :
            return [
                lan.strip() for lan in self.demo_language.split(',')]
        else :
            return []
    
    def get_categories(self):
        if self.target_category :
            return [
                cat.strip() 
                for cat in self.target_category.split(',')]
        else:
            return []

    def get_yobs(self):

        def get_end(pair):
            try:
                return pair[1]
            except IndexError:
                return '100'

        if not self.demo_age:
            return True, []
        elif self.demo_age.upper() == 'ALL':
            return True, []
        ages = [
                { 
                    'begin' : age.strip().split('-')[0].strip('+'),
                    'end'   : get_end(age.strip().split('-'))
                }
                for age in self.demo_age.split(',') 
                    if age.strip().lower() != 'unspecified'
        ]
        current_year = datetime.datetime.now().year
        age_list = []
        for age_range in ages :
            age_list.extend(
                range(
                    int(age_range['begin']), 
                    int(age_range['end']) + 1)
            )
        yobs = [current_year - age for age in age_list]
        exclude_if_not_present = True

        for age in self.demo_age.split(','):
            if age.strip().lower() == 'unspecified':
                exclude_if_not_present = False

        return exclude_if_not_present , yobs

    def get_genders(self):
        if not self.demo_gender:
            return True, []
        exclude_if_not_present = True
        genders = [ gen.strip().lower()
                    for gen in self.demo_gender.split(',')]
        gens = []
        for gen in genders:
            if gen == 'male':
                gens.append('M')
            elif gen == 'female':
                gens.append('F')
            elif gen == 'other':
                exclude_if_not_present = False
        return exclude_if_not_present, gens

    def get_oss(self):
        if self.target_os:
            return [
                os.strip()
                for os in self.target_os.split(',')]
        else:
            return []

    def get_locations(self, all_countries, transformations):
        if not self.geo_country:
            return []
        countries = [
            c.strip()
            for c in self.geo_country.split(',')
        ]
        if countries[0] == 'ALL':
            countries = all_countries
        countries = ['^%s' % c for c in countries]
        # expand country list with transformation
        ext = []
        for c in countries:
            try :
                ext.append('^%s' % transformations[c[1:]])
            except KeyError:
                continue
        countries.extend(ext)
        # go through countries and add states if the country is US
        if self.geo_state and '^US' in countries:
            states = [s.strip() for s in self.geo_state.split(',')]
            if states[0].upper() != 'ALL':
                countries.remove('^US')
                countries.remove('^USA')
                for st in states:
                    countries.append('^US:%s' % st)
                    countries.append('^USA:%s' % st)
        return countries
        
    def get_zips(self):
        if not self.geo_zip:
            return []
        countries = [c.strip().upper() for c in self.geo_country.split(',')]
        if 'US' not in countries :
            if 'ALL' not in countries:
                return []
        zips = [z.strip().upper() for z in self.geo_zip.split(',')]
        return zips
        

    def get_dmas(self):
        if not self.geo_dma:
            return []
        countries = [c.strip().upper() for c in self.geo_country.split(',')]
        if 'US' not in countries :
            if 'ALL' not in countries:
                return []
        dma = [d.strip().upper() for d in self.geo_dma.split(',')]
        return dma

    def get_domains(self):
        if not self.allow_block:
            return True, []
        
        p = re.compile(
                r'[a-zA-Z\d-]{,63}(\.[a-zA-Z\d-]{,63})+') 
        def is_domain(dom):
            if p.match(dom):
                return True
            return False  
        
        domains = [
            d.strip() 
                for d in self.allow_block.split(',') 
                if is_domain(d.strip())]
        
        factor = lambda x : True if x == 'ALLOW' else False
        return factor(self.allow_block_factor), domains

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

class IABSubCategory(BaseModel):
    id = BigIntegerField(primary_key=True)
    cat_code = CharField(max_length=50, null=True)
    cat_name = CharField(max_length=255, null=True)
    cat_subcat = IntegerField(null=True)

    class Meta:
        db_table = 'iabcat_full'

    @classmethod
    def get_subcats(cls, cats):
        categ_list = []
        for cat in cats :
            a_cat = '%s-' % cat
            categ_list.extend(
                [ cat.cat_code for cat in IABSubCategory.select().where(
                    fn.Substr(IABSubCategory.cat_code, 1, len(a_cat)) == a_cat)]
            )
        categ_list.extend(cats)
        return categ_list

if __name__ == '__main__' :
    #print Creative.select().get()
    #print Flight.select().get()
    #print Campaign.select().get()
    #print IABSubCategory.get_subcats(['IAB1','IAB2'])
    print Flight.get(Flight.id==398).get_dmas()
