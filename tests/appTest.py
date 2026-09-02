import unittest

from app.app import app


class AppTest(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_print_health_check(self):
        response = self.app.get("/health-check")
        self.assertEqual(200, response.status_code)
        self.assertEqual({"status": "ok"}, response.get_json())

    def test_print_hello_error(self):
        response = self.app.get("/hello")
        self.assertEqual(400, response.status_code)
        self.assertEqual({"error": "Name is required"}, response.get_json())

    def test_print_hello_success(self):
        response = self.app.get("/hello?name=Victor")
        self.assertEqual(200, response.status_code)
        self.assertEqual({"message": "Hello, Victor!"}, response.get_json())


if __name__ == "__main__":
    unittest.main()
