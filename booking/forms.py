
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
            'contact_number': forms.TextInput(attrs={'id': 'id_contact_number'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['date'].initial = date.today() 
        #self.initial['date'] = date.today()
 

    def clean_contact_number(self):
        contact_number = self.cleaned_data.get('contact_number')
        # Remove any spaces from the contact number
        if ' ' in contact_number:
            raise forms.ValidationError("Spaces are not allowed in the contact number.")
        
        # Check if the contact number matches the specified format
        if not (contact_number.startswith('+491') and len(contact_number) == 13) and \
           not (contact_number.startswith('49') and len(contact_number) == 12) and \
           not (len(contact_number) == 11):
            raise ValidationError("Contact number should be in the format")
        
        return contact_number
    # def clean_date(self):
    #     date = self.cleaned_data.get('date')
    #     if date < date.today():
    #         raise forms.ValidationError("Date cannot be in the past.")
    #     return date

   
 
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