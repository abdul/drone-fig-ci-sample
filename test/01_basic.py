# encoding:utf-8
import unittest

import flask
from app  import app

# vars

class TestAuth(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_hello(self):
        rv = self.app.get('/')
        self.assertIn('Hello', rv.data)
        self.assertEqual(rv.status_code, 200)

if __name__ == '__main__':
    unittest.main()
