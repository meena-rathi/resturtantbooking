
from django import forms
from .models import Reservation
from datetime import date
import re

class ReservationsForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['email', 'contact_number', 'number_people', 'date', 'time']
        widgets = {
            # 'user': forms.TextInput(attrs={'readonly': True, 'style': 'text-transform: uppercase;'}),
            'date': forms.DateInput(attrs={'type': 'date' , 'id': 'id_date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
            'number_people': forms.TextInput(attrs={}),
            'contact_number': forms.TextInput(attrs={'id': 'id_contact_number'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['date'].initial = date.today() 
        #self.initial['date'] = date.today()
    def clean_contact_number(self):
        contact_number = self.cleaned_data.get('contact_number')
        contact_number_pattern = re.compile(r'^\+?\d{10,15}$')

        if not contact_number:
            raise forms.ValidationError("Contact number is required.")
        
        if ' ' in contact_number:
            raise forms.ValidationError("Spaces are not allowed contact number.")

        if not contact_number_pattern.match(contact_number):
            raise forms.ValidationError("Invalid contact number format. Contact number can only contain digits and an optional '+' sign, and must be between 10 to 15 digits.")

        return contact_number

    def clean_email(self):
        email = self.cleaned_data.get('email')
        email_pattern = re.compile(r'^[^\s@]+@[^\s@]+\.[^\s@]+$')
        allowed_domains = ['gmail.com', 'yahoo.com', 'hotmail.com']  # Add allowed domains here

        if not email_pattern.match(email):
            raise forms.ValidationError("Invalid email format.")

        domain = email.split('@')[1]
        if domain.lower() not in allowed_domains:
            raise forms.ValidationError(f"Email domain must be one of the following: {', '.join(allowed_domains)}")
        return email