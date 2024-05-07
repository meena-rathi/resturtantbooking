
from django import forms
from .models import Reservation
from datetime import date

class ReservationsForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['email', 'contact_number', 'number_people', 'date', 'time']
        widgets = {
            # 'user': forms.TextInput(attrs={'readonly': True, 'style': 'text-transform: uppercase;'}),
            'date': forms.DateInput(attrs={'type': 'date' , 'id': 'id_date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
            'number_people': forms.TextInput(attrs={}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['date'].initial = date.today() 
        #self.initial['date'] = date.today()

    # def clean_date(self):
    #     date = self.cleaned_data.get('date')
    #     if date < date.today():
    #         raise forms.ValidationError("Date cannot be in the past.")
    #     return date

    def clean_contact_number(self):
        contact_number = self.cleaned_data.get('contact_number')
    
    # Check for spaces before or after the contact number
        if contact_number.strip() != contact_number:
             raise forms.ValidationError("Spaces before or after the contact number are not allowed.")

    # Remove spaces from before and after the contact number
        contact_number_stripped = contact_number.strip()

    # Check if the contact number consists only of digits
        if not contact_number_stripped.replace(" ", "").isdigit():
            raise forms.ValidationError("Contact number must contain only digits.")

    # Check if the contact number is empty
        if not contact_number_stripped:
            raise forms.ValidationError("Contact number cannot be empty.")

    # Check if the contact number is the string "either"
        if contact_number_stripped.lower() == "either":
            raise forms.ValidationError("String 'either' is not allowed.")

        return contact_number
 
# from django import forms
# from .models import Reservation
# from django.contrib.auth.models import User

# class ReservationsForm(forms.ModelForm):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         if self.instance and self.instance.user:
#             self.fields['user'].initial = self.instance.user.username
#         else:
#             self.fields['user'].initial = self.initial.get('user', '')

        
#         self.fields['user'].widget = forms.TextInput(attrs={'readonly': True, 'value': self.fields['user'].initial})

#     class Meta:
#         model = Reservation
#         fields = ['user', 'email', 'contact_number', 'number_people', 'date', 'time']
#         widgets = {
#             'date': forms.DateInput(attrs={'type': 'date'}),
#             'time': forms.TimeInput(attrs={'type': 'time'}),
#             'number_people': forms.TextInput(attrs={}),
#         }