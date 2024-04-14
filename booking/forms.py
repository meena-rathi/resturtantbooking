from django import forms
from .models import Reservation

class ReservationsForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['name','email', 'contact_number', 'number_people', 'date', 'time']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
        }
