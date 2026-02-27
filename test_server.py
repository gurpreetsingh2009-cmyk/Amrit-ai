import unittest
from server import app  # import the Flask app from your server module

class ServerTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = app.test_client()  # Create a test client for your Flask app
        cls.app.testing = True  # Enable testing mode

    def test_home_status_code(self):
        """Test the home page status code."""
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_home_content(self):
        """Test the content of the home page."""
        response = self.app.get('/')
        self.assertIn(b"Welcome", response.data)  # Assuming "Welcome" is a word in the home content

    def test_example_endpoint(self):
        """Test a specific endpoint."""
        response = self.app.get('/example')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'message': 'This is an example'})

    # Add more tests for other endpoints and functionalities as needed

if __name__ == '__main__':
    unittest.main()