from django.db          import models
from django.utils       import timezone
from django.contrib.auth.models     import User
from .form_choices      import *
from django.contrib.postgres.fields import ArrayField
from django.utils.translation import gettext_lazy as _


class BugReport(models.Model):
    bug_text               = models.TextField()#null=True,blank=True)
    author                 = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)

#blank=True
class Hospitals(models.Model):
    name                   = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Diagnosis(models.Model):
    name                  = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
class SurgicalProcedure(models.Model):
    name                  = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Instruments(models.Model):
    name                  = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class InstrumentIssues(models.Model):
    name                  = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class CartIssues(models.Model):
    name                  = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class DeviceIssues(models.Model):
    name                  = models.CharField(max_length=100)
    def __str__(self):
        return self.name


class Instruments_list(models.Model):
    #name                    = models.CharField(max_length=100)
    choices                 = models.ManyToManyField(
                                        #'form.Instruments',
                                        Instruments,
                                        #related_name='instruments'
                                    )

class Post(models.Model):
    hospital_name                   = models.ForeignKey(Hospitals,on_delete=models.PROTECT)#,null=True,blank=True)

    patient_id                      = models.CharField(max_length=100)#,null=True,blank=True)
    patient_name                    = models.CharField(max_length=100)#,null=True,blank=True)
    gender                          = models.CharField(
                                        max_length=1,
                                        choices=GENDER_CHOICES#,null=True,blank=True
                                        )

    age                             = models.IntegerField()#null=True,blank=True)
    height                          = models.IntegerField(null=True,blank=True)
    weight                          = models.IntegerField(null=True,blank=True)
    author                          = models.ForeignKey(User, on_delete=models.PROTECT)
    
    #diagnosis                       = models.ForeignKey(Diagnosis,on_delete=models.PROTECT)#,null=True,blank=True)
    diagnosis                       = models.CharField(max_length=100)

    case_no                         = models.IntegerField()#null=True,blank=True)
    date_of_admission               = models.DateTimeField(null=True,blank=True)
    date_of_surgery                 = models.DateTimeField()#null=True,blank=True)
    surgical_procedure              = models.ForeignKey(SurgicalProcedure, on_delete=models.PROTECT)#, null=True,blank=True)

    surgeon_name_1                  = models.CharField(max_length=100,null=True,blank=True)
    surgeon_name_2                  = models.CharField(max_length=100,null=True,blank=True)

    assistant_surgeon_name_1        = models.CharField(max_length=100,null=True,blank=True)
    assistant_surgeon_name_2        = models.CharField(max_length=100,null=True,blank=True)
    #assistant_surgeon_name_3        = models.CharField(max_length=100,null=True,blank=True)

    patient_in_time                 = models.TimeField(null=True,blank=True)
    patient_out_time                = models.TimeField(null=True,blank=True)
    system_on_time                  = models.TimeField()#null=True,blank=True)
    system_off_time                 = models.TimeField()#null=True,blank=True)
    draping_start_time              = models.TimeField(null=True,blank=True)
    draping_end_time                = models.TimeField(null=True,blank=True)
    patient_incision_time           = models.TimeField(null=True,blank=True)
    patient_skin_closure_time       = models.TimeField(null=True,blank=True)
    port_placement_start_time       = models.TimeField(null=True,blank=True)
    cart_pos_and_doc_start_timem    = models.TimeField(null=True,blank=True)
    cart_pos_and_doc_end_time       = models.TimeField(null=True,blank=True)
    console_start_time              = models.TimeField(null=True,blank=True)
    console_end_time                = models.TimeField(null=True,blank=True)
    console_interruption_time       = models.IntegerField(null=True,blank=True)
    cart_undock_start_time          = models.IntegerField(null=True,blank=True)
    cart_undock_end_time            = models.IntegerField(null=True,blank=True)

    instrument_used_1               = models.ForeignKey(Instruments, on_delete=models.PROTECT, null=True,blank=True,related_name='instrument1')
    instrument_1_id                 = models.IntegerField(null=True,blank=True)
    instrument_used_2               = models.ForeignKey(Instruments, on_delete=models.PROTECT, null=True,blank=True,related_name='instrument2')
    instrument_2_id                 = models.IntegerField(null=True,blank=True)
    instrument_used_3               = models.ForeignKey(Instruments, on_delete=models.PROTECT, null=True,blank=True,related_name='instrument3')
    instrument_3_id                 = models.IntegerField(null=True,blank=True)
    instrument_used_4               = models.ForeignKey(Instruments, on_delete=models.PROTECT, null=True,blank=True,related_name='instrument4')
    instrument_4_id                 = models.IntegerField(null=True,blank=True)
    instrument_used_5               = models.ForeignKey(Instruments, on_delete=models.PROTECT, null=True,blank=True,related_name='instrument5')
    instrument_5_id                 = models.IntegerField(null=True,blank=True)
    case_converted                  = models.BooleanField(null=True,blank=True)

    cart_issue                      = models.ForeignKey(CartIssues, on_delete=models.PROTECT,null=True,blank=True)
    #cart_issue_remark               = models.TextField(null=True,blank=True)
    cart_issue_remark               = models.CharField(max_length=200,null=True,blank=True)
    device_issue                    = models.ForeignKey(DeviceIssues, on_delete=models.PROTECT,null=True,blank=True)
    #device_issue_remark             = models.TextField(null=True,blank=True)
    device_issue_remark             = models.CharField(max_length=200,null=True,blank=True)
    instrument_issue                = models.ForeignKey(InstrumentIssues, on_delete=models.PROTECT,null=True,blank=True)
    #instrument_issue_remark         = models.TextField(null=True,blank=True)
    instrument_issue_remark         = models.CharField(max_length=200,null=True,blank=True)

    device_patient_complications    = models.CharField(max_length=100,null=True,blank=True)
    date_of_discharge               = models.DateTimeField(null=True,blank=True)
    length_of_stay                  = models.DurationField(null=True,blank=True)
    readmission                     = models.BooleanField(null=True,blank=True)

    post_discharge_complications    = models.CharField(max_length=100,null=True,blank=True)

    #surgical_steps                  = models.CharField(max_length=200,null=True,blank=True)
    surgical_steps                  = models.TextField(null=True,blank=True)
    total_blood_loss                = models.IntegerField(null=True,blank=True)
    additional_remark               = models.TextField(null=True,blank=True)
    
'''

- Hospital name
- Patient ID
- Patient name
- Gender
- Age
- Height
- Weight
- Diagnosis
- Case no
- Date of Admission
- Date of surgery
- Surgical procedure
- Surgeon name 1
- Surgeon name 2
- Assitant surgeon name 1
- Assitant surgeon name 2
- Assitant surgeon name 3
- Patient in time
- Patient out time
- System on time
- System off time
- Draping start time
- Draping end time
- Patient incision time
- Patient skin closure time
- Port placement start time
- Port placement end time
- Cart positioning and docking start time
- Cart positioning and docking end time
- Console start time
- Console end time
- Console interruption time
- Cart undock start time
- Cart undock end time
- Instruments used

- Instrument issues
- Cart issues
- Device issue
- Device patient complications

- Date of discharge
- Length of stay
- Readmission
- Post discharge complications

- surgical steps

- total blood loss
'''