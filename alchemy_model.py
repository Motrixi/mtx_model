from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, BigInteger, Text,\
                       Time, DATETIME, Boolean
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, backref

import sys
import datetime
import re
import urllib

sys.path.append('../')

import settings

Base = declarative_base()


class Agency(Base):
    __tablename__ = 'agency'
    id                 = Column(Integer, primary_key=True, autoincrement=True)
    account_balance    = Column(Float,                    nullable=True)
    agency_name        = Column(String(length=255),       nullable=True)
    agency_type        = Column(String(length=255),       nullable=True)
    suspended          = Column(Boolean,                  nullable=True)
    url_postback       = Column(String(length=2048),      nullable=True)


class Brand(Base):
    __tablename__ = 'brand'
    id                 = Column(Integer, primary_key=True, autoincrement=True)
    brand_name         = Column(String(length=255),       nullable=True)
    url_postback       = Column(String(length=2048),      nullable=True)

    agency_id          = Column(Integer, ForeignKey('agency.id'))
    agency             = relationship("Agency", 
                                backref=backref('brand', order_by=id))

class Campaign(Base):
    __tablename__ = 'campaign'
    id                 = Column(Integer, primary_key=True, autoincrement=True)
    budget_daily       = Column(Float,                    nullable=True)
    budget_total       = Column(Float,                    nullable=True)
    campaign_name      = Column(String(length=255),       nullable=True)
    date_end           = Column(DATETIME,                 nullable=True)
    date_start         = Column(DATETIME,                 nullable=True)
    impression_daily   = Column(BigInteger,               nullable=True)
    impression_total   = Column(BigInteger,               nullable=True)
    state              = Column(String(length=255),       nullable=True)

    brand_id           = Column(Integer, ForeignKey('brand.id'))
    brand              = relationship("Brand", 
                                backref=backref('campaigns', order_by=id))
        

class Flight(Base):
    __tablename__ = 'flight'
    
    id                 = Column(Integer, primary_key=True, autoincrement=True)
    bid_amount         = Column(Float,                  nullable=True)
    allow_block        = Column(Text,                   nullable=True)
    allow_block_factor = Column(String(length=255),     nullable=True)
    bid_type           = Column(String(length=5),       nullable=True)
    budget_daily       = Column(Float,                  nullable=True)
    budget_total       = Column(Float,                  nullable=True)
    cap                = Column(BigInteger,             nullable=True)
    cap_on             = Column(Integer,                nullable=True)
    conversion_value   = Column(BigInteger,             nullable=True)
    date_end           = Column(DATETIME,               nullable=True)
    date_start         = Column(DATETIME,               nullable=True)
    day_parting        = Column(Integer,                nullable=True)
    delivery_pace      = Column(String(length=255),     nullable=True)
    demo_age           = Column(String(length=45),      nullable=True)
    demo_children      = Column(String(length=45),      nullable=True)
    demo_edu           = Column(String(length=45),      nullable=True)
    demo_ethnicity     = Column(String(length=1024),    nullable=True)
    demo_gender        = Column(String(length=45),      nullable=True)
    demo_hhi           = Column(String(length=45),      nullable=True)
    demo_language      = Column(String(length=45),      nullable=True)
    demo_pets          = Column(String(length=45),      nullable=True)
    demo_relationship  = Column(String(length=45),      nullable=True)
    demo_vehicle       = Column(String(length=45),      nullable=True)
    dp_1               = Column(String(length=255),     nullable=True)
    dp_2               = Column(String(length=255),     nullable=True)
    dp_3               = Column(String(length=255),     nullable=True)
    dp_4               = Column(String(length=255),     nullable=True)
    dp_5               = Column(String(length=255),     nullable=True)
    dp_6               = Column(String(length=255),     nullable=True)
    dp_7               = Column(String(length=255),     nullable=True)
    exchanges          = Column(String(length=1024),    nullable=True)
    flight_name        = Column(String(length=255),     nullable=True)
    geo_country        = Column(String(length=1024),    nullable=True)
    geo_dma            = Column(Text,                   nullable=True)
    geo_state          = Column(String(length=1024),    nullable=True)
    geo_zip            = Column(Text,                   nullable=True)
    impression_daily   = Column(BigInteger,             nullable=True)
    impression_total   = Column(BigInteger,             nullable=True)
    intent             = Column(Text,                   nullable=True)
    lat_long           = Column(Text,                   nullable=True)
    pixel              = Column(Text,                   nullable=True)
    pixel_type         = Column(String(length=255),     nullable=True)
    radius             = Column(Float,                  nullable=True)
    segment_clickers   = Column(Integer,                nullable=True)
    segment_converters = Column(Integer,                nullable=True)
    state              = Column(String(length=255),     nullable=True)
    target_carrier     = Column(String(length=1024),    nullable=True)
    target_category    = Column(String(length=1024),    nullable=True)
    target_environment = Column(String(length=255),     nullable=True)
    target_name        = Column(String(length=255),     nullable=True)
    target_os          = Column(String(length=255),     nullable=True)
    target_toggle      = Column(Integer,                nullable=True)
    markdown_margin    = Column(Float,                  nullable=True)
    markup_multiplier  = Column(Float,                  nullable=True)
    campaign_category  = Column(String(length=255),     nullable=True)

    campaign_id        = Column(Integer, ForeignKey('campaign.id'))
    campaign           = relationship("Campaign", 
                                backref=backref('flights', order_by=id))

    def get_exchanges(self):
        if self.exchanges :
            return [ex.strip() for ex in self.exchanges.split(',')]
        else :
            return []

    def get_languages(self):
        if self.demo_language :
            return [
                lan.strip().upper() for lan in self.demo_language.split(',')]
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

        return exclude_if_not_present, yobs

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
                os.strip().lower()
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
            urllib.quote(d.strip().encode('utf-8'))
                for d in self.allow_block.split(',') 
                if is_domain(d.strip())]

        extended = ['http%%3A%%2F%%2F%s' % d for d in domains]
        domains.extend(extended)
        factor = lambda x : True if x == 'ALLOW' else False
        return factor(self.allow_block_factor), domains

    def get_apps(self):
        if not self.allow_block:
            return True, []

        p = re.compile(
                r'[a-zA-Z\d-]{,63}(\.[a-zA-Z\d-]{,63})+') 
        def is_domain(dom):
            if p.match(dom):
                return True
            return False  
        
        apps = [
            urllib.quote(d.strip().encode('utf-8'))
                for d in self.allow_block.split(',') 
                if not is_domain(d.strip())]
        
        factor = lambda x : True if x == 'ALLOW' else False
        return factor(self.allow_block_factor), apps



