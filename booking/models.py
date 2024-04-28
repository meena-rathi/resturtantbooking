from django.db import models
from django.contrib.auth.models import User

class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # ForeignKey to the User model
    email = models.EmailField(max_length=30, null=False, blank=False)
    contact_number = models.CharField(max_length=11, null=False)
    number_people = models.IntegerField(null=True)
    date = models.DateField(null=False)
    time = models.TimeField(null=False)
    
    def __str__(self):
        return f"Reservation for {self.user}{self.user.username} on {self.date} at {self.time} {self.date}"
        #return f"Reservation for {self.user.username} on {self.date} at {self.time} {self.date}"
    
    