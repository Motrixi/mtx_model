from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, BigInteger, Text,\
                       Time, DATETIME, Boolean
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, backref
import sys

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
    last_budget_run      = Column(BigInteger,   nullable=False, default=0)
    spent_budget_micros  = Column(BigInteger,   nullable=False, default=0)
    state                = Column(Integer,      nullable=False, default=STOPPED_STATE)
    account              = Column(String,       nullable=False)
    # TODO impression daily + total ?

    def initialize(self, flight, conf_blob):
        self.config              = conf_blob
        self.date_end            = flight.date_end.strftime('%s')
        self.date_start          = flight.date_start.strftime('%s')
        self.account = 'account_%d_%d' % (flight.campaign.id, flight.id)
        if not flight.budget_daily:
            self.daily_budget_micros = 0
        else:
            self.daily_budget_micros = \
                int('%.0f' % (flight.budget_daily * 1000000))
        if not flight.budget_total:
            self.total_budget_micros = 0
        else:
            self.total_budget_micros = \
                int('%.0f' % (flight.budget_total * 1000000))

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
    pass
