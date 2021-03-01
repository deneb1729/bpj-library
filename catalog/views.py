import datetime

from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.views import generic

from .forms import RenewBookForm
from .models import Author, Book, BookInstance, Genre


def index(request):
    num_books = Book.objects.count()
    num_instances = BookInstance.objects.count()
    num_instances_available = BookInstance.objects.filter(status__exact="a").count()
    num_authors = Author.objects.count()
    num_genres = Genre.objects.count()
    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "num_books": num_books,
        "num_instances": num_instances,
        "num_instances_available": num_instances_available,
        "num_authors": num_authors,
        "num_genres": num_genres,
        "num_visits": num_visits,
    }

    return render(request, "index.html", context=context)


class BookListView(generic.ListView):
    model = Book
    paginate_by = 2


class BookDetailView(generic.DetailView):
    model = Book


class AuthorListView(generic.ListView):
    model = Author


class AuthorDetailView(generic.DetailView):
    model = Author


class LoanedBooksByUserListView(LoginRequiredMixin, generic.ListView):
    model = BookInstance
    template_name = "catalog/bookinstance_list_borrowed_user.html"
    paginate_by = 10

    def get_queryset(self):
        return (
            BookInstance.objects.filter(borrower=self.request.user)
            .filter(status__exact="o")
            .order_by("due_back")
        )


class BorrowedBooksListView(PermissionRequiredMixin, generic.ListView):
    model = BookInstance
    template_name = "catalog/bookinstance_list_borrowed_all.html"
    paginate_by = 2
    permission_required = "catalog.can_mark_returned"

    def get_queryset(self):
        return BookInstance.objects.filter(status__exact="o").order_by("due_back")


@permission_required("catalog.can_mark_returned")
def renew_book_librarian(request, pk):
    book_inst = get_object_or_404(BookInstance, pk=pk)

    if request.method == "POST":
        form = RenewBookForm(request.POST)

        if form.is_valid():
            book_inst.due_back = form.cleaned_data["renewal_date"]
            book_inst.save()

            return HttpResponseRedirect(reverse("all_borrowed"))

    elif request.method == "GET":
        proposed_renewal_date = datetime.date.today() + datetime.timedelta(weeks=2)
        form = RenewBookForm(
            initial={
                "renewal_date": proposed_renewal_date,
            }
        )

    return render(
        request,
        "catalog/book_renew_librarian.html",
        {"form": form, "bookinst": book_inst},
    )


class AuthorCreateView(PermissionRequiredMixin, generic.CreateView):
    model = Author
    permission_required = "catalog.can_mark_returned"
    fields = "__all__"


class AuthorUpdateView(PermissionRequiredMixin, generic.UpdateView):
    model = Author
    permission_required = "catalog.can_mark_returned"
    fields = ["first_name", "last_name", "date_of_birth", "date_of_death"]


class AuthorDeleteView(PermissionRequiredMixin, generic.DeleteView):
    model = Author
    permission_required = "catalog.can_mark_returned"
    success_url = reverse_lazy("authors")
    template_name_suffix = "_delete_successfull"


class BookCreateView(PermissionRequiredMixin, generic.CreateView):
    model = Book
    permission_required = "catalog.can_mark_returned"
    fields = "__all__"


class BookUpdateView(PermissionRequiredMixin, generic.UpdateView):
    model = Book
    permission_required = "catalog.can_mark_returned"
    fields = "__all__"


class BookDeleteView(PermissionRequiredMixin, generic.DeleteView):
    model = Book
    permission_required = "catalog.can_mark_returned"
    success_url = reverse_lazy("books")
    template_name_suffix = "_delete_successfull"
