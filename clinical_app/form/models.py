from django.db          import models
from django.utils       import timezone
from django.contrib.auth.models     import User
from .form_choices      import *
from django.contrib.postgres.fields import ArrayField

#blank=True
class Hospitals(models.Model):
    hospital_name                   = models.CharField(max_length=100)
    def __str__(self):
        return self.hospital_name

class Diagnosis(models.Model):
    diagnosis_name                  = models.CharField(max_length=100)
    def __str__(self):
        return self.diagnosis_name
    
class SurgicalProcedure(models.Model):
    surgical_procedure              = models.CharField(max_length=100)
    def __str__(self):
        return self.surgical_procedure

class Instruments(models.Model):
    instrument_name                 = models.CharField(max_length=100)
    def __str__(self):
        return self.instrument_name

class Post(models.Model):
    hospital_name                   = models.ForeignKey(Hospitals,on_delete=models.PROTECT,null=True,blank=True)


    patient_id                      = models.CharField(max_length=100,null=True,blank=True)
    patient_name                    = models.CharField(max_length=100,null=True,blank=True)
    gender                          = models.CharField(
                                        max_length=1,
                                        choices=GENDER_CHOICES,null=True,blank=True
                                        )
    age                             = models.IntegerField(null=True,blank=True)
    height                          = models.IntegerField(null=True,blank=True)
    weight                          = models.IntegerField(null=True,blank=True)

    author                          = models.ForeignKey(User, on_delete=models.PROTECT)

    # diagnosis                       = models.CharField(
    #                                     max_length=3,
    #                                     choices=DIAGNOSIS_CHOICES,null=True,blank=True
    #                                     )
    
    diagnosis                       = models.ForeignKey(Diagnosis,on_delete=models.PROTECT,null=True,blank=True)
    
    case_no                         = models.IntegerField(null=True,blank=True)
    date_of_admission               = models.DateTimeField(null=True,blank=True)
    date_of_surgery                 = models.DateTimeField(null=True,blank=True)
    # surgical_procedure              = models.CharField(
    #                                     max_length=3,
    #                                     choices=SURGICAL_PROCEDURE_CHOICES,null=True,blank=True
    #                                     )
    surgical_procedure              = models.ForeignKey(SurgicalProcedure, on_delete=models.PROTECT, null=True,blank=True)

    surgeon_name_1                  = models.CharField(max_length=100,null=True,blank=True)
    surgeon_name_2                  = models.CharField(max_length=100,null=True,blank=True)

    assistant_surgeon_name_1        = models.CharField(max_length=100,null=True,blank=True)
    assistant_surgeon_name_2        = models.CharField(max_length=100,null=True,blank=True)
    assistant_surgeon_name_3        = models.CharField(max_length=100,null=True,blank=True)

    patient_in_time                 = models.TimeField(null=True,blank=True)
    patient_out_time                = models.TimeField(null=True,blank=True)
    system_on_time                  = models.TimeField(null=True,blank=True)
    system_off_time                 = models.TimeField(null=True,blank=True)
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

    #instrument_used_temp            = models.ForeignKey(Instruments, on_delete=models.PROTECT, null=True,blank=True)
    #instrument_used_temp_1          = models.ForeignKey(Instruments, on_delete=models.PROTECT, null=True,blank=True)

    # instrument_test                 = ArrayField(
    #                                     models.ForeignKey(Instruments, on_delete=models.PROTECT, null=True,blank=True),
    #                                         size=10   
    #                                         )

    instrument_test                 = models.ManyToManyField(
                                                'form.Instruments',
                                                related_name='instruments'
                                            )
    
    # instrument_test                 = ArrayField(
    #                                         models.ManyToManyField(
    #                                             'form.Instruments'
    #                                         ),
    #                                         size=10                                                   
    #                                     )

    #instrument_used_2               = models.ForeignKey(Instruments, on_delete=models.PROTECT, null=True,blank=True)
    #instrument_used_3               = models.ForeignKey(Instruments, on_delete=models.PROTECT, null=True,blank=True)
    #instrument_used_4               = models.ForeignKey(Instruments, on_delete=models.PROTECT, null=True,blank=True)
    #instrument_used_5               = models.ForeignKey(Instruments, on_delete=models.PROTECT, null=True,blank=True)

    instrument_used_1               = models.CharField(
                                        max_length=3,
                                        choices=INSTRUMENT_CHOICES,null=True,blank=True
                                    )
    instrument_used_2               = models.CharField(
                                        max_length=3,
                                        choices=INSTRUMENT_CHOICES,null=True,blank=True
                                    )
    instrument_used_3               = models.CharField(
                                        max_length=3,
                                        choices=INSTRUMENT_CHOICES,null=True,blank=True
                                    )
    instrument_used_4               = models.CharField(
                                        max_length=3,
                                        choices=INSTRUMENT_CHOICES,null=True,blank=True
                                    )
    instrument_used_5               = models.CharField(
                                        max_length=3,
                                        choices=INSTRUMENT_CHOICES,null=True,blank=True
                                    )

    cart_issue                      = models.CharField(
                                        max_length=3,
                                        choices=CART_ISSUE_CHOICES,null=True,blank=True
                                    )
    
    device_issue                    = models.CharField(
                                        max_length=3,
                                        choices=DEVICE_ISSUE_CHOICES,null=True,blank=True
                                    )

    device_patient_complications    = models.CharField(max_length=100,null=True,blank=True)

    date_of_discharge               = models.DateTimeField(null=True,blank=True)
    length_of_stay                  = models.DurationField(null=True,blank=True)
    readmission                     = models.BooleanField(null=True,blank=True)

    post_discharge_complications    = models.CharField(max_length=100,null=True,blank=True)

    surgical_steps                  = models.CharField(max_length=200,null=True,blank=True)

    total_blood_loss                = models.IntegerField(null=True,blank=True)

    # def __str__(self):
    #     return self.patient_name






