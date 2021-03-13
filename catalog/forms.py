import datetime

from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

from .models import Author


class RenewBookForm(forms.Form):
    renewal_date = forms.DateField(
        help_text="Enter a date between now and 3 weeks (default 2)."
    )

    def clean_renewal_date(self):
        data = self.cleaned_data["renewal_date"]

        if data < datetime.date.today():
            raise ValidationError(_("Invalid date - renewal in past"))

        if data > datetime.date.today() + datetime.timedelta(weeks=3):
            raise ValidationError(_("Invalid date - renewal more than 3 weeks ahead"))

        help_texts = {
            "due_back": _("Enter a date between now and 3 weeks (default 2)."),
        }


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = "__all__"
        widgets = {
            "date_of_birth": forms.DateInput(
                format=("%Y-%m-%d"), attrs={"type": "date"}
            ),
            "date_of_death": forms.DateInput(
                format=("%Y-%m-%d"), attrs={"type": "date"}
            ),
        }
