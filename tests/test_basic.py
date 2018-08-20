import os
import unittest

from app.config import TestingConfig

os.environ['ENVIROMENT']='testing'
from app import app, db

TEST_DB = 'test.db'

class BasicTests(unittest.TestCase):
     # executed prior to each test
    def setUp(self):
        app.config.from_object(TestingConfig)
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        self.app = app.test_client()
        db.drop_all()
        db.create_all()
 
        self.assertEqual(app.debug, False)
 
    def tearDown(self):
        pass
 
    def test_main_page(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
 
 
if __name__ == "__main__":
    unittest.main()