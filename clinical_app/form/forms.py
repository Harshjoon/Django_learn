from django     import forms

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

class surgery_data_form(forms.Form):

    hospital_name       = forms.CharField(max_length=100)
    patient_name        = forms.CharField(max_length=100)
    case_number         = forms.IntegerField()
    patient_age         = forms.IntegerField()
    patient_gender      = forms.CharField(
                                max_length=1,
                                widget=forms.Select(choices=GENDER_CHOICES)
                            )
    
    surgeon_name_1      = forms.CharField(max_length=100)
    surgeon_name_2      = forms.CharField(max_length=100)    

    assistant_surgeron_name_1 = forms.CharField(max_length=100)    
    assistant_surgeron_name_2 = forms.CharField(max_length=100)    
    assistant_surgeron_name_3 = forms.CharField(max_length=100)    

    port_side_nurse_name    = forms.CharField(max_length=100)

    surgery_name        = forms.CharField(max_length=100)

    surgery_start_time  = forms.TimeInput()
    surgery_end_time    = forms.TimeInput()

    system_on_time      = forms.TimeInput()
    system_off_time     = forms.TimeInput()

    draping_start_time  = forms.TimeInput()
    draping_end_time    = forms.TimeInput()

    docking_start_time  = forms.TimeInput()
    docking_end_time    = forms.TimeInput()

    Instrument_used_1   = forms.CharField(
                                max_length=1,
                                widget=forms.Select(choices=INSTRUMENT_CHOICES)
                            )

    case_converted      = forms.BooleanField()

    Instrument_issue    = forms.CharField(
                                max_length=1,
                                widget=forms.Select(choices=INSTRUMENT_ISSUES_CHOICES)
                            )

    class Meta:
        request = 'POST'
        button  = 'enabled'    