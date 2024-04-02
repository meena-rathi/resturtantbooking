from django import forms
from .models import reservation

class reservationsForms(forms.ModelForm):
    class Meta:
        model = reservation
        Fields = ['email', 'contact_number', 'number_people', 'date', 'time']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }
