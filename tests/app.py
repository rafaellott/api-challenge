import unittest


class TestUser(unittest.TestCase):

    def setUp(self):
        pass

    def test_add_single_user(self):
        from forecast.api.v1.controllers import add_user
        user_data = {

        }
        result = add_user(user_data)



    def test_something(self):
        self.assertEqual(True, False)
