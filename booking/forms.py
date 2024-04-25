# from django import forms
# from .models import Reservation
# from datetime import date


# class ReservationsForm(forms.ModelForm):
#     class Meta:
#         model = Reservation
#         fields = ['name','email', 'contact_number', 'number_people', 'date', 'time']
#         widgets = {
#             'date': forms.DateInput(attrs={'type': 'date'}),
#             'time': forms.TimeInput(attrs={'type': 'time'}),
#             'number_people': forms.TextInput(attrs={}),
#         }
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.initial['date'] = date.today()
#         if self.instance.user:  # Check if the reservation is associated with a user
#             self.fields['name'].disabled = True  


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
        self.initial['date'] = date.today()
        self.fields['user'].disabled = True

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.initial['date'] = date.today()
    #     if self.instance.user: 
    #         self.fields['user'].disabled = True 
   
