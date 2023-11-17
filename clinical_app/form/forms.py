from django         import forms

class clinical_form(forms.Form):

    # later need to add these choices in database
    hospital_choices = [
        ('1', 'RGCI'),
        ('2', 'Fortis')
    ]

    #hospital_name   = forms.CharField(label="Hospital name",max_length=100)
    hospital_name   = forms.CharField(label="Hospital Name", widget=forms.Select(choices=hospital_choices),required=False)
    patient_name    = forms.CharField(label="Patient name",max_length=100,required=False)

    class Meta:
        request = "POST"
        button  = "enable"
