from django         import forms
from django.forms   import ModelForm
from .models        import Post
from .form_choices  import *

# class clinical_form(forms.Form):

#     hospital_name                   = forms.CharField(max_length=100, required=False)
#     patient_id                      = forms.CharField(max_length=100, required=False)
#     patient_name                    = forms.CharField(max_length=100, required=False)
#     gender                          = forms.CharField(
#                                         max_length=1,
#                                         widget=forms.Select(choices=GENDER_CHOICES), required=False
#                                         )
#     age                             = forms.IntegerField(required=False)
#     height                          = forms.IntegerField(required=False)
#     weight                          = forms.IntegerField(required=False)

#     diagnosis                       = forms.CharField(
#                                         max_length=3,
#                                         widget=forms.Select(choices=DIAGNOSIS_CHOICES), required=False
#                                         )
    
#     case_no                         = forms.IntegerField(required=False)
#     date_of_admission               = forms.DateTimeField(required=False)
#     date_of_surgery                 = forms.DateTimeField(required=False)
#     surgical_procedure              = forms.CharField(
#                                         max_length=3,
#                                         widget=forms.Select(choices=SURGICAL_PROCEDURE_CHOICES), required=False
#                                         )

#     surgeon_name_1                  = forms.CharField(max_length=100, required=False)
#     surgeon_name_2                  = forms.CharField(max_length=100, required=False)

#     assistant_surgeon_name_1        = forms.CharField(max_length=100, required=False)
#     assistant_surgeon_name_2        = forms.CharField(max_length=100, required=False)
#     assistant_surgeon_name_3        = forms.CharField(max_length=100, required=False)

#     patient_in_time                 = forms.TimeField(required=False)
#     patient_out_time                = forms.TimeField(required=False)
#     system_on_time                  = forms.TimeField(required=False)
#     system_off_time                 = forms.TimeField(required=False)
#     draping_start_time              = forms.TimeField(required=False)
#     draping_end_time                = forms.TimeField(required=False)
#     patient_incision_time           = forms.TimeField(required=False)
#     patient_skin_closure_time       = forms.TimeField(required=False)
#     port_placement_start_time       = forms.TimeField(required=False)
#     cart_pos_and_doc_start_timem    = forms.TimeField(required=False)
#     cart_pos_and_doc_end_time       = forms.TimeField(required=False)
#     console_start_time              = forms.TimeField(required=False)
#     console_end_time                = forms.TimeField(required=False)
#     console_interruption_time       = forms.IntegerField(required=False)
#     cart_undock_start_time          = forms.IntegerField(required=False)
#     cart_undock_end_time            = forms.IntegerField(required=False)

#     instrument_used_1               = forms.CharField(
#                                         max_length=3,
#                                         widget=forms.Select(choices=INSTRUMENT_CHOICES), required=False
#                                     )
#     instrument_used_2               = forms.CharField(
#                                         max_length=3,
#                                         widget=forms.Select(choices=INSTRUMENT_CHOICES), required=False
#                                     )
#     instrument_used_3               = forms.CharField(
#                                         max_length=3,
#                                         widget=forms.Select(choices=INSTRUMENT_CHOICES), required=False
#                                     )
#     instrument_used_4               = forms.CharField(
#                                         max_length=3,
#                                         widget=forms.Select(choices=INSTRUMENT_CHOICES), required=False
#                                     )
#     instrument_used_5               = forms.CharField(
#                                         max_length=3,
#                                         widget=forms.Select(choices=INSTRUMENT_CHOICES), required=False
#                                     )

#     cart_issue                      = forms.CharField(
#                                         max_length=3,
#                                         widget=forms.Select(choices=CART_ISSUE_CHOICES), required=False
#                                     )
    
#     device_issue                    = forms.CharField(
#                                         max_length=3,
#                                         widget=forms.Select(choices=DEVICE_ISSUE_CHOICES), required=False
#                                     )

#     device_patient_complications    = forms.CharField(max_length=100, required=False)

#     date_of_discharge               = forms.DateTimeField(required=False)
#     length_of_stay                  = forms.DurationField(required=False)
#     readmission                     = forms.BooleanField(required=False)

#     post_discharge_complications    = forms.CharField(max_length=100, required=False)

#     surgical_steps                  = forms.CharField(max_length=200, required=False)

#     total_blood_loss                = forms.IntegerField(required=False)

#     class Meta:
#         request = "POST"
#         button  = "enable"



class clinical_form(ModelForm):
    class Meta:
        model       = Post
        fields      = [
            'hospital_name',
            'patient_id',
            'patient_name',
            'gender',
            'age',
            'height',
            'weight',
            'diagnosis',
            'case_no',
            'date_of_admission',
            'date_of_surgery',
            'surgical_procedure',
            'surgeon_name_1',
            'surgeon_name_2',
            'assistant_surgeon_name_1',
            'assistant_surgeon_name_2',
            'assistant_surgeon_name_3',
            'patient_in_time',
            'patient_out_time',
            'system_on_time',
            'system_off_time',
            'draping_start_time',
            'draping_end_time',
            'patient_incision_time',
            'patient_skin_closure_time',
            'port_placement_start_time',
            'cart_pos_and_doc_start_timem',
            'cart_pos_and_doc_end_time',
            'console_start_time',
            'console_end_time',
            'console_interruption_time',
            'cart_undock_start_time',
            'cart_undock_end_time',
            'instrument_used_1',
            'instrument_used_2',
            'instrument_used_3',
            'instrument_used_4',
            'instrument_used_5',
            'cart_issue',
            'device_issue',
            'device_patient_complications',
            'date_of_discharge',
            'length_of_stay',
            'readmission',  
            'post_discharge_complications',  
            'surgical_steps',   
            'total_blood_loss',  

            # FOR TESTING
            'instrument_test'          
        ]