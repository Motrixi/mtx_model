import hashlib
import datetime

from sqlalchemy.ext.declarative import declarative_base as\
    real_declarative_base
from sqlalchemy import TypeDecorator, type_coerce, String

# Let's make this a class decorator
declarative_base = lambda cls: real_declarative_base(cls=cls)


@declarative_base
class Base(object):
    """
    Add some default properties and methods to the SQLAlchemy declarative base.
    """
    __table_args__ = {'mysql_engine': 'InnoDB'}

    @property
    def columns(self):
        return [c.name for c in self.__table__.columns]

    @property
    def columnitems(self):
        res = {}
        for column in self.columns:
            if column in ['passhash', 'token']:  # @TODO IMPROVE ME
                continue
            value = getattr(self, column)
            if value.__class__ == datetime.datetime:
                value = value.isoformat()
            res[column] = value
        return res

    def __repr__(self):
        return '{}({})'.format(self.__class__.__name__, self.columnitems)

    def tojson(self):
        return self.columnitems


class PasswordType(TypeDecorator):
    '''Custom type that will hash plain text password into a sha256 hex string.
    Will also do the corresponding comparison when filtering by it.'''
    impl = String(64)

    def process_bind_param(self, value, dialect):
        return hashlib.sha256(value).hexdigest()

    class comparator_factory(String.comparator_factory):
        def __eq__(self, other):
            local_pw = type_coerce(self.expr, String)
            return local_pw == hashlib.sha256(other).hexdigest()
