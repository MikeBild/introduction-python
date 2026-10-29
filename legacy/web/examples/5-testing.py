from app import app
import unittest

class FlaskAppTests(unittest.TestCase):
  def setUp(self):
    self.app = app.test_client()
    self.app.testing = True

  def test_home_status_code(self):
    result = self.app.get('/')
    self.assertEqual(result.status_code, 202)

  def test_home_data(self):
    result = self.app.get('/')
    self.assertEqual( b'Hello World!', result.data)

if __name__ == "__main__":
  unittest.main()