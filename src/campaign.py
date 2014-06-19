import datetime

from sqlalchemy import Column
from sqlalchemy import ForeignKey, Integer, String, DateTime, Text, Float
from sqlalchemy import CHAR
from sqlalchemy.orm import relationship, backref

from custom_types import Base


class Campaign(Base):
    __tablename__ = 'campaign'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(length=255), nullable=False)


class Flight(Base):
    __tablename__ = 'flight'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(length=255), nullable=False)
    budget_type = Column(Integer, nullable=False)
    bid_type = Column(Integer, nullable=False)
    budget_daily = Column(Float, nullable=True)
    budget_total = Column(Float, nullable=True)
    impression_daily = Column(Integer, nullable=True)
    impression_total = Column(Integer, nullable=True)
    bid_amount = Column(Float, nullable=False)
    start_date = Column(DateTime, nullable=False)
    end_date = Column(DateTime, nullable=False)
    UTF_offset = Column(Integer, nullable=False)
    daypart = Column(CHAR(length=168), nullable=True)
    state = Column(Integer, nullable=False)
    status = Column(Integer, nullable=False)
    created = Column(DateTime, nullable=False, default=datetime.datetime.now)

    brand_id = Column(Integer, ForeignKey('brand.id'), nullable=False)
    brand = relationship("Brand", backref=backref('flights', order_by=id))

    campaign_id = Column(Integer, ForeignKey('campaign.id'), nullable=True)
    campaign = relationship("Campaign", backref=backref('flights',
                                                        order_by=id))

    category_id = Column(Integer, ForeignKey('category.id'), nullable=False)
    category = relationship("Category", backref=backref('flights',
                                                        order_by=id))


class FlightOption(Base):
    __tablename__ = 'flightoption'
    id = Column(Integer, primary_key=True, autoincrement=True)
    key = Column(String(length=45), nullable=False)
    value = Column(String(length=255), nullable=False)

    flight_id = Column(Integer, ForeignKey('flight.id'), nullable=False)
    flight = relationship("Flight", backref=backref('options', order_by=id))


class Target(Base):
    __tablename__ = 'target'
    id = Column(Integer, primary_key=True, autoincrement=True)
    target_id = Column(Integer, nullable=False)

    flight_id = Column(Integer, ForeignKey('flight.id'), nullable=False)
    flight = relationship("Flight", backref=backref('targets', order_by=id))

    target_type_id = Column(Integer, ForeignKey('target_type.id'),
                            nullable=False)
    target_type = relationship("TargetType", backref=backref('targets',
                                                             order_by=id))


class Creative(Base):
    __tablename__ = 'creative'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(length=255), nullable=False)
    type = Column(Integer, nullable=False)
    width = Column(Integer, nullable=False)
    height = Column(Integer, nullable=False)
    ad_domain = Column(String(length=255), nullable=False)
    url_dest = Column(String(length=2048), nullable=False)
    url_image = Column(String(length=2048), nullable=True)
    url_image_preview = Column(String(length=2048), nullable=False)
    url_imp = Column(String(length=2048), nullable=True)
    url_hosted_preview = Column(String(2048), nullable=True)
    url_postback = Column(String(2048), nullable=True)
    ad_tag = Column(Text, nullable=True)
    status = Column(Integer, nullable=False)
    state = Column(Integer, nullable=False)
    created = Column(DateTime, nullable=False, default=datetime.datetime.now)

    flight_id = Column(Integer, ForeignKey('flight.id'), nullable=False)
    flight = relationship("Flight", backref=backref('creatives', order_by=id))
