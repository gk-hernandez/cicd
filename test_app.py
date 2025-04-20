import unittest
import json
from app import app

class TestGreetingService(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_greet_endpoint(self):
        response = self.app.get('/greet')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data['message'], "Hello from the greeting microservice!")

if __name__ == '__main__':
    unittest.main()
