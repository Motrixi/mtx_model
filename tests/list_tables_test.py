import unittest

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import NoSuchTableError

from src.custom_types import Base
from src.list_tables import ZipList


class TestListTables(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        engine = create_engine('mysql://root@localhost/')
        conn = engine.connect()
        conn.execute('commit')
        conn.execute('DROP DATABASE IF EXISTS tests')
        conn.execute('CREATE DATABASE tests')
        conn.close()

        cls.engine = create_engine('mysql://root@localhost/tests')
        cls.Session = sessionmaker(bind=cls.engine)
        cls.session = cls.Session()

    @classmethod
    def tearDownClass(cls):
        # Close all active transactions
        cls.session.commit()
        Base.metadata.drop_all(cls.engine)

    def test_no_table(self):
        with self.assertRaises(NoSuchTableError):
            ZipList.get('no_table', self.engine)

    def test_create_table(self):
        table = ZipList.create('create_table', self.engine)
        self.assertTrue(self.engine.has_table(table.name))
        table.drop(bind=self.engine)

    def test_create_class(self):
        table = ZipList.create('create_class', self.engine)
        cls = ZipList.get('create_class', self.engine)
        self.assertIsInstance(cls, Base.__class__)
        table.drop(bind=self.engine)


if __name__ == '__main__':
    unittest.main()
