from django         import forms
from django.forms   import ModelForm
from .models        import (
    EditHospitals, 
    EditDiagnosis, 
    EditSurgicalProcedure,
    EditInstruments,
    EditInstrumentsIssues,
    EditCartIssues,
    EditDeviceIssues
)

class EditHospitalsForm(ModelForm):
    class Meta:
        model       = EditHospitals
        fields      = [
            'add',
            'remove'
        ]

class EditDiagnosisForm(ModelForm):
    class Meta:
        model       = EditDiagnosis
        fields      = [
            'add',
            'remove'
        ]

class EditSurgicalProcedureForm(ModelForm):
    class Meta:
        model       = EditSurgicalProcedure
        fields      = [
            'add',
            'remove'
        ]

class EditInstrumentsForm(ModelForm):
    class Meta:
        model       = EditInstruments
        fields      = [
            'add',
            'remove'
        ]

class EditInstrumentsIssuesForm(ModelForm):
    class Meta:
        model       = EditInstrumentsIssues
        fields      = [
            'add',
            'remove'
        ]


class EditCartIssuesForm(ModelForm):
    class Meta:
        model       = EditCartIssues
        fields      = [
            'add',
            'remove'
        ]

class EditDeviceIssuesForm(ModelForm):
    class Meta:
        model       = EditDeviceIssues
        fields      = [
            'add',
            'remove'
        ]