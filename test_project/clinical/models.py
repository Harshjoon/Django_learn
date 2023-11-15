from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

'''
CLASS MODEL REPRESENTS CLINICAL SURGERY DATA
- Hospital name
- Patient name
- Surgery type
- Surgery date
'''

class Data(models.Model):
    hospital_name   = models.CharField(max_length=100)
    patient_name    = models.CharField(max_length=100)
    surgery_type    = models.CharField(max_length=100)
    #surgery_date    = models.DateTimeField(auto_now=False)
    surgery_date    = models.DateTimeField(default=timezone.now)

    author          = models.ForeignKey(User, on_delete=models.CASCADE) # if user is deleted, its data is also deleted
    

