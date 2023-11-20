from django.db          import models
from form.models        import Hospitals
# Create your models here.

#blank=True
class EditHospitals(models.Model):
    add_hospital_name                      = models.CharField(max_length=100,null=True,blank=True)
    remove_hospital_name                   = models.ForeignKey(Hospitals,on_delete=models.PROTECT,null=True,blank=True)