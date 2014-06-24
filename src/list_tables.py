from sqlalchemy import Table, Column, MetaData, Integer, String, Float
from sqlalchemy.exc import NoSuchTableError

from custom_types import Base


class BaseList(object):
    instances = {}
    columns = []

    @classmethod
    def create(cls, name, engine):
        '''Creates table based on subclass column definition'''
        if not cls.columns:
            raise NotImplementedError('Column definition list is required')
        new_name = '%s_%s' % (cls.__name__.lower(), str(name).lower())

        columns = []
        for each in cls.columns:
            column = Column(each['name'], each['type'], **each['params'])
            columns.append(column)

        obj = Table(new_name, MetaData(), *columns)
        obj.create(bind=engine)
        return obj

    @classmethod
    def get(cls, name, engine):
        '''Returns the class for the table that should be queried'''
        if not cls.columns:
            raise NotImplementedError('Column definition list is required')
        class_name = '%s_%s' % (cls.__name__, name)
        if class_name not in cls.instances:
            table_name = '%s_%s' % (cls.__name__.lower(), str(name).lower())
            if not engine.has_table(table_name):
                raise NoSuchTableError("Table %s doesn't exist, call create "
                                       "first." % (table_name,))
            columns = {'__tablename__': table_name}
            for each in cls.columns:
                columns[each['name']] = Column(each['type'], **each['params'])
            cls.instances[class_name] = type(class_name, (Base, ), columns)
        return cls.instances[class_name]


class ZipList(BaseList):
    columns = [
        {'name': 'id',
         'type': Integer,
         'params': {'primary_key': True, 'autoincrement': True}
         },
        {'name': 'zip_code',
         'type': Integer,
         'params': {'nullable': False, 'unique': True}
         }
        ]


class CoordList(BaseList):
    columns = [
        {'name': 'id',
         'type': Integer,
         'params': {'primary_key': True, 'autoincrement': True}
         },
        {'name': 'lat',
         'type': Float,
         'params': {'nullable': False}
         },
        {'name': 'lon',
         'type': Float,
         'params': {'nullable': False}
         },
        {'name': 'radius',
         'type': Float,
         'params': {'nullable': False}
         }
        ]


class SiteBlockList(BaseList):
    columns = [
        {'name': 'id',
         'type': Integer,
         'params': {'primary_key': True, 'autoincrement': True}
         },
        {'name': 'site_id',
         'type': String(length=45),
         'params': {'nullable': False, 'unique': True}
         }
        ]


class SiteAllowList(BaseList):
    columns = [
        {'name': 'id',
         'type': Integer,
         'params': {'primary_key': True, 'autoincrement': True}
         },
        {'name': 'site_id',
         'type': String(length=45),
         'params': {'nullable': False, 'unique': True}
         }
        ]


if __name__ == '__main__':
    import random

    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    engine = create_engine('sqlite:///aaaa.db', echo=False)
    Session = sessionmaker(bind=engine)
    session = Session()

    brands = [1, 2, 3]

    for each in brands:
        ZipList.create(each, engine)
        cls = ZipList.get(each, engine)
        [session.add(cls(zip_code=random.randint(1000, 9999))) for x in
            range(5)]

    session.commit()

    import pprint
    for each in brands:
        cls = ZipList.get(each, engine)
        all_ = session.query(cls).all()
        pprint.pprint(all_)

    SiteBlockList.create('1', engine)
    cls = SiteBlockList.get('1', engine)
    session.add(cls(site_id=1234))
    session.commit()

    pprint.pprint(session.query(cls).all())

    SiteAllowList.create('1', engine)
    #CoordList.create('1', engine)
    cls = CoordList.get('1', engine)

    import ipdb;ipdb.set_trace()
    print '-' * 10
    pprint.pprint(BaseList.instances)
