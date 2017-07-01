from django import forms
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from test_assignment.models import Person

class EditPersonForm(forms.ModelForm):

    class Meta:
        model   = Person
        fields  = '__all__'

        