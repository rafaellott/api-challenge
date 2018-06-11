import unittest

from forecast.app import create_app
from forecast.database.models import User


class TestUser(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.app = create_app(mode="Testing")

    def test_controller_add_single_user(self):
        from forecast.api.v1.controllers import add_user
        user_data = {

        }
        result = add_user(user_data)
        self.assertIsInstance(result, User)

    def test_view_add_single_user(self):
        with self.app.app_context():
            pass

    def test_something(self):
        self.assertEqual(True, False)
