from django.test import SimpleTestCase
from django.urls import resolve, reverse

from catalog import views


class TestBookUrls(SimpleTestCase):
    def test_index_url_resolves(self):
        url = reverse("index")
        self.assertEqual(resolve(url).func, views.index)

    def test_book_list_url_resolves(self):
        url = reverse("books")
        self.assertEqual(resolve(url).func.view_class, views.BookListView)

    def test_renew_book_url_resolves(self):
        url = reverse("renew_book_librarian", args=["1"])
        self.assertEqual(resolve(url).func, views.renew_book_librarian)

    def test_book_create_url_resolves(self):
        url = reverse("book_create")
        self.assertEqual(resolve(url).func.view_class, views.BookCreateView)


class TestAuthorUrls(SimpleTestCase):
    def test_author_list_url_resolves(self):
        url = reverse("authors")

        self.assertEqual(resolve(url).func.view_class, views.AuthorListView)
