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
    EditInstrumentsForm
)
from form.models                import (
    Hospitals,
    Diagnosis,
    SurgicalProcedure,
    Instruments
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

            #form_data       = EditHospitalsForm(request.POST)

            models_list = [ 
                    Hospitals, 
                    Diagnosis,
                    SurgicalProcedure,
                    Instruments 
                ]
            forms  = [
                EditHospitalsForm(request.POST),
                EditDiagnosisForm(request.POST),
                EditSurgicalProcedureForm(request.POST),
                EditInstrumentsForm(request.POST) 
            ]

            form_names = [
                'edit_hospital_form',
                'edit_diagnosis_form',
                'edit_surgical_procedure_form',
                'edit_instrument_form',
            ]

            # print("request post type name",request.POST.get("name"))
            # print("request post type id",request.POST.get("id"))
            # print("request post type form_type",request.POST.get("form_type"))
            print("request post type ",request.POST.get("edit_hospital_form"))
            print("request post type 2",request.POST.get("edit_diagnosis_form"))

            print([ form.is_valid() for form in forms ])

            # if all([ form_.is_valid() for form_ in forms]):
            #     edit_models(models_list, forms, request)

            for i,name in enumerate(form_names):
                if request.POST.get(name) != None:
                    if forms[i].is_valid():
                        print("name ---------- ",name)
                        edit_models(models_list[i], forms[i], request)


            # for i,form in enumerate(forms):
            #     if form.is_valid():
            #         edit_models(models_list[i], form, request)

            messages.success(request, f'Hospital data edited.')

            # return redirect("form-home")

            # #if form_data.is_valid():
            # if any([ form.is_valid() for form in forms ]):
                
            #     print("forms are valid")

            #     edit_models(models, forms, request)
            #     messages.success(request, f'Hospital data edited.')
            #     return redirect("form-home")

            #     '''
            #     edit_hospitals(Hospitals, form_data, request)
            #     messages.success(request, f'Hospital data edited.')
            #     return redirect("form-home")
            #     '''
        # form_context = {
        #     "hospital_form": EditHospitalsForm(),
        # }

        form_context = {
            "edit_hospital_form": EditHospitalsForm(),
            "edit_diagnosis_form": EditDiagnosisForm(),
            "edit_surgical_procedure_form": EditSurgicalProcedureForm(),
            "edit_instrument_form": EditInstrumentsForm(),
        }

        return render(request, "data_editor/edit_format.html", form_context)
        
    else:
        messages.warning(request, "Only admins can access dashboard")
        return redirect('login', name="dataeditor-home")