from django.db          import models
from form.models        import (
    Hospitals, 
    Diagnosis, 
    SurgicalProcedure, 
    Instruments, 
    InstrumentIssues,
    CartIssues,
    DeviceIssues,
)
# Create your models here.

#blank=True
class EditHospitals(models.Model):
    add                      = models.CharField(
                                                    max_length=100,
                                                    null=True,
                                                    blank=True
                                                )
    remove                   = models.ForeignKey(
                                                    Hospitals,
                                                    on_delete=models.PROTECT,
                                                    null=True,
                                                    blank=True
                                                )

class EditDiagnosis(models.Model):
    add                      = models.CharField(
                                                            max_length=100,
                                                            null=True,
                                                            blank=True,
                                                            default=None                                                    
                                                        )
    remove                   = models.ForeignKey(
                                                            Diagnosis,
                                                            on_delete=models.PROTECT,
                                                            null=True,
                                                            blank=True)
    
class EditSurgicalProcedure(models.Model):
    add                  = models.CharField(
                                                            max_length=100,
                                                            null=True,
                                                            blank=True,
                                                            default=None
                                                        )
    remove               = models.ForeignKey(
                                                            SurgicalProcedure,
                                                            on_delete=models.PROTECT,
                                                            null=True,
                                                            blank=True,
                                                        )
                                                        
class EditInstruments(models.Model):
    add                          = models.CharField(
                                                            max_length=100,
                                                            null=True,
                                                            blank=True,
                                                            default=None
                                                        ) 
    remove                       = models.ForeignKey(
                                                            Instruments,
                                                            on_delete=models.PROTECT,
                                                            null=True,
                                                            blank=True,
                                                        )


class EditInstrumentsIssues(models.Model):
    add                          = models.CharField(
                                                            max_length=100,
                                                            null=True,
                                                            blank=True,
                                                            default=None
                                                        ) 
    remove                       = models.ForeignKey(
                                                            InstrumentIssues,
                                                            on_delete=models.PROTECT,
                                                            null=True,
                                                            blank=True,
                                                        )    

class EditCartIssues(models.Model):
    add                          = models.CharField(
                                                            max_length=100,
                                                            null=True,
                                                            blank=True,
                                                            default=None
                                                        ) 
    remove                       = models.ForeignKey(
                                                            CartIssues,
                                                            on_delete=models.PROTECT,
                                                            null=True,
                                                            blank=True,
                                                        )   

class EditDeviceIssues(models.Model):
    add                          = models.CharField(
                                                            max_length=100,
                                                            null=True,
                                                            blank=True,
                                                            default=None
                                                        ) 
    remove                       = models.ForeignKey(
                                                            DeviceIssues,
                                                            on_delete=models.PROTECT,
                                                            null=True,
                                                            blank=True,
                                                        )                   