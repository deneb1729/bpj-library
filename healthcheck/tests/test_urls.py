from django.test import SimpleTestCase
from django.urls import resolve, reverse
from healthcheck import views


class TestHealthcheckUrls(SimpleTestCase):
    def test_health_url_resolve(self):
        url = reverse("health")
        self.assertEqual(resolve(url).func, views.health)
