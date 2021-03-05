from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views import generic

from .models import Partner


class PartnerListView(PermissionRequiredMixin, generic.ListView):
    model = Partner
    permission_required = "catalog.can_mark_returned"
    paginate_by = 10


class PartnerDetailView(PermissionRequiredMixin, generic.DetailView):
    model = Partner
    permission_required = "catalog.can_mark_returned"


class PartnerCreateView(PermissionRequiredMixin, generic.CreateView):
    model = Partner
    permission_required = "catalog.can_mark_returned"
    template_name = "core/partner_create.html"
    fields = "__all__"


class PartnerUpdateView(PermissionRequiredMixin, generic.UpdateView):
    model = Partner
    permission_required = "catalog.can_mark_returned"
    template_name = "core/partner_create.html"
    fields = "__all__"

    def get_success_url(self):
        return reverse("partners")


class PartnerDeleteView(PermissionRequiredMixin, generic.DeleteView):
    model = Partner
    permission_required = "catalog.can_mark_returned"
    success_url = reverse_lazy("partners")
    template_name_suffix = "_delete_successfull"


@permission_required("catalog.can_mark_returned")
def partner_list(request):
    partners = Partner.objects.all()
    partner_quantity = Partner.objects.count()

    context = {
        "partners": partners,
        "partner_quantity": partner_quantity,
    }

    return render(request, "core/partner_list.html", context=context)
