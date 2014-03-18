import peewee as pw
import sys

sys.path.append('../../')

import settings

if __name__ == '__main__':
    database = pw.SqliteDatabase('internal.db')
else:
    database = pw.SqliteDatabase(settings.INTERNAL_DB_PATH,
                                 threadlocals=True)

START_ACTION   = 1
UPDATE_ACTION  = 2
STOP_ACTION    = 3
PAUSE_ACTION   = 4
RESUME_ACTION  = 5
ARCHIVE_ACTION = 6

STOPPED_STATE = 0
RUNNING_STATE = 1
ERROR_STATE   = 2

class Agent(pw.Model):
    id                   = pw.BigIntegerField()
    config               = pw.BlobField(null=False)
    date_end             = pw.BigIntegerField(null=False)
    date_start           = pw.BigIntegerField(null=False)
    daily_budget_micros  = pw.BigIntegerField(null=False)
    total_budget_micros  = pw.BigIntegerField(null=False)
    last_budget_run      = pw.BigIntegerField(default=0)
    spent_budget_micros  = pw.BigIntegerField(default=0)
    state                = pw.IntegerField(default=STOPPED_STATE)
    account              = pw.CharField(max_length=40)  
    # TODO impression daily + total ?
    class Meta:
        database = database
        db_table = 'agent'

    def initialize(self, flight, conf_blob):
        self.config              = conf_blob
        self.date_end            = flight.date_end.strftime('%s')
        self.date_start          = flight.date_start.strftime('%s')
        self.account = 'account_%d_%d' % (flight.campaign, flight.id)
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

class Action(pw.Model):
    id                   = pw.BigIntegerField()
    action               = pw.IntegerField(default=0)
    exec_ts              = pw.IntegerField(null=True)
    agent                = pw.BigIntegerField(
                                null=True, db_column='agent_id')
    class Meta:
        database = database
        db_table = 'action'

class Timer(pw.Model):
    id                   = pw.BigIntegerField()
    ts                   = pw.BigIntegerField()
    timer_t              = pw.CharField(max_length=8)
    agent                = pw.BigIntegerField(
                                null=True, db_column='agent_id')
    class Meta:
        database = database
        db_table = 'timer'

class AccountError(pw.Model):
    id                   = pw.BigIntegerField()
    run_time             = pw.BigIntegerField()
    description          = pw.BlobField(null=False)
    agent                = pw.BigIntegerField(
                                null=True, db_column='agent_id')
    class Meta:
        database = database
        db_table = 'account_error'

if __name__ == '__main__':
    Agent.create_table()
    Action.create_table()
    Timer.create_table()
    AccountError.create_table()
