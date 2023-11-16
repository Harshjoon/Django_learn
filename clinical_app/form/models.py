from django.db import models
from django.contrib.auth.models import User

GENDER_CHOICES = [
    ("M","Male"),
    ("F","Female"),
]

INSTRUMENT_CHOICES = [
    ('LND', 'Large needle driver'),
    ('MCS', 'Monopoler curved siccors'),
]

INSTRUMENT_ISSUES_CHOICES = [
    ('0', "No issue"),
    ('1', "Issue 1"),
    ('2', "Issue 2"),
    ('3', "Issue 3"),
    ('4', "Issue 4"),
]

class surgery_data(models.Model):

    hospital_name       = models.CharField(max_length=100)
    patient_name        = models.CharField(max_length=100)
    case_number         = models.IntegerField()
    patient_age         = models.IntegerField()
    patient_gender      = models.CharField(
                            max_length=1,
                            choices=GENDER_CHOICES
                            )
    
    author              = models.ForeignKey(User, on_delete=models.PROTECT)
    
    # STAFF INFORMATION
    surgeon_name_1      = models.CharField(max_length=100)
    surgeon_name_2      = models.CharField(max_length=100)

    assistant_surgeon_name_1        = models.CharField(max_length=100)
    assistant_surgeon_name_2        = models.CharField(max_length=100)
    assistant_surgeon_name_3        = models.CharField(max_length=100)

    port_side_nurse_names           = models.CharField(max_length=100)

    surgery_name        = models.CharField(max_length=100)

    surgery_start_time  = models.DateTimeField()
    surgery_end_time    = models.DateTimeField()

    system_on_time      = models.DateTimeField()
    system_off_time     = models.DateTimeField()

    draping_start_time  = models.DateTimeField()
    draping_end_time    = models.DateTimeField()

    docking_start_time  = models.DateTimeField()
    docking_end_time    = models.DateTimeField()

    Instrument_used_1   = models.CharField(
                            max_length=3,
                            choices=INSTRUMENT_CHOICES
                            )
    
    case_converted      = models.BooleanField()

    Instrument_issue    = models.CharField(
                            max_length=3,
                            choices=INSTRUMENT_ISSUES_CHOICES
                            )



'''
-- DATA FORMAT -- 

MAIN DETAILS
- hospital name
- case name
- patient name
- patient age
- patient gender

STAFF INFORMATION
- Surgeon names
- Assistant surgeon names
- Port side nurse name

SURGERY INFORMATION
- Surgery type

TIME INFORMATION
- surgery start time
- surgery end time
- system on time
- system off time
- draping start time
- draping end time
- docking start time
- docking end time
- Instruments used

ISSUES
- Case converted
- Instument Issue
- Cart Issue
- Arm Issue
- Actutor Issue
- TI Issue
- Vision cart Issue
- Software Issue
'''