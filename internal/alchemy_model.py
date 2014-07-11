from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, BigInteger, Text,\
                       Time, DATETIME, Boolean
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, backref
import sys
import datetime

sys.path.append('../../')

import settings

START_ACTION   = 1
UPDATE_ACTION  = 2
STOP_ACTION    = 3
PAUSE_ACTION   = 4
RESUME_ACTION  = 5
ARCHIVE_ACTION = 6

STOPPED_STATE = 0
RUNNING_STATE = 1
ERROR_STATE   = 2

Base = declarative_base()

class Agent(Base):
    __tablename__ = 'agent'
    id                   = Column(Integer, primary_key=True, autoincrement=True)
    config               = Column(Text,         nullable=False)
    date_end             = Column(BigInteger,   nullable=False)
    date_start           = Column(BigInteger,   nullable=False)
    daily_budget_micros  = Column(BigInteger,   nullable=False)
    total_budget_micros  = Column(BigInteger,   nullable=False)
    last_imp_run         = Column(BigInteger,   nullable=False, default=0)
    last_budget_run      = Column(BigInteger,   nullable=False, default=0)
    spent_budget_micros  = Column(BigInteger,   nullable=False, default=0)
    state                = Column(Integer,      nullable=False, default=STOPPED_STATE)
    account              = Column(String,       nullable=False)
    pacing               = Column(String,       nullable=False, default='asap')
    probability          = Column(Float(precision=3), nullable=False, default='0')
    budget_type          = Column(String(length=25),  nullable=False)
    impression_daily     = Column(BigInteger,         nullable=False, default=0)
    impression_total     = Column(BigInteger,         nullable=False, default=0)
    bid_amount           = Column(BigInteger,         nullable=False, default=0)
    bid_type             = Column(String(length=5),   nullable=False, default='CPM')
    is_capped            = Column(Boolean,            nullable=False, default=False)

    def initialize(self, flight, conf_blob):
        self.account = 'account_%d_%d' % (flight['campaign_id'], flight['id'])
        self.config              = conf_blob
        self.date_end            = int(datetime.datetime.strptime(
                                        flight['end_date'], '%Y-%m-%dT%H:%M:%S').strftime('%s'))
        self.date_start          = int(datetime.datetime.strptime(
                                        flight['start_date'], '%Y-%m-%dT%H:%M:%S').strftime('%s'))
        self.budget_type         = flight['budget_type']['name']
        self.impression_daily    = flight['impression_daily']
        self.impression_total    = flight['impression_total']
        self.bid_amount          = flight['bid_amount'] * 1000000
        self.bid_type            = flight['bid_type']['name']

        if not flight['pacing_type']:
            self.pacing = 'asap'
        else:
            self.pacing = flight['pacing_type']['name'].lower()

        if not flight['budget_daily']:
            self.daily_budget_micros = 0
        else:
            self.daily_budget_micros = \
                int('%.0f' % (flight['budget_daily'] * 1000000))
        if not flight['budget_total']:
            self.total_budget_micros = 0
        else:
            self.total_budget_micros = \
                int('%.0f' % (flight['budget_total'] * 1000000))
        if self.budget_type == 'impression':
            self.daily_budget_micros = int(
                self.bid_amount * self.impression_daily / 1000)
            delta = self.date_end - self.date_start
            self.total_budget_micros = self.daily_budget_micros * delta.days
        else :
            self.probability = 0.5
        if not self.impression_daily:
            self.impression_daily = 0
        if not self.impression_total:
            self.impression_total = 0

class Action(Base):
    __tablename__ = 'action'
    id                   = Column(Integer, primary_key=True, autoincrement=True)
    action               = Column(Integer,      nullable=False, default=0)
    exec_ts              = Column(Integer,      nullable=True)

    agent_id             = Column(Integer, ForeignKey('agent.id'))
    agent                = relationship("Agent", 
                                backref=backref('actions', order_by=id))


class Timer(Base):
    __tablename__ = 'timer'
    id                   = Column(Integer, primary_key=True, autoincrement=True)
    ts                   = Column(BigInteger,   nullable=False)
    timer_t              = Column(String,   nullable=False)

    agent_id             = Column(Integer, ForeignKey('agent.id'))
    agent                = relationship("Agent", 
                                backref=backref('timers', order_by=id))

class AccountError(Base):
    __tablename__ = 'account_error'
    id                   = Column(Integer, primary_key=True, autoincrement=True)
    run_time             = Column(BigInteger,   nullable=False)
    description          = Column(Text,         nullable=False)

    agent_id             = Column(Integer, ForeignKey('agent.id'))
    agent                = relationship("Agent", 
                                backref=backref('errors', order_by=id))


if __name__ == '__main__':
    
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    engine = create_engine(
                'sqlite:///%s' % settings.INTERNAL_DB_PATH, echo=True)
    Base.metadata.create_all(engine) 
