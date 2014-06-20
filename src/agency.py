import datetime

from sqlalchemy import Table, Column
from sqlalchemy import ForeignKey, Integer, String, DateTime, Text
from sqlalchemy.orm import relationship, backref

from itsdangerous import BadSignature, SignatureExpired, \
    TimedJSONWebSignatureSerializer as Serializer

from custom_types import Base, PasswordType


User_Brand = Table('user_brand',
                   Base.metadata,
                   Column('id', Integer, primary_key=True),
                   Column('user_id', Integer, ForeignKey('user.id'),
                          nullable=False),
                   Column('brand_id', Integer, ForeignKey('brand.id'),
                          nullable=False),
                   )


class Role(Base):
    __tablename__ = 'role'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(length=45), nullable=False)


class User(Base):
    __tablename__ = 'user'
    hide_columns = ['passhash', 'token']
    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(length=255), nullable=False, unique=True)
    passhash = Column(PasswordType(length=70), nullable=False)
    first_name = Column(String(length=45), nullable=False)
    last_name = Column(String(length=45), nullable=False)
    token = Column(String(length=255), nullable=True)
    status = Column(Integer, nullable=True)
    created = Column(DateTime, nullable=False, default=datetime.datetime.now)
    skype_id = Column(String(length=255), nullable=True)

    role_id = Column(Integer, ForeignKey('role.id'), nullable=False)
    role = relationship("Role", backref=backref('users', order_by=id))

    agency_id = Column(Integer, ForeignKey('agency.id'), nullable=False)
    agency = relationship('Agency', backref=backref('users', order_by=id))

    def generate_token(self, secret_key, expires=600):
        s = Serializer(secret_key, expires_in=expires)
        self.token = s.dumps({'user_id': self.id})

    @classmethod
    def verify_credentials(cls, session, email, password):
        total = session.query(cls).filter_by(email=email, passhash=password) \
            .count()
        return total == 1

    @classmethod
    def verify_token(cls, session, secret_key, token):
        try:
            data = Serializer(secret_key).loads(token)
            if not 'user_id' in data:
                raise BadSignature('Invalid Token')
            user = session.query(User).get(data['user_id'])
            if not user:
                raise BadSignature('Invalid Userd Id')
            return user
        except (SignatureExpired, BadSignature):
            return False


class Brand(Base):
    __tablename__ = 'brand'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(length=45), nullable=False)
    domain = Column(String(length=255), nullable=False)
    created = Column(DateTime, nullable=False, default=datetime.datetime.now)

    agency_id = Column(Integer, ForeignKey('agency.id'), nullable=False)
    agency = relationship("Agency", backref=backref('brands', order_by=id))

    users = relationship('User', secondary=User_Brand, backref='brands')


class BrandOption(Base):
    __tablename__ = 'brand_option'
    id = Column(Integer, primary_key=True, autoincrement=True)
    key = Column(String(length=45), nullable=False)
    value = Column(String(length=255), nullable=False)

    brand_id = Column(Integer, ForeignKey('brand.id'), nullable=False)
    brand = relationship("Brand", backref=backref('options', order_by=id))


class Agency(Base):
    __tablename__ = 'agency'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(length=255), nullable=False)
    domain = Column(String(length=255), nullable=False)
    type = Column(String(length=45), nullable=False)
    status = Column(Integer, nullable=False)
    created = Column(DateTime, nullable=False, default=datetime.datetime.now)


class AgencyOption(Base):
    __tablename__ = 'agency_option'
    id = Column(Integer, primary_key=True, autoincrement=True)
    key = Column(String(length=45), nullable=False)
    value = Column(String(length=255), nullable=False)

    agency_id = Column(Integer, ForeignKey('agency.id'), nullable=False)
    agency = relationship("Agency", backref=backref('options', order_by=id))


class AgencyInfo(Base):
    __tablename__ = 'agency_info'
    id = Column(Integer, primary_key=True, autoincrement=True)
    address = Column(String(length=255), nullable=False)
    address2 = Column(String(length=255), nullable=True)
    city = Column(String(length=255), nullable=False)
    state = Column(String(length=30), nullable=True)
    postcode = Column(String(length=30), nullable=True)
    country = Column(String(length=45), nullable=False)
    phone = Column(String(length=15), nullable=True)
    contact = Column(String(length=100), nullable=True)

    agency_id = Column(Integer, ForeignKey('agency.id'), nullable=False)
    agency = relationship("Agency", backref=backref('info', order_by=id))


class AuditLog(Base):
    __tablename__ = 'auditlog'
    id = Column(Integer, primary_key=True, autoincrement=True)
    event_dt = Column(DateTime, nullable=False, default=datetime.datetime.now)
    event_type = Column(String(length=45), nullable=False)
    object_type = Column(String(length=45), nullable=False)
    user_id = Column(Integer, nullable=False)
    data = Column(Text, nullable=True)
