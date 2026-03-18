from django.test import TestCase


class SimpleTests(TestCase):
    def test_home_status(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
