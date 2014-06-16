from sqlalchemy import Column
from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy import CHAR
from sqlalchemy.orm import relationship, backref

from custom_types import Base


class DemoAgeBracket(Base):
    __tablename__ = 'demo_age_bracket'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(length=255), nullable=False)
    min_value = Column(Integer, nullable=False)
    max_value = Column(Integer, nullable=False)


class DemoGender(Base):
    __tablename__ = 'demo_gender'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(length=255), nullable=False)
    value = Column(String(length=10), nullable=False)


class DemoLanguage(Base):
    __tablename__ = 'demo_language'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(length=255), nullable=False)
    iso_code = Column(String(length=10), nullable=False)


class DevicePlatform(Base):
    __tablename__ = 'device_platform'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(length=255), nullable=False)


class DeviceType(Base):
    __tablename__ = 'device_type'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(length=255), nullable=False)


class DeviceEnvironment(Base):
    __tablename__ = 'device_environment'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(length=255), nullable=False)


class Exchange(Base):
    __tablename__ = 'exchange'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(length=45), nullable=False)


class Category(Base):
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(length=45), nullable=False)
    iab_code = Column(String(length=10), nullable=False)
    google_code = Column(String(length=10), nullable=False)
    parent_id = Column(Integer, nullable=True)


class Site(Base):
    __tablename__ = 'site'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(length=255), nullable=False)
    type = Column(Integer, nullable=False)
    domain = Column(String(length=255), nullable=True)
    exchange_id = Column(Integer, nullable=True)
    external_id = Column(String(length=45), nullable=False)


class BehaviorSegment(Base):
    __tablename__ = 'behavior_sergment'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(length=255), nullable=False)
    code = Column(String(length=45), nullable=False)
    data_type = Column(Integer, nullable=True)
    vendor_id = Column(Integer, nullable=True)
    parent_id = Column(Integer, nullable=True)


class GeoCountry(Base):
    __tablename__ = 'geo_country'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(length=255), nullable=False)
    iso_a2 = Column(CHAR(length=2), nullable=False)
    iso_a3 = Column(CHAR(length=3), nullable=False)
    iso_num = Column(Integer, nullable=True)
    google_id = Column(String(length=15), nullable=True)


class GeoRegion(Base):
    __tablename__ = 'geo_region'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(length=255), nullable=False)
    iso_code = Column(String(length=10), nullable=False)
    google_id = Column(String(length=15), nullable=True)

    country_id = Column(Integer, ForeignKey('geo_country.id'), nullable=False)
    country = relationship('GeoCountry', backref=backref('regions',
                                                         order_by=id))


class GeoMetro(Base):
    __tablename__ = 'geo_metro'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(length=255), nullable=False)
    dma_code = Column(Integer, nullable=False)
    iso_code = Column(String(length=10), nullable=True)
    google_id = Column(String(length=15), nullable=True)

    region_id = Column(Integer, ForeignKey('geo_region.id'), nullable=False)
    region = relationship('GeoRegion', backref=backref('metros', order_by=id))
