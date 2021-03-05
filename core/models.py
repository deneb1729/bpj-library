from django.core.validators import RegexValidator
from django.db import models
from django.urls import reverse


class Partner(models.Model):

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(
        auto_now=False, auto_now_add=False, null=True, blank=True
    )
    identification_number = models.CharField(
        max_length=8,
        validators=[
            RegexValidator(
                r"^\d{7,8}$", "DNI invalido, debe tener entre 7 y 8 dígitos."
            )
        ],
    )
    phone = models.CharField(max_length=15, null=True, blank=True)
    email = models.EmailField(max_length=254, null=True, blank=True)

    class Meta:
        verbose_name = "partner"
        verbose_name_plural = "partners"

    def __str__(self):
        return "{0}, {1}".format(self.last_name, self.first_name)

    def get_absolute_url(self):
        return reverse("partner_detail", args=[str(self.id)])
