from django import forms
from django.forms.widgets import DateTimeInput
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

# from mapwidgets.widgets import GooglePointFieldWidget

from .models import Event


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ["title", "details", "category", "location", "datetime", "image"]
        widgets = {
            # "location": GooglePointFieldWidget,
            "datetime": DateTimeInput(attrs={"type": "datetime-local"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit("submit", "Save"))
