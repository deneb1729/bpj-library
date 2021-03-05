from django.conf.urls import url

from . import views

urlpatterns = [
    url(r"^partners/$", views.partner_list, name="partners"),
    url(
        r"^partner/(?P<pk>\d+)$",
        views.PartnerDetailView.as_view(),
        name="partner_detail",
    ),
    url(
        r"^partner/(?P<pk>\d+)/update/$",
        views.PartnerUpdateView.as_view(),
        name="partner_update",
    ),
    url(
        r"^partner/(?P<pk>\d+)/delete/$",
        views.PartnerDeleteView.as_view(),
        name="partner_delete",
    ),
    url(r"^partner/create/$", views.PartnerCreateView.as_view(), name="partner_create"),
]
