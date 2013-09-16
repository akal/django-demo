from django.forms import ModelForm
from contactform.models import ContactRequest


class ContactRequestForm(ModelForm):
    class Meta:
        model = ContactRequest

