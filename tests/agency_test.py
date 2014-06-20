import unittest
import time

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.custom_types import Base
from src.agency import User, Role, Agency


class TestUser(unittest.TestCase):

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

        cls.role = {'name': 'Role Name'}
        cls.agency = {'name': 'Agency Name',
                      'domain': 'Agency Domain',
                      'type': 'Agency Type',
                      'status': 1}

        cls.user = {'email': 'foo@bar.com',
                    'passhash': 'super secret password',
                    'first_name': 'Foo',
                    'last_name': 'Bar',
                    'role_id': 1,
                    'agency_id': 1
                    }

        Base.metadata.create_all(cls.engine)
        cls.session.add(Role(**cls.role))
        cls.session.add(Agency(**cls.agency))
        cls.session.add(User(**cls.user))
        cls.session.commit()

    @classmethod
    def tearDownClass(cls):
        # Close all active transactions
        cls.session.commit()
        Base.metadata.drop_all(cls.engine)

    def test_verify_credentials_test_ok(self):
        # Correct email - Correct Password
        res = User.verify_credentials(self.session, self.user['email'],
                                      self.user['passhash'])
        self.assertTrue(res)

    def test_verify_credentials_wrong_password(self):
        # Correct email - Wrong Password
        res = User.verify_credentials(self.session, self.user['email'],
                                      'some wrong password')
        self.assertFalse(res)

    def test_verify_credentials_wrong_email(self):
        # Wrong email - Correct password
        res = User.verify_credentials(self.session, 'wrongi.foo@bar.com',
                                      self.user['passhash'])
        self.assertFalse(res)

    def test_verify_credentials_wrong_email_wrong_password(self):
        # Wrong email - Wrong password
        res = User.verify_credentials(self.session, 'wrongi.foo@bar.com',
                                      'some wrong password')
        self.assertFalse(res)

    def test_token_correct(self):
        secret = 'secret'
        user = self.session.query(User).get(1)
        user.generate_token(secret, expires=10)
        res = User.verify_token(self.session, secret, user.token)
        self.assertTrue(res)

    def test_token_expired_token(self):
        secret = 'secret'
        user = self.session.query(User).get(1)
        user.generate_token(secret, expires=1)
        time.sleep(2)
        res = User.verify_token(self.session, secret, user.token)
        self.assertFalse(res)

    def test_token_tempered(self):
        secret = 'secret'
        user = self.session.query(User).get(1)
        user.generate_token(secret, expires=1)
        user.token = user.token + 'sadsl13123'
        res = User.verify_token(self.session, secret, user.token)
        self.assertFalse(res)


class TestHiddenColumns(unittest.TestCase):
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

        cls.role = {'name': 'Role Name'}
        cls.agency = {'name': 'Agency Name',
                      'domain': 'Agency Domain',
                      'type': 'Agency Type',
                      'status': 1}

        cls.user = {'email': 'foo@bar.com',
                    'passhash': 'super secret password',
                    'first_name': 'Foo',
                    'last_name': 'Bar',
                    'role_id': 1,
                    'agency_id': 1
                    }

        Base.metadata.create_all(cls.engine)
        cls.session.add(Role(**cls.role))
        cls.session.add(Agency(**cls.agency))
        cls.session.add(User(**cls.user))
        cls.session.commit()

    @classmethod
    def tearDownClass(cls):
        # Close all active transactions
        cls.session.commit()
        Base.metadata.drop_all(cls.engine)

    def test_hidden_columns(self):
        user = self.session.query(User).get(1)
        data = user.todict()
        self.assertNotIn('token', data)
        self.assertNotIn('passhash', data)

    def test_force_show(self):
        user = self.session.query(User).get(1)
        user.hide_columns = []
        data = user.todict()
        self.assertIn('token', data)
        self.assertIn('passhash', data)


if __name__ == '__main__':
    unittest.main()
