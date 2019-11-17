from django.db import models

# Create your models here.
class doctor(models.Model):
    name_doctor=models.CharField(max_length=100)
    qualification=models.CharField(max_length=100)
    info_of_medication=models.CharField(max_length=100)