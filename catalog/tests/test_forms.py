import datetime

from django.test import SimpleTestCase

from catalog.forms import RenewBookForm


class TestForms(SimpleTestCase):
    def test_renew_book_form_valid_data(self):
        valid_date = datetime.date.today() + datetime.timedelta(weeks=1)
        form = RenewBookForm(data={"renewal_date": valid_date})

        self.assertTrue(form.is_valid())

    def test_form_no_data(self):
        form = RenewBookForm(data={})

        self.assertFalse(form.is_valid())
