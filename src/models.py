import datetime

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Table, Column
from sqlalchemy import ForeignKey, Integer, String, DateTime, Text
from sqlalchemy.orm import relationship, backref

Base = declarative_base()


User_Brand = Table('user_brand',
                   Base.metadata,
                   Column('id', Integer, primary_key=True),
                   Column('user_id', Integer, ForeignKey('user.id')),
                   Column('brand_id', Integer, ForeignKey('brand.id')),
                   )


class Role(Base):
    __tablename__ = 'role'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(length=45), nullable=False)


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(length=255), nullable=False)
    passhash = Column(String(length=255), nullable=False)
    first_name = Column(String(length=255), nullable=False)
    last_name = Column(String(length=255), nullable=False)
    token = Column(String(length=255), nullable=True)
    status = Column(Integer, nullable=True)
    created = Column(DateTime, nullable=False, default=datetime.datetime.now)
    skype_id = Column(String(length=255), nullable=True)

    role_id = Column(Integer, ForeignKey('role.id'))
    role = relationship("Role", backref=backref('users', order_by=id))


class Brand(Base):
    __tablename__ = 'brand'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(length=45), nullable=False)
    domain = Column(String(length=255), nullable=False)
    created = Column(DateTime, nullable=False, default=datetime.datetime.now)

    agency_id = Column(Integer, ForeignKey('agency.id'))
    agency = relationship("Agency", backref=backref('brand', order_by=id))

    users = relationship('User', secondary=User_Brand, backref='brands')


class BrandOptions(Base):
    __tablename__ = 'brand_options'
    id = Column(Integer, primary_key=True, autoincrement=True)
    key = Column(String(length=45), nullable=False)
    value = Column(String(length=45), nullable=True)

    brand_id = Column(Integer, ForeignKey('brand.id'))
    brand = relationship("Brand", backref=backref('options', order_by=id))


class Agency(Base):
    __tablename__ = 'agency'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(length=45), nullable=False)
    domain = Column(String(length=255), nullable=False)
    type = Column(String(length=45), nullable=False)
    created = Column(DateTime, nullable=False, default=datetime.datetime.now)


class AgencyOptions(Base):
    __tablename__ = 'agency_options'
    id = Column(Integer, primary_key=True, autoincrement=True)
    key = Column(String(length=45), nullable=False)
    value = Column(String(length=45), nullable=True)

    agency_id = Column(Integer, ForeignKey('agency.id'))
    agency = relationship("Agency", backref=backref('options', order_by=id))


class AgencyInfo(Base):
    __tablename__ = 'agency_info'
    id = Column(Integer, primary_key=True, autoincrement=True)
    address = Column(String(length=255), nullable=False)
    address2 = Column(String(length=255), nullable=False)
    city = Column(String(length=255), nullable=False)
    state = Column(String(length=30), nullable=True)
    postcode = Column(String(length=30), nullable=True)
    country = Column(String(length=45), nullable=False)
    phone = Column(String(length=15), nullable=True)
    contact = Column(String(length=100), nullable=True)

    agency_id = Column(Integer, ForeignKey('agency.id'))
    agency = relationship("Agency", backref=backref('info', order_by=id))


class AuditLog(Base):
    __tablename__ = 'auditlog'
    id = Column(Integer, primary_key=True, autoincrement=True)
    event_dt = Column(DateTime, nullable=False, default=datetime.datetime.now)
    event_type = Column(String(length=45), nullable=False)
    object_type = Column(String(length=45), nullable=False)
    user_id = Column(Integer, nullable=False)
    data = Column(Text, nullable=True)
