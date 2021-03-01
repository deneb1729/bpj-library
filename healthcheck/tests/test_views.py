from django.test import Client, TestCase


class TestHealtcheckViews(TestCase):
    def setUp(self):
        self.client = Client()

    def test_health_GET(self):
        response = self.client.get("/health/")
        self.assertEqual(response.status_code, 200)
