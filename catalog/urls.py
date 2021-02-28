from django.conf.urls import url

from . import views

urlpatterns = [
    url(r"^$", views.index, name="index"),
    url(r"^authors/$", views.AuthorListView.as_view(), name="authors"),
    url(r"^author/create/$", views.AuthorCreateView.as_view(), name="author_create"),
    url(
        r"^author/(?P<pk>\d+)$", views.AuthorDetailView.as_view(), name="author_detail"
    ),
    url(
        r"^author/(?P<pk>\d+)/update/$",
        views.AuthorUpdateView.as_view(),
        name="author_update",
    ),
    url(
        r"^author/(?P<pk>\d+)/delete/$",
        views.AuthorDeleteView.as_view(),
        name="author_delete",
    ),
    url(r"^books/$", views.BookListView.as_view(), name="books"),
    url(r"^book/create/$", views.BookCreateView.as_view(), name="book_create"),
    url(r"^book/(?P<pk>\d+)$", views.BookDetailView.as_view(), name="book_detail"),
    url(
        r"^book/(?P<pk>\d+)/update/$",
        views.BookUpdateView.as_view(),
        name="book_update",
    ),
    url(
        r"^book/(?P<pk>\d+)/delete/$",
        views.BookDeleteView.as_view(),
        name="book_delete",
    ),
    url(
        r"^book/(?P<pk>[-\w]+)/renew/$",
        views.renew_book_librarian,
        name="renew_book_librarian",
    ),
    url(r"^borrowed/$", views.BorrowedBooksListView.as_view(), name="all_borrowed"),
    url(r"^mybooks/$", views.LoanedBooksByUserListView.as_view(), name="my_borrowed"),
]
