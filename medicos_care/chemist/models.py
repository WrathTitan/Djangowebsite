from django.db import models

# Create your models here.
class chemist(models.Model):
    prescribtion_of_patient=models.TextField(max_length=500)
    name_of_pharmacy=models.CharField(max_length=100)