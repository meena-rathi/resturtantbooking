from django.db import models


# Create your models here.
class Reservation(models.Model):
    name = models.CharField(max_length=30, default="Unnamed")
    email = models.EmailField(max_length=30, null=False, blank=False)
    contact_number = models.CharField(max_length=11, null=False)
    number_people = models.IntegerField(null=True)
    date = models.DateField(null=False)
    time = models.TimeField(null=False)
    
    def __str__(self):
        return f"Reservation for {self.name} {self.email} on {self.date} at {self.time}"
    