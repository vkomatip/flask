import app
import unittest

class AppTestCase(unittest.TestCase):
    def setUp(self):
        app.app.testing = True
        self.app = app.app.test_client()

    def test_index(self):
        result = self.app.get('/')
        self.assertEqual(result.status_code, 200)
        self.assertEqual(result.data.decode('utf-8'), 'Hello, world!')

if __name__ == '__main__':
    unittest.main()
