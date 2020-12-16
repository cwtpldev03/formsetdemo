from django import forms
from django.forms import (formset_factory, modelformset_factory)
from .models import PressureFormat, Certificate

class PressureForm(forms.ModelForm):
    class Meta:
        model = PressureFormat
        fields = '__all__'
        labels = {
            'name': 'Book Name'
        }
        



PressureFormset = modelformset_factory(
    PressureFormat,
    fields= '__all__',
    extra=1,
    
)



