from django.db          import models
from django.utils       import timezone
from django.contrib.auth.models     import User

class Post(models.Model):
    hospital_name       = models.CharField(max_length=100)
    patient_name        = models.CharField(max_length=100)
    #date_added          = models.DateTimeField(auto_now=True)
    #date_added          = models.DateTimeField(auto_now_add=True)
    date_added          = models.DateTimeField(default=timezone.now)
    author              = models.ForeignKey(User, on_delete=models.CASCADE) # delete data if user is deleted
    
    def __str__(self):
        return self.patient_name