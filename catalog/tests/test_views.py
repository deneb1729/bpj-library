import datetime

from django.contrib.auth.models import Permission, User
from django.test import Client, TransactionTestCase
from django.urls import reverse

from catalog.models import Author


class TestAuthorViews(TransactionTestCase):
    reset_sequences = True

    def setUp(self):
        self.client = Client()
        self.author_list = reverse("authors")
        self.author_create = reverse("author_create")
        self.author_update = reverse("author_update", args=["1"])
        self.author_delete = reverse("author_delete", args=["1"])
        user1 = User.objects.create_user(username="john", password="123456")
        user1.save()
        permission = Permission.objects.get(name="Set book as returned")
        user1.user_permissions.add(permission)
        user1.save()

    def test_author_list_GET(self):
        response = self.client.get(self.author_list)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "catalog/author_list.html")

    def test_author_GET_create_no_authorized(self):
        response = self.client.get(self.author_create)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, "/accounts/login/?next=/catalog/author/create/")

    def test_author_GET_update_no_authorized(self):
        response = self.client.get(self.author_update)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response, "/accounts/login/?next=/catalog/author/1/update/"
        )

    def test_author_GET_delete_no_authorized(self):
        response = self.client.get(self.author_delete)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response, "/accounts/login/?next=/catalog/author/1/delete/"
        )

    def test_author_POST_create_author(self):
        login = self.client.login(username="john", password="123456")
        response = self.client.post(
            self.author_create,
            {
                "first_name": "Jorge Luis",
                "last_name": "Borges",
                "date_of_birth": datetime.date(1896, 8, 24),
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, "/catalog/author/1")

        author1 = Author.objects.first()
        self.assertEquals(author1.first_name, "Jorge Luis")
        self.assertEquals(Author.objects.count(), 1)
