import datetime

from django.contrib.auth.models import User
from django.test import TestCase

from catalog.models import Author, Book, BookInstance, Genre, Language


class TestBasicModels(TestCase):
    def setUp(self):
        self.genre1 = Genre.objects.create(name="Literatura Francesa")
        self.language1 = Language.objects.create(name="Ingles")

    def test_str_method(self):
        self.assertEquals(str(self.genre1), "LITERATURA FRANCESA")
        self.assertEquals(str(self.language1), "INGLES")


class TestAuthorModel(TestCase):
    @classmethod
    def setUpTestData(cls):
        Author.objects.create(
            first_name="john",
            last_name="doe",
        )

    def test_author_methods(self):
        author = Author.objects.first()
        self.assertEquals(str(author), "DOE, JOHN")
        self.assertEquals(author.get_absolute_url(), "/catalog/author/1")


class TestBookModel(TestCase):
    @classmethod
    def setUpTestData(self):
        genre1 = Genre.objects.create(name="Literatura Francesa")
        language1 = Language.objects.create(name="Ingles")
        author1 = Author.objects.create(
            first_name="john",
            last_name="doe",
        )
        book1 = Book.objects.create(
            title="My book",
            author=author1,
            summary="This is a summary",
            isbn="123456",
            language=language1,
        )
        book1.genre.set(Genre.objects.all())

    def test_book_methods(self):
        book = Book.objects.first()
        self.assertEquals(str(book), "MY BOOK")
        self.assertEquals(book.get_absolute_url(), "/catalog/book/1")
        self.assertEquals(book.display_genre(), "Literatura Francesa")

    def test_book_instance_methods(self):
        book1 = Book.objects.first()
        user1 = User.objects.create_user(username="john", password="123456")
        bookinst1 = BookInstance.objects.create(
            book=book1,
            imprint="second edition",
            due_back=(datetime.date.today() + datetime.timedelta(weeks=2)),
            status="o",
            borrower=user1,
        )

        self.assertEquals(bookinst1.get_status_display(), "On Load")
        self.assertTrue("My book" in str(bookinst1))
        self.assertFalse(bookinst1.is_overdue)
