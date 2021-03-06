'''
Created on 05/05/2014

@author: pablin
'''
from contextlib import contextmanager

@contextmanager
def SessionCommiter(SessionFactory):
    """Provide a transactional scope around a series of operations.The 
    SessionFactory must be a class constructed from a sessionmaker.
    After it goes out of scope it commit the transactions (or rollback 
    if can not commit (error))."""
    
    session = SessionFactory()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()


@contextmanager
def SessionCloser(SessionFactory):
    """ SessionFactory must be a class constructed from a sessionmaker.
    After it goes out of scope it close session."""
    
    session = SessionFactory()
    try:
        yield session
    except:
        session.rollback()
        raise
    finally:
        session.close()
