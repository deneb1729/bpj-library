from django.contrib import admin

from .models import Author, Book, BookInstance, Genre, Language

admin.site.register(Language)
admin.site.register(Genre)


class BookInline(admin.TabularInline):
    model = Book


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("last_name", "first_name", "date_of_birth", "date_of_death")
    fields = ["last_name", "first_name", ("date_of_birth", "date_of_death")]


class BookInstanceInline(admin.TabularInline):
    model = BookInstance


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "get_authors", "display_genre")
    inlines = [BookInstanceInline]


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ("id", "book", "status", "borrower", "due_back")
    list_filter = ("status", "due_back")

    fieldsets = (
        (
            None,
            {
                "fields": ("id", "book", "imprint"),
            },
        ),
        ("Availability", {"fields": ("status", "due_back", "borrower")}),
    )
