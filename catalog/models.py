import uuid
from datetime import date

from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Genre(models.Model):

    name = models.CharField(
        max_length=200, help_text="Ingrese un nombre de género (ej.: Ciencia Ficción):"
    )

    class Meta:
        verbose_name = "genre"
        verbose_name_plural = "genres"

    def __str__(self):
        return self.name.upper()


class Book(models.Model):

    title = models.CharField(max_length=200)
    author = models.ForeignKey("Author", on_delete=models.SET_NULL, null=True)
    summary = models.TextField(
        max_length=1000, help_text="Ingrese una breve descripción del libro:"
    )
    isbn = models.CharField(
        "ISBN",
        max_length=13,
        help_text="13 Caracteres <a href='https://www.isbn-international.org/content/what-isbn'>ISBN number</a>",
    )
    genre = models.ManyToManyField(
        "Genre", help_text="Seleccione un género para este libro:"
    )
    language = models.ForeignKey("Language", on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = "book"
        verbose_name_plural = "books"

    def display_genre(self):
        return ", ".join([genre.name for genre in self.genre.all()[:3]])

    display_genre.short_description = "Genre"

    def __str__(self):
        return self.title.upper()

    def get_absolute_url(self):
        return reverse("book_detail", args=[str(self.id)])


class BookInstance(models.Model):

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        help_text="ID único para este libro particular en toda la biblioteca",
    )
    book = models.ForeignKey("Book", on_delete=models.SET_NULL, null=True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)

    LOAN_STATUS = (
        ("m", "Maintenance"),
        ("o", "On Load"),
        ("a", "Available"),
        ("r", "Reserved"),
    )

    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default="m",
        help_text="Disponibilidad del libro",
    )
    borrower = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name = "bookinstance"
        verbose_name_plural = "bookinstances"
        ordering = ["due_back"]
        permissions = (("can_mark_returned", "Set book as returned"),)

    def __str__(self):
        return "{0} ({1})".format(self.id, self.book.title)

    @property
    def is_overdue(self):
        if self.due_back and date.today() > self.due_back:
            return True
        return False


class Author(models.Model):

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField("Died", null=True, blank=True)

    class Meta:
        verbose_name = "author"
        verbose_name_plural = "authors"
        ordering = ["last_name"]

    def __str__(self):
        return "{0}, {1}".format(self.last_name, self.first_name).upper()

    def get_absolute_url(self):
        return reverse("author_detail", args=[str(self.id)])


class Language(models.Model):

    name = models.CharField(
        max_length=50, help_text="Ingrese un lenguaje natural para un libro:"
    )

    class Meta:
        verbose_name = "language"
        verbose_name_plural = "languages"

    def __str__(self):
        return self.name.upper()
