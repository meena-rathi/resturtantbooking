
from django import forms
from .models import Reservation
from datetime import date

class ReservationsForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['user', 'email', 'contact_number', 'number_people', 'date', 'time']
        widgets = {
            'user': forms.TextInput(attrs={'readonly': True, 'style': 'text-transform: uppercase;'}),
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
            'number_people': forms.TextInput(attrs={}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initial['date'] = date.today()
        
