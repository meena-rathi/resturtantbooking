
from django import forms
from .models import Reservation
from datetime import date
import re
from allauth.account.forms import SignupForm

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
        allowed_domains = ['gmail.com', 'yahoo.com', 'hotmail.com']

        if not email_pattern.match(email):
            raise forms.ValidationError("Invalid email format.")

        domain = email.split('@')[1]
        if domain.lower() not in allowed_domains:
            raise forms.ValidationError(f"Email domain must be one of the following: {', '.join(allowed_domains)}")
        return email

    def clean(self):
        cleaned_data = super().clean()
        date_selected = cleaned_data.get('date')
        current_date = date.today()

        if date_selected is None:
            raise forms.ValidationError("Date is required")

        if date_selected < current_date:
            raise forms.ValidationError("The date cannot be in the past")

        return cleaned_data


class CustomSignupForm(SignupForm):
    """
    Extends the allauth signup form with additional fields.
    """
    username = forms.CharField(max_length=50, required=True, label='Username')
    email = forms.EmailField(max_length=50, required=True, label='Email')

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.username = self.cleaned_data['username']
        user.email = self.cleaned_data['email']

        user.save()
        return user