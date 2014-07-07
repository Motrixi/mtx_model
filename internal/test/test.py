import unittest
import sys
import json
import os

sys.path.append('../../../')

import model.internal as internal
DB_PATH = 'test.db'
DB_LOCACTION = 'sqlite:///%s' % DB_PATH

json_flight = r'''{
    "UTF_offset": 0, 
    "bid_amount": 0.5, 
    "bid_type": {
        "id": 1, 
        "name": "CPM"
    }, 
    "bid_type_id": 1, 
    "brand_id": 1, 
    "budget_daily": 1000.0, 
    "budget_total": 10000.0, 
    "budget_type": {
        "id": 1, 
        "name": "budget"
    }, 
    "budget_type_id": 1, 
    "campaign_id": 1, 
    "category_id": 1, 
    "created": "2014-06-24T00:00:00", 
    "daypart": null, 
    "end_date": "2014-07-14T00:00:00", 
    "id": 2, 
    "impression_daily": 0, 
    "impression_total": 0, 
    "name": "flight_nemi", 
    "pacing_type": {
        "id": 1, 
        "name": "EVEN"
    }, 
    "pacing_type_id": 1, 
    "start_date": "2014-06-24T00:00:00", 
    "state": {
        "id": 1, 
        "name": "PAUSED"
    }, 
    "state_id": 1, 
    "status": {
        "id": 1, 
        "name": "PENDING"
    }, 
    "status_id": 1
}'''

class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        # connect to the db
        engine = create_engine(DB_LOCACTION, echo=False)
        Session = sessionmaker(bind=engine)
        self.lite_session = Session()

    def test_01(self):
        # create an agent based on a json object and save it,
        # query it and check it is still the same
        jf = json.loads(json_flight)
        a = internal.Agent()
        a.initialize(jf, '{}')
        self.assertEqual(a.config, '{}')
        self.assertEqual(a.date_end, 1405306800)
        self.assertEqual(a.date_start, 1403578800)
        self.assertEqual(a.daily_budget_micros, 1000000000)
        self.assertEqual(a.total_budget_micros, 10000000000)
        self.assertEqual(a.account, 'account_1_2')
        self.assertEqual(a.pacing, 'even')
        self.assertEqual(a.budget_type, 'budget')
        self.assertEqual(a.bid_amount, 500000)
        self.assertEqual(a.bid_type, 'CPM')
        self.assertEqual(a.state, None)
        self.lite_session.add(a)
        self.lite_session.commit()

    def test_02(self):
        # read the agent and check it is still the same
        a = self.lite_session.query(internal.Agent).all()[0]
        self.assertEqual(a.config, '{}')
        self.assertEqual(a.date_end, 1405306800)
        self.assertEqual(a.date_start, 1403578800)
        self.assertEqual(a.daily_budget_micros, 1000000000)
        self.assertEqual(a.total_budget_micros, 10000000000)
        self.assertEqual(a.account, 'account_1_2')
        self.assertEqual(a.pacing, 'even')
        self.assertEqual(a.budget_type, 'budget')
        self.assertEqual(a.bid_amount, 500000)
        self.assertEqual(a.bid_type, 'CPM')
        self.assertEqual(a.state, 0)

if __name__ == '__main__':
    
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    os.remove(DB_PATH)
    engine = create_engine(DB_LOCACTION, echo=False)
    internal.Base.metadata.create_all(engine)
    unittest.main()