# class Post(models.Model):
#     #hospital_name       = models.CharField(max_length=100)
#     #patient_name        = models.CharField(max_length=100)
#     #date_added          = models.DateTimeField(auto_now=True)
#     #date_added          = models.DateTimeField(auto_now_add=True)
#     #date_added          = models.DateTimeField(default=timezone.now)
#     #author              = models.ForeignKey(User, on_delete=models.CASCADE) # delete data if user is deleted
    

#     hospital_name                   = models.CharField(max_length=100,null=True)
#     patient_id                      = models.CharField(max_length=100,null=True)
#     patient_name                    = models.CharField(max_length=100,null=True)
#     gender                          = models.CharField(
#                                         max_length=1,
#                                         choices=GENDER_CHOICES,null=True
#                                         )
#     age                             = models.IntegerField(null=True)
#     height                          = models.IntegerField(null=True)
#     weight                          = models.IntegerField(null=True)

#     author                          = models.ForeignKey(User, on_delete=models.PROTECT)

#     diagnosis                       = models.CharField(
#                                         max_length=3,
#                                         choices=DIAGNOSIS_CHOICES,null=True
#                                         )
    
#     case_no                         = models.IntegerField(null=True)
#     date_of_admission               = models.DateTimeField(null=True)
#     date_of_surgery                 = models.DateTimeField(null=True)
#     surgical_procedure              = models.CharField(
#                                         max_length=3,
#                                         choices=SURGICAL_PROCEDURE_CHOICES,null=True
#                                         )

#     surgeon_name_1                  = models.CharField(max_length=100,null=True)
#     surgeon_name_2                  = models.CharField(max_length=100,null=True)

#     assistant_surgeon_name_1        = models.CharField(max_length=100,null=True)
#     assistant_surgeon_name_2        = models.CharField(max_length=100,null=True)
#     assistant_surgeon_name_3        = models.CharField(max_length=100,null=True)

#     patient_in_time                 = models.TimeField(null=True)
#     patient_out_time                = models.TimeField(null=True)
#     system_on_time                  = models.TimeField(null=True)
#     system_off_time                 = models.TimeField(null=True)
#     draping_start_time              = models.TimeField(null=True)
#     draping_end_time                = models.TimeField(null=True)
#     patient_incision_time           = models.TimeField(null=True)
#     patient_skin_closure_time       = models.TimeField(null=True)
#     port_placement_start_time       = models.TimeField(null=True)
#     cart_pos_and_doc_start_timem    = models.TimeField(null=True)
#     cart_pos_and_doc_end_time       = models.TimeField(null=True)
#     console_start_time              = models.TimeField(null=True)
#     console_end_time                = models.TimeField(null=True)
#     console_interruption_time       = models.IntegerField(null=True)
#     cart_undock_start_time          = models.IntegerField(null=True)
#     cart_undock_end_time            = models.IntegerField(null=True)

#     instrument_used_1               = models.CharField(
#                                         max_length=3,
#                                         choices=INSTRUMENT_CHOICES,null=True
#                                     )
#     instrument_used_2               = models.CharField(
#                                         max_length=3,
#                                         choices=INSTRUMENT_CHOICES,null=True
#                                     )
#     instrument_used_3               = models.CharField(
#                                         max_length=3,
#                                         choices=INSTRUMENT_CHOICES,null=True
#                                     )
#     instrument_used_4               = models.CharField(
#                                         max_length=3,
#                                         choices=INSTRUMENT_CHOICES,null=True
#                                     )
#     instrument_used_5               = models.CharField(
#                                         max_length=3,
#                                         choices=INSTRUMENT_CHOICES,null=True
#                                     )

#     cart_issue                      = models.CharField(
#                                         max_length=3,
#                                         choices=CART_ISSUE_CHOICES,null=True
#                                     )
    
#     device_issue                    = models.CharField(
#                                         max_length=3,
#                                         choices=DEVICE_ISSUE_CHOICES,null=True
#                                     )

#     device_patient_complications    = models.CharField(max_length=100,null=True)

#     date_of_discharge               = models.DateTimeField(null=True)
#     length_of_stay                  = models.DurationField(null=True)
#     readmission                     = models.BooleanField(null=True)

#     post_discharge_complications    = models.CharField(max_length=100,null=True)

#     surgical_steps                  = models.CharField(max_length=200,null=True)

#     total_blood_loss                = models.IntegerField(null=True)

#     # def __str__(self):
#     #     return self.patient_name
    
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