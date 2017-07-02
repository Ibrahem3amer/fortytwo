from django import forms
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from test_assignment.models import Person
from test_assignment.validators import EditPersonValidator

class EditPersonForm(forms.ModelForm):

    class Meta:
        model       = Person
        fields      = '__all__'
    
    def clean_birth_date(self):
        """
        Validates birth_date field by calling birth_date_validator
        """
        EditPersonValidator.validate_birth_date(self.cleaned_data['birth_date'])
        return self.cleaned_data['birth_date']
        

        