class Creative(Base):
    __tablename__ = 'creative'
    id                 = Column(Integer, primary_key=True, autoincrement=True)
    ad_tag             = Column(Text,                      nullable=True)
    creative_height    = Column(Integer,                   nullable=True)
    creative_name      = Column(String(length=255),        nullable=True)
    creative_width     = Column(Integer,                   nullable=True)
    domain_destination = Column(String(length=255),        nullable=True)
    url_destination    = Column(String(length=2048),       nullable=True)
    url_icon           = Column(String(length=2048),       nullable=True)
    url_image          = Column(String(length=2048),       nullable=True)
    url_image_preview  = Column(String(length=2048),       nullable=True)
    url_imp            = Column(String(length=2048),       nullable=True)
    url_media          = Column(String(length=2048),       nullable=True)
    url_postback       = Column(String(length=2048),       nullable=True)
    state              = Column(String(length=255),        nullable=True)

    flight_id          = Column(Integer, ForeignKey('flight.id'))
    flight             = relationship("Flight", 
                                backref=backref('creatives', order_by=id))
    

class Exchange(Base):
    __tablename__ = 'exchange'
    id                 = Column(Integer, primary_key=True, autoincrement=True)
    name               = Column(String(length=50),     nullable=True)

class IABSubCategory(Base):
    __tablename__ = 'iabcat_full'
    id                 = Column(Integer, primary_key=True, autoincrement=True)
    cat_code           = Column(String(length=50),        nullable=True)
    cat_name           = Column(String(length=255),       nullable=True)
    cat_subcat         = Column(Integer,                  nullable=True)

    @classmethod
    def get_subcats(cls, session, cats):
        categ_list = []
        for cat in cats :
            a_cat = '%s-' % cat
            categ_list.extend(
                [ cat.cat_code for cat in session.query(IABSubCategory).filter
                    (IABSubCategory.cat_code.like('%s%%' % a_cat))]
            )
        categ_list.extend(cats)
        return categ_list

class Event(Base):
    __tablename__ = 'event'

    IMPRESSION_CAP_TOTAL   = 1
    IMPRESSION_CAP_DAILY   = 2
    IMPRESSION_CAP_RELEASE = 3

    id                 = Column(Integer, primary_key=True, autoincrement=True)
    type               = Column(Integer,      nullable=True)
    ts                 = Column(BigInteger,   nullable=True)
    flight_id          = Column(Integer, ForeignKey('flight.id'))
    flight             = relationship("Flight", 
                                backref=backref('events', order_by=id))
    

if __name__ == '__main__':

    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    
    print 'SQLAlchemy tests'

    engine = create_engine(
                'mysql://root:pepe123@localhost/bu?charset=utf8', echo=True)
    Session = sessionmaker(bind=engine, autocommit=True)
    session = Session()   

    f = session.query(Flight).filter(Flight.id == 398).first()
    print f.campaign.campaign_name
    print f.campaign.brand.brand_name
    print f.campaign.brand.agency.agency_name
    print f.get_exchanges()
    print f.get_languages()
    print f.get_categories()
    print f.get_yobs()
    print f.get_genders()
    print f.get_oss()
    print f.get_locations(settings.COUNTRIES_ALL,
                          settings.COUNTRIES_ALPHA2_TO_ALPHA3)
    print f.get_zips()
    print f.get_dmas()
    print f.get_domains()
    print f.get_apps()
    for c in f.creatives:
        print c.creative_name
    print IABSubCategory.get_subcats(session, ['IAB1','IAB2',])
