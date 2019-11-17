from django.db import models

# Create your models here.
class patient(models.Model):
    name_of_patient= models.CharField(max_length=100)
    name_of_doctor=models.CharField(max_length=100)
    patient_pescribtion=models.TextField(max_length=500)
    prescribtion_date=models.DateField(auto_now=False, auto_now_add=False)
    time_for_medication=models.TimeField(auto_now=False, auto_now_add=False)

