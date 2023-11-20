from django         import forms
from django.forms   import ModelForm
from .models        import EditHospitals

class EditHospitalsForm(ModelForm):
    class Meta:
        model       = EditHospitals
        fields      = [
            'add_hospital_name',
            'remove_hospital_name'
        ]