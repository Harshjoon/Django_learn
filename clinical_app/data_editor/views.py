from django.shortcuts import render
from django.contrib.auth.decorators     import user_passes_test , login_required
from django.contrib             import messages
from django.http                import HttpResponseRedirect
from django.shortcuts           import redirect
#from .models                    import edit_hospitals
from .forms                     import (
    EditHospitalsForm, 
    EditDiagnosisForm,
    EditSurgicalProcedureForm,
    EditInstrumentsForm,
    EditCartIssuesForm,
    EditDeviceIssuesForm,
    EditInstrumentsIssuesForm
)
from form.models                import (
    Hospitals,
    Diagnosis,
    SurgicalProcedure,
    Instruments,
    InstrumentIssues
)
#from form.models                import Hospitals
from .functions                 import edit_hospitals, edit_models

def check_admin(user):   
   return user.is_superuser

#@user_passes_test(check_admin)
# @login_required
# def home_page(request):
#     print("-----------------------------")
#     if request.user.is_superuser:
#         return render(request, "data_editor/home.html")
#     else:
#         messages.warning(request, "Only admins can access dashboard")
#         return redirect('login', name="dataeditor-home")
    
@login_required
def home_page(request):

    if request.user.is_superuser:
        if request.method    == 'POST':
            print("request post sent.")

            models_list = [ 
                    Hospitals, 
                    Diagnosis,
                    SurgicalProcedure,
                    Instruments,
                    InstrumentIssues,
                    CartIssues,
                    DeviceIssues, 
                ]

            forms  = [
                EditHospitalsForm(request.POST),
                EditDiagnosisForm(request.POST),
                EditSurgicalProcedureForm(request.POST),
                EditInstrumentsForm(request.POST),
                EditInstrumentsIssuesForm(request.POST),
                EditCartIssuesForm(request.POST),
                EditDeviceIssuesForm(request.POST)  
            ]

            form_names = [
                'edit_hospital_form',
                'edit_diagnosis_form',
                'edit_surgical_procedure_form',
                'edit_instrument_form',
                'edit_instrument_issues_form',
                'edit_cart_issues_form',
                'edit_device_issues_form'
            ]

            print([ form.is_valid() for form in forms ])

            for i,name in enumerate(form_names):
                if request.POST.get(name) != None:
                    if forms[i].is_valid():
                        print("name ---------- ",name)
                        edit_models(models_list[i], forms[i], request)

            messages.success(request, f'Hospital data edited.')

        form_context = {
            "edit_hospital_form"            : EditHospitalsForm(),
            "edit_diagnosis_form"           : EditDiagnosisForm(),
            "edit_surgical_procedure_form"  : EditSurgicalProcedureForm(),
            "edit_instrument_form"          : EditInstrumentsForm(),
            "edit_instrument_issues_form"   : EditInstrumentsIssuesForm(),
            'edit_cart_issues_form'         : EditCartIssuesForm(),
            'edit_device_issues_form'       : EditDeviceIssuesForm()
        }

        return render(request, "data_editor/edit_format.html", form_context)
        
    else:
        messages.warning(request, "Only admins can access dashboard")
        return redirect('login', name="dataeditor-home")