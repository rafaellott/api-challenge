import unittest


class TestApp(unittest.TestCase):

    def test_create_app(self):
        from forecast import create_app
        create_app()
