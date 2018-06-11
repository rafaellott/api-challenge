import unittest

from forecast import create_app
from forecast.api.v1.controllers import add_user
from forecast.database.models import User


class TestUser(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.app = create_app(mode="Testing")
        self.client = self.app.test_client()

    def test_controller_add_single_user_raise_error(self):
        with self.assertRaises(AttributeError):
            add_user({})

    def test_list_users(self):
        result = self.client.get('/api/users/')
        keys = {'items', 'page', 'pages', 'per_page', 'total'}
        self.assertSetEqual(set(result.json.keys()), keys)

    def test_view_add_single_user(self):
        result = self.client.post('/api/users/', json={'name': 'test user'})
        self.assertEqual(201, result.status_code)

    def test_view_delete_user(self):
        # Get a single user
        user_result = self.client.get('/api/users/')
        user = user_result.json['items'][0]

        result = self.client.delete(
            '/api/users/{user_id}'.format(user_id=user['id'])
        )
        self.assertEqual(204, result.status_code)